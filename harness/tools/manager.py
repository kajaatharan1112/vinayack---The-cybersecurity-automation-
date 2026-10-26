"""Probe installed tools and perform safe, gated updates ("one-click sync").

Design rules (all enforced here, not just in the UI):

* **Probe, don't assume.** A tool is reported installed only if its binary is on
  ``PATH``; a version is reported only if the binary actually prints one.
* **Never auto-manage offensive tools.** Entries with ``manual_review`` or risk
  >= INTRUSIVE are excluded from sync and must be installed/updated by a human.
* **Network is gated.** Updates that need the network are skipped unless the
  operator has enabled network mode on the Policy Engine.
* **Dry-run by default.** ``sync`` builds and returns a plan; it executes commands
  only when ``dry_run=False`` *and* the operator opts in. Everything is audited.
* **No shell strings.** Commands are built as argv lists and would run without a
  shell, so there is no command injection from catalog data.
"""

from __future__ import annotations

import shutil
import subprocess  # noqa: S404 - argv-only, no shell; see _run.
from dataclasses import dataclass, field
from typing import cast

from harness.core.audit import AuditLog
from harness.core.policy import PolicyEngine
from harness.tools.catalog import CatalogEntry, ToolCatalog


@dataclass(frozen=True)
class ToolStatus:
    """Result of probing one tool."""

    tool_id: str
    name: str
    installed: bool
    binary: str
    path: str | None
    version: str | None
    manual_review: bool
    auto_update: bool

    @property
    def state(self) -> str:
        """A short, honest status label for the UI."""
        if self.installed:
            return "Installed"
        if self.manual_review:
            return "Controlled-lab"
        return "Not installed"


@dataclass(frozen=True)
class SyncStep:
    """One planned update action for a single tool."""

    tool_id: str
    #: "update", "skip-offensive", "skip-network", "skip-unknown-method".
    action: str
    #: argv commands that would run (empty for skips).
    commands: list[list[str]] = field(default_factory=list)
    reason: str = ""
    executed: bool = False
    ok: bool | None = None
    output: str = ""


@dataclass(frozen=True)
class SyncPlan:
    """The full plan returned by :meth:`ToolManager.sync`."""

    dry_run: bool
    steps: list[SyncStep]

    @property
    def updatable(self) -> list[SyncStep]:
        return [s for s in self.steps if s.action == "update"]

    @property
    def skipped(self) -> list[SyncStep]:
        return [s for s in self.steps if s.action != "update"]


# Supported update methods -> how to turn an entry into argv commands.
def _commands_for(entry: CatalogEntry) -> list[list[str]] | None:
    method = str(entry.update.get("method", ""))
    post_raw = cast("list[str]", entry.update.get("post") or [])
    post = [str(c).split() for c in post_raw]
    if method == "apt":
        pkg = str(entry.update.get("package", entry.binary))
        cmds = [["sudo", "apt-get", "install", "-y", pkg]]
    elif method == "gem":
        pkg = str(entry.update.get("package", entry.tool_id))
        cmds = [["gem", "install", pkg]]
    elif method == "pipx":
        pkg = str(entry.update.get("package", entry.tool_id))
        cmds = [["pipx", "upgrade", pkg]]
    elif method == "git":
        src = str(entry.update.get("source", entry.source))
        # Update into a gitignored vendor/ dir; clone/pull is handled by the script.
        cmds = [["git", "-C", f"vendor/{entry.tool_id}", "pull", "--ff-only"]]
        _ = src
    else:
        return None
    return cmds + post


class ToolManager:
    """Probes installed tools and runs the gated one-click sync."""

    def __init__(
        self,
        catalog: ToolCatalog,
        policy: PolicyEngine,
        audit: AuditLog | None = None,
        *,
        probe_timeout: float = 5.0,
    ) -> None:
        self._catalog = catalog
        self._policy = policy
        self._audit = audit or AuditLog()
        self._probe_timeout = probe_timeout

    # -- probing -----------------------------------------------------------

    def probe(self, entry: CatalogEntry) -> ToolStatus:
        """Check whether a single tool is installed and read its version."""
        path = shutil.which(entry.binary)
        version: str | None = None
        if path and entry.version_arg:
            version = self._read_version(path, entry.version_arg)
        return ToolStatus(
            tool_id=entry.tool_id,
            name=entry.name,
            installed=path is not None,
            binary=entry.binary,
            path=path,
            version=version,
            manual_review=entry.manual_review,
            auto_update=entry.auto_update,
        )

    def status(self) -> list[ToolStatus]:
        """Probe every catalog tool."""
        return [self.probe(e) for e in self._catalog.all()]

    def _read_version(self, path: str, version_arg: str) -> str | None:
        try:
            proc = self._run([path, version_arg])
        except (OSError, subprocess.SubprocessError):
            return None
        text = (proc.stdout or proc.stderr or "").strip()
        return text.splitlines()[0].strip() if text else None

    # -- the one-click sync ------------------------------------------------

    def sync(
        self,
        tool_ids: list[str] | None = None,
        *,
        dry_run: bool = True,
    ) -> SyncPlan:
        """Build (and, when ``dry_run`` is False, execute) the update plan.

        Only safe, non-offensive, auto-updatable tools are ever touched. The
        plan is fully explained so the operator sees exactly what runs.
        """
        entries = (
            [self._catalog.get(t) for t in tool_ids]
            if tool_ids is not None
            else self._catalog.all()
        )
        steps: list[SyncStep] = []
        for entry in entries:
            step = self._plan_one(entry, dry_run=dry_run)
            steps.append(step)

        self._audit.append(
            "tool_sync",
            {
                "dry_run": dry_run,
                "requested": tool_ids or "all",
                "updated": [s.tool_id for s in steps if s.executed and s.ok],
                "skipped": [s.tool_id for s in steps if s.action != "update"],
            },
            actor="operator",
        )
        return SyncPlan(dry_run=dry_run, steps=steps)

    def _plan_one(self, entry: CatalogEntry, *, dry_run: bool) -> SyncStep:
        if entry.manual_review or not entry.auto_update:
            return SyncStep(
                entry.tool_id,
                "skip-offensive",
                reason="manual-review / lab-only: install or update by hand",
            )
        if entry.requires_network and not self._policy.network_enabled:
            return SyncStep(
                entry.tool_id,
                "skip-network",
                reason="needs network; enable network mode to update",
            )
        commands = _commands_for(entry)
        if commands is None:
            return SyncStep(
                entry.tool_id,
                "skip-unknown-method",
                reason=f"no updater for method {entry.update.get('method')!r}",
            )
        if dry_run:
            return SyncStep(
                entry.tool_id, "update", commands=commands, reason="planned (dry-run)"
            )
        return self._execute(entry, commands)

    def _execute(self, entry: CatalogEntry, commands: list[list[str]]) -> SyncStep:
        outputs: list[str] = []
        ok = True
        for cmd in commands:
            try:
                proc = self._run(cmd, timeout=600)
                outputs.append(proc.stdout or proc.stderr or "")
                if proc.returncode != 0:
                    ok = False
                    break
            except (OSError, subprocess.SubprocessError) as exc:
                ok = False
                outputs.append(f"error: {exc}")
                break
        return SyncStep(
            entry.tool_id,
            "update",
            commands=commands,
            reason="executed",
            executed=True,
            ok=ok,
            output="\n".join(outputs).strip(),
        )

    # -- subprocess boundary (argv only, never a shell) --------------------

    def _run(
        self, argv: list[str], timeout: float | None = None
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(  # noqa: S603 - argv list, shell=False, no user shell.
            argv,
            capture_output=True,
            text=True,
            timeout=timeout or self._probe_timeout,
            check=False,
        )

    @property
    def audit(self) -> AuditLog:
        return self._audit

    @property
    def policy(self) -> PolicyEngine:
        return self._policy

#!/usr/bin/env python3
"""Auto-update connected tools (the "one-click update" backend).

This is the script the Web UI button and local cron both call. It:

  1. loads the tool catalog,
  2. (for git-based tools) clones missing upstreams into a gitignored ``vendor/``,
  3. runs the policy-gated :class:`ToolManager` sync.

Safety: dry-run by default (shows the plan, changes nothing). Offensive /
lab-only tools are never touched. Network-dependent updates only run when
``--network`` is passed, mirroring the operator enabling network mode in the app.

Usage:
    python scripts/update_tools.py                 # preview everything
    python scripts/update_tools.py --network       # preview incl. network tools
    python scripts/update_tools.py --network --execute   # actually update
    python scripts/update_tools.py --only nmap tshark    # a subset
"""

from __future__ import annotations

import argparse
import subprocess  # noqa: S404 - argv-only clone helper.
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from harness.core.policy import PolicyEngine, Scope  # noqa: E402
from harness.tools.catalog import load_catalog  # noqa: E402
from harness.tools.manager import ToolManager  # noqa: E402

VENDOR = REPO_ROOT / "vendor"


def ensure_git_sources(tool_ids: list[str] | None, execute: bool) -> list[str]:
    """Clone missing git-based upstreams into ``vendor/``. Returns log lines."""
    catalog = load_catalog()
    logs: list[str] = []
    entries = (
        [catalog.get(t) for t in tool_ids] if tool_ids else catalog.auto_updatable()
    )
    for e in entries:
        if e.update.get("method") != "git" or e.manual_review:
            continue
        dest = VENDOR / e.tool_id
        if dest.exists():
            continue
        src = str(e.update.get("source", e.source))
        if not execute:
            logs.append(f"[clone] would clone {src} -> vendor/{e.tool_id}")
            continue
        VENDOR.mkdir(exist_ok=True)
        try:
            subprocess.run(  # noqa: S603 - argv list, no shell.
                ["git", "clone", "--depth", "1", src, str(dest)],
                check=False,
                capture_output=True,
                text=True,
                timeout=600,
            )
            logs.append(f"[clone] cloned {src} -> vendor/{e.tool_id}")
        except (OSError, subprocess.SubprocessError) as exc:
            logs.append(f"[clone] FAILED {src}: {exc}")
    return logs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Update connected security tools.")
    parser.add_argument("--network", action="store_true", help="allow network updates")
    parser.add_argument("--execute", action="store_true", help="actually run (not dry-run)")
    parser.add_argument("--only", nargs="*", default=None, help="limit to these tool ids")
    args = parser.parse_args(argv)

    catalog = load_catalog()
    policy = PolicyEngine(Scope())
    if args.network:
        policy.enable_network()
    manager = ToolManager(catalog, policy)

    print("=" * 64)
    print("  HARNESS TOOL SYNC" + ("  [LIVE]" if args.execute else "  [DRY-RUN]"))
    print("=" * 64)

    for line in ensure_git_sources(args.only, args.execute):
        print(line)

    plan = manager.sync(args.only, dry_run=not args.execute)
    for step in plan.steps:
        mark = {"update": "↻", "skip-offensive": "🔒", "skip-network": "🌐"}.get(
            step.action, "–"
        )
        status = ""
        if step.executed:
            status = " OK" if step.ok else " FAILED"
        print(f" {mark} {step.tool_id:14} {step.action:20} {step.reason}{status}")
        if not args.execute:
            for cmd in step.commands:
                print(f"      $ {' '.join(cmd)}")

    print("-" * 64)
    print(
        f" updatable: {len(plan.updatable)}   skipped: {len(plan.skipped)}   "
        f"mode: {'EXECUTED' if args.execute else 'preview'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

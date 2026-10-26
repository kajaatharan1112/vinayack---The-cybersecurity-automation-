"""Tests for the policy-gated tool manager (probe + one-click sync)."""

from __future__ import annotations

from harness.core.audit import AuditLog
from harness.core.policy import PolicyEngine, RiskClass, Scope
from harness.tools.catalog import CatalogEntry, ToolCatalog
from harness.tools.manager import ToolManager


def _catalog() -> ToolCatalog:
    return ToolCatalog(
        "test",
        [
            CatalogEntry(
                "safe_net", "SafeNet", "net", RiskClass.ACTIVE, True, "P1",
                "python3", "--version", "src", "MIT",
                {"method": "apt", "package": "python3"},
                auto_update=True, manual_review=False,
            ),
            CatalogEntry(
                "offensive", "Offensive", "lab", RiskClass.DESTRUCTIVE, True, "P5",
                "nonexistent-bin-xyz", None, "src", "GPL",
                {"method": "apt", "package": "evil"},
                auto_update=False, manual_review=True,
            ),
            CatalogEntry(
                "weird", "Weird", "misc", RiskClass.PASSIVE, False, "extra",
                "nonexistent-bin-abc", None, "src", "MIT",
                {"method": "carrier-pigeon"},
                auto_update=True, manual_review=False,
            ),
        ],
    )


def _manager(network: bool = False) -> ToolManager:
    policy = PolicyEngine(Scope())
    if network:
        policy.enable_network()
    return ToolManager(_catalog(), policy, AuditLog())


def test_probe_detects_installed_binary() -> None:
    # python3 is on PATH in the test environment.
    status = _manager().probe(_catalog().get("safe_net"))
    assert status.installed is True
    assert status.path is not None
    assert status.version  # python3 --version prints something


def test_probe_missing_binary() -> None:
    status = _manager().probe(_catalog().get("offensive"))
    assert status.installed is False
    assert status.state == "Controlled-lab"


def test_sync_skips_offensive_tools() -> None:
    plan = _manager(network=True).sync(dry_run=True)
    off = next(s for s in plan.steps if s.tool_id == "offensive")
    assert off.action == "skip-offensive"
    assert off.commands == []


def test_sync_gates_network_tools_when_offline() -> None:
    plan = _manager(network=False).sync(dry_run=True)
    net = next(s for s in plan.steps if s.tool_id == "safe_net")
    assert net.action == "skip-network"


def test_sync_plans_network_tool_when_enabled() -> None:
    plan = _manager(network=True).sync(dry_run=True)
    net = next(s for s in plan.steps if s.tool_id == "safe_net")
    assert net.action == "update"
    assert net.commands[0][:3] == ["sudo", "apt-get", "install"]
    assert net.executed is False  # dry-run never executes


def test_sync_rejects_unknown_update_method() -> None:
    plan = _manager(network=True).sync(dry_run=True)
    weird = next(s for s in plan.steps if s.tool_id == "weird")
    assert weird.action == "skip-unknown-method"


def test_sync_is_audited() -> None:
    mgr = _manager(network=True)
    mgr.sync(dry_run=True)
    assert len(mgr.audit.find("tool_sync")) == 1


def test_dry_run_does_not_execute() -> None:
    plan = _manager(network=True).sync(dry_run=True)
    assert all(not s.executed for s in plan.steps)

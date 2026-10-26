"""End-to-end: objective -> proposed plan -> policy gate -> audited outcome.

Proves the core guarantee: the AI proposes, the Policy Engine decides, and a
network step cannot run until the operator enables network mode.
"""

from __future__ import annotations

from harness.ai.local_stub import LocalStubAdapter
from harness.core.config import HarnessConfig
from harness.core.lifecycle import Harness
from harness.core.policy import Scope


def build_harness() -> Harness:
    scope = Scope(
        allowed_cidrs=["10.0.0.0/24"],
        allowed_tools={"nmap", "ip_intel"},
        allowed_operations={"host_discovery", "service_scan", "local_inventory"},
    )
    harness = Harness(HarnessConfig(), scope=scope)
    harness.start()
    return harness


def test_network_plan_blocked_until_operator_enables_network() -> None:
    harness = build_harness()
    workflow = LocalStubAdapter().plan("discover hosts and services on the lab")

    # Offline: every network step is denied.
    before = [harness.policy.evaluate(s.request) for s in workflow.steps]
    assert all(not r.allowed for r in before)

    # Operator authorizes network mode.
    harness.enable_network()
    after = [harness.policy.evaluate(s.request) for s in workflow.steps]
    assert all(r.allowed for r in after)


def test_emergency_stop_mid_flow_blocks_everything() -> None:
    harness = build_harness()
    harness.enable_network()
    workflow = LocalStubAdapter().plan("discover services")
    assert all(harness.policy.evaluate(s.request).allowed for s in workflow.steps)

    harness.emergency_stop()
    assert all(not harness.policy.evaluate(s.request).allowed for s in workflow.steps)
    assert harness.audit.find("emergency_stop.engaged")

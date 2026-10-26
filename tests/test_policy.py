"""Tests for the authoritative Policy Engine — the project's safety core."""

from __future__ import annotations

import pytest

from harness.core.policy import (
    Decision,
    OperationRequest,
    PolicyEngine,
    RiskClass,
    Scope,
)


def make_engine(**scope_kwargs) -> PolicyEngine:
    scope = Scope(
        allowed_cidrs=["10.0.0.0/24"],
        allowed_domains=["lab.example"],
        allowed_tools={"nmap", "ip_intel"},
        allowed_operations={"host_discovery", "service_scan", "local_inventory"},
        **scope_kwargs,
    )
    return PolicyEngine(scope, network_enabled=True)


def test_allows_in_scope_operation() -> None:
    engine = make_engine()
    req = OperationRequest(
        tool="nmap",
        operation="host_discovery",
        target="10.0.0.5",
        risk=RiskClass.ACTIVE,
        requires_network=True,
    )
    result = engine.evaluate(req)
    assert result.allowed
    assert result.decision is Decision.ALLOW


def test_denies_unapproved_tool() -> None:
    engine = make_engine()
    req = OperationRequest(tool="metasploit", operation="host_discovery")
    result = engine.evaluate(req)
    assert not result.allowed
    assert any("not approved" in r for r in result.reasons)


def test_denies_out_of_scope_ip() -> None:
    engine = make_engine()
    req = OperationRequest(
        tool="nmap",
        operation="host_discovery",
        target="192.168.1.1",
        requires_network=True,
    )
    result = engine.evaluate(req)
    assert not result.allowed
    assert any("outside authorized scope" in r for r in result.reasons)


def test_domain_suffix_matching() -> None:
    engine = make_engine()
    assert engine._scope.target_in_scope("api.lab.example")  # noqa: SLF001
    assert engine._scope.target_in_scope("lab.example")  # noqa: SLF001
    assert not engine._scope.target_in_scope("evil.example")  # noqa: SLF001


def test_network_required_but_disabled_is_denied() -> None:
    engine = make_engine()
    engine.disable_network()
    req = OperationRequest(
        tool="nmap",
        operation="service_scan",
        target="10.0.0.5",
        requires_network=True,
    )
    result = engine.evaluate(req)
    assert not result.allowed
    assert any("network access is not enabled" in r for r in result.reasons)


def test_high_risk_requires_approval() -> None:
    engine = make_engine(max_risk=RiskClass.ACTIVE, high_risk_approval_level=2)
    req = OperationRequest(
        tool="nmap",
        operation="host_discovery",
        target="10.0.0.5",
        risk=RiskClass.INTRUSIVE,
        requires_network=True,
        approval_level=0,
    )
    assert not engine.evaluate(req).allowed
    approved = OperationRequest(
        tool="nmap",
        operation="host_discovery",
        target="10.0.0.5",
        risk=RiskClass.INTRUSIVE,
        requires_network=True,
        approval_level=2,
    )
    assert engine.evaluate(approved).allowed


def test_emergency_stop_denies_everything() -> None:
    engine = make_engine()
    engine.engage_emergency_stop()
    assert not engine.network_enabled
    req = OperationRequest(
        tool="ip_intel",
        operation="local_inventory",
        target=None,
        risk=RiskClass.PASSIVE,
    )
    result = engine.evaluate(req)
    assert not result.allowed
    assert any("emergency stop" in r for r in result.reasons)


def test_empty_scope_denies_remote_target() -> None:
    engine = PolicyEngine(Scope(allowed_tools={"nmap"}), network_enabled=True)
    req = OperationRequest(
        tool="nmap", operation="x", target="8.8.8.8", requires_network=True
    )
    assert not engine.evaluate(req).allowed


def test_local_target_is_in_scope() -> None:
    engine = make_engine()
    req = OperationRequest(
        tool="ip_intel", operation="local_inventory", target=None
    )
    assert engine.evaluate(req).allowed


@pytest.mark.parametrize("bad", [-1, 0])
def test_emergency_reset_restores_evaluation(bad: int) -> None:
    engine = make_engine()
    engine.engage_emergency_stop()
    engine.reset_emergency_stop()
    req = OperationRequest(
        tool="ip_intel", operation="local_inventory", target=None
    )
    assert engine.evaluate(req).allowed

"""Tests for the offline stub adapter. (DeepSeek has its own test module.)"""

from __future__ import annotations

from harness.ai.local_stub import LocalStubAdapter


def test_stub_plans_network_objective() -> None:
    wf = LocalStubAdapter().plan("Discover hosts and exposed services on the lab")
    assert wf.objective
    ops = [s.request.operation for s in wf.steps]
    assert "host_discovery" in ops
    assert "service_scan" in ops
    # Network steps are flagged so the policy engine can gate them.
    assert all(s.request.requires_network for s in wf.steps)


def test_stub_defaults_to_passive_local_plan() -> None:
    wf = LocalStubAdapter().plan("just inspect what I already have locally")
    assert len(wf.steps) == 1
    assert not wf.steps[0].request.requires_network


def test_stub_analyze() -> None:
    assert "2" in LocalStubAdapter().analyze([{}, {}])

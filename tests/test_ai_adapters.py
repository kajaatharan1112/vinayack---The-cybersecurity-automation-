"""Tests for the AI model adapters (stub + DeepSeek scaffold)."""

from __future__ import annotations

import pytest

from harness.ai.deepseek_adapter import DeepSeekAdapter, DeepSeekConfig
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


def test_deepseek_falls_back_when_unconfigured() -> None:
    adapter = DeepSeekAdapter()
    assert not adapter.is_ready
    # Offline-first: unconfigured adapter still plans, via the fallback.
    wf = adapter.plan("discover services")
    assert wf.steps


def test_deepseek_not_ready_without_network_flag() -> None:
    adapter = DeepSeekAdapter(DeepSeekConfig(endpoint="http://localhost:11434"))
    assert not adapter.is_ready  # endpoint set but allow_network is False


def test_deepseek_ready_requires_endpoint_and_network() -> None:
    adapter = DeepSeekAdapter(
        DeepSeekConfig(endpoint="http://localhost:11434", allow_network=True)
    )
    assert adapter.is_ready
    # Real inference is not wired in yet.
    with pytest.raises(NotImplementedError):
        adapter.plan("discover services")

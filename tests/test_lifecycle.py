"""Tests for the offline-first harness lifecycle."""

from __future__ import annotations

import pytest

from harness.core.config import HarnessConfig, OperatingMode
from harness.core.lifecycle import Harness


def test_starts_offline_with_network_disabled() -> None:
    harness = Harness(HarnessConfig())
    harness.start()
    assert harness.started
    assert harness.mode is OperatingMode.OFFLINE
    assert not harness.policy.network_enabled
    # Startup must never leave an audit gap.
    assert harness.audit.find("harness.offline_ready")


def test_enable_and_disable_network() -> None:
    harness = Harness(HarnessConfig())
    harness.start()
    harness.enable_network()
    assert harness.mode is OperatingMode.NETWORK_ENABLED
    assert harness.policy.network_enabled
    assert harness.audit.find("network.enabled")

    harness.disable_network()
    assert harness.mode is OperatingMode.OFFLINE
    assert not harness.policy.network_enabled


def test_emergency_stop_revokes_network() -> None:
    harness = Harness(HarnessConfig())
    harness.start()
    harness.enable_network()
    harness.emergency_stop()
    assert harness.mode is OperatingMode.OFFLINE
    assert not harness.policy.network_enabled
    assert harness.policy.emergency_stopped
    assert harness.audit.find("emergency_stop.engaged")


def test_cannot_enable_network_during_emergency_stop() -> None:
    harness = Harness(HarnessConfig())
    harness.start()
    harness.emergency_stop()
    with pytest.raises(RuntimeError):
        harness.enable_network()
    assert harness.audit.find("network.enable_refused")

"""Tests for the append-only audit log."""

from __future__ import annotations

import json

from harness.core.audit import AuditLog


def test_append_and_read() -> None:
    log = AuditLog()
    log.append("harness.init", {"instance": "test"})
    log.append("policy.loaded")
    assert len(log) == 2
    assert log.events[0].action == "harness.init"
    assert log.events[0].details == {"instance": "test"}


def test_find_by_action() -> None:
    log = AuditLog()
    log.append("network.enabled")
    log.append("network.disabled")
    log.append("network.enabled")
    assert len(log.find("network.enabled")) == 2


def test_event_serializes_to_json() -> None:
    log = AuditLog()
    event = log.append("emergency_stop.engaged", {"reason": "test"}, actor="operator")
    data = json.loads(event.to_json())
    assert data["action"] == "emergency_stop.engaged"
    assert data["actor"] == "operator"
    assert "timestamp" in data


def test_events_view_is_immutable_tuple() -> None:
    log = AuditLog()
    log.append("x")
    assert isinstance(log.events, tuple)

"""Tests for the tool registry."""

from __future__ import annotations

import pytest

from harness.core.policy import RiskClass
from harness.registry.tool_registry import ToolRegistry, ToolSpec, default_registry


def test_register_and_get() -> None:
    reg = ToolRegistry()
    reg.register(ToolSpec("nmap", "Nmap", "network_discovery", RiskClass.ACTIVE, True))
    assert reg.is_registered("nmap")
    assert reg.get("nmap").name == "Nmap"


def test_duplicate_registration_raises() -> None:
    reg = ToolRegistry()
    reg.register(ToolSpec("nmap", "Nmap", "network_discovery"))
    with pytest.raises(ValueError):
        reg.register(ToolSpec("nmap", "Nmap again", "network_discovery"))


def test_get_unknown_raises() -> None:
    with pytest.raises(KeyError):
        ToolRegistry().get("ghost")


def test_load_for_returns_only_requested() -> None:
    reg = default_registry()
    loaded = reg.load_for(["ip_intel"])
    assert [s.tool_id for s in loaded] == ["ip_intel"]


def test_by_category() -> None:
    reg = default_registry()
    assert reg.by_category("ip_intelligence")[0].tool_id == "ip_intel"


def test_default_registry_has_expected_tools() -> None:
    reg = default_registry()
    assert {s.tool_id for s in reg.all()} == {"nmap", "ip_intel", "tshark"}

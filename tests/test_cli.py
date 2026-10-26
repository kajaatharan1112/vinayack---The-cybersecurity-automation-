"""Tests for the terminal interface."""

from __future__ import annotations

from harness.core.config import HarnessConfig
from harness.core.lifecycle import Harness
from harness.interfaces.cli import main, render_status, render_tools
from harness.registry.tool_registry import default_registry


def test_status_command_returns_zero(capsys) -> None:
    rc = main(["status"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "OFFLINE CYBERSECURITY HARNESS ENGINE" in out
    assert "Network Permission  : DISABLED" in out


def test_tools_command_lists_tools(capsys) -> None:
    rc = main(["tools"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "nmap" in out
    assert "ip_intel" in out


def test_render_status_reflects_emergency_stop() -> None:
    harness = Harness(HarnessConfig())
    harness.start()
    harness.emergency_stop()
    banner = render_status(harness, 3)
    assert "Emergency Stop      : ENGAGED" in banner


def test_render_tools_lists_registry() -> None:
    text = render_tools(default_registry())
    assert "tshark" in text

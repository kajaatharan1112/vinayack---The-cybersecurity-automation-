"""Tests for the auto-update script (scripts/update_tools.py)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "update_tools.py"
_spec = importlib.util.spec_from_file_location("update_tools", _SCRIPT)
assert _spec and _spec.loader
update_tools = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(update_tools)


def test_dry_run_returns_zero(capsys) -> None:
    rc = update_tools.main([])
    assert rc == 0
    out = capsys.readouterr().out
    assert "DRY-RUN" in out
    assert "metasploit" in out


def test_git_clone_is_dry_run_by_default() -> None:
    logs = update_tools.ensure_git_sources(None, execute=False)
    assert all("would clone" in line for line in logs) or logs == []


def test_only_subset(capsys) -> None:
    rc = update_tools.main(["--only", "nmap", "--network"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "nmap" in out
    assert "tshark" not in out

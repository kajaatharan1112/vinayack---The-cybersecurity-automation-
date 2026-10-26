"""Tests for the tool catalog loader."""

from __future__ import annotations

import pytest

from harness.core.policy import RiskClass
from harness.tools.catalog import CatalogEntry, ToolCatalog, load_catalog


def test_loads_bundled_catalog() -> None:
    catalog = load_catalog()
    assert len(catalog) >= 22  # the 22 original tools, plus extras
    nmap = catalog.get("nmap")
    assert nmap.name == "Nmap"
    assert nmap.risk is RiskClass.ACTIVE
    assert nmap.requires_network is True
    assert nmap.auto_update is True


def test_all_original_notes_tools_present() -> None:
    catalog = load_catalog()
    ids = {e.tool_id for e in catalog.all()}
    for required in [
        "nmap", "netcat", "wireshark", "tshark", "theharvester", "recon-ng",
        "searchsploit", "nikto", "gobuster", "dirb", "wpscan", "sqlmap",
        "enum4linux", "smbclient", "john", "hashcat", "hydra", "aircrack-ng",
        "ettercap", "metasploit", "set",
    ]:
        assert required in ids, f"{required} missing from catalog"


def test_offensive_tools_are_manual_review() -> None:
    catalog = load_catalog()
    for tid in ["metasploit", "hydra", "sqlmap", "ettercap", "set", "aircrack-ng"]:
        entry = catalog.get(tid)
        assert entry.manual_review is True
        assert entry.auto_update is False
        assert entry.is_offensive is True


def test_auto_updatable_excludes_offensive() -> None:
    catalog = load_catalog()
    auto_ids = {e.tool_id for e in catalog.auto_updatable()}
    assert "nmap" in auto_ids
    assert "metasploit" not in auto_ids
    assert "hydra" not in auto_ids


def test_to_registry_round_trips() -> None:
    catalog = load_catalog()
    reg = catalog.to_registry()
    assert len(reg) == len(catalog)
    assert reg.get("nmap").name == "Nmap"


def test_duplicate_tool_id_rejected() -> None:
    entry = CatalogEntry(
        "dup", "Dup", "x", RiskClass.PASSIVE, False, "", "dup", None, "", ""
    )
    with pytest.raises(ValueError, match="duplicate"):
        ToolCatalog("1", [entry, entry])


def test_get_unknown_raises() -> None:
    with pytest.raises(KeyError):
        load_catalog().get("does-not-exist")

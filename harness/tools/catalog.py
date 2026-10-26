"""Load and model the tool catalog (``resources/tools/catalog.json``).

The catalog is data, not code: new tools are added by editing the JSON file, so
the dashboard, registry, and updater pick them up without code changes. Each
entry maps to a :class:`CatalogEntry`; :meth:`ToolCatalog.to_registry` projects
the catalog into the existing :class:`~harness.registry.tool_registry.ToolRegistry`
so the rest of the harness keeps one view of "known tools".
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import cast

from harness.core.policy import RiskClass
from harness.registry.tool_registry import ToolRegistry, ToolSpec

#: Default catalog location, resolved relative to the repository root.
DEFAULT_CATALOG_PATH = (
    Path(__file__).resolve().parents[2] / "resources" / "tools" / "catalog.json"
)


@dataclass(frozen=True)
class CatalogEntry:
    """One tool's full manifest, as loaded from the catalog JSON."""

    tool_id: str
    name: str
    category: str
    risk: RiskClass
    requires_network: bool
    tier: str
    binary: str
    version_arg: str | None
    source: str
    license: str
    update: dict[str, object] = field(default_factory=dict)
    #: May the harness update this tool as part of a one-click sync?
    auto_update: bool = False
    #: Offensive / high-impact tools: never auto-cloned or auto-updated.
    manual_review: bool = True
    notes_path: str | None = None
    summary: str = ""

    @property
    def is_offensive(self) -> bool:
        """True for tools gated behind manual review / lab-only use."""
        return self.manual_review or self.risk >= RiskClass.INTRUSIVE


def _entry_from_dict(raw: dict[str, object]) -> CatalogEntry:
    try:
        risk = RiskClass[str(raw["risk"]).upper()]
    except KeyError as exc:
        raise ValueError(f"unknown risk class {raw.get('risk')!r}") from exc
    return CatalogEntry(
        tool_id=str(raw["tool_id"]),
        name=str(raw["name"]),
        category=str(raw["category"]),
        risk=risk,
        requires_network=bool(raw["requires_network"]),
        tier=str(raw.get("tier", "")),
        binary=str(raw["binary"]),
        version_arg=(str(raw["version_arg"]) if raw.get("version_arg") else None),
        source=str(raw.get("source", "")),
        license=str(raw.get("license", "")),
        update=cast("dict[str, object]", raw.get("update") or {}),
        auto_update=bool(raw.get("auto_update", False)),
        manual_review=bool(raw.get("manual_review", True)),
        notes_path=(str(raw["notes_path"]) if raw.get("notes_path") else None),
        summary=str(raw.get("summary", "")),
    )


class ToolCatalog:
    """An in-memory view of the catalog with simple lookups."""

    def __init__(self, version: str, entries: list[CatalogEntry]) -> None:
        self.version = version
        self._entries: dict[str, CatalogEntry] = {}
        for entry in entries:
            if entry.tool_id in self._entries:
                raise ValueError(f"duplicate tool_id '{entry.tool_id}' in catalog")
            self._entries[entry.tool_id] = entry

    def all(self) -> list[CatalogEntry]:
        return list(self._entries.values())

    def get(self, tool_id: str) -> CatalogEntry:
        try:
            return self._entries[tool_id]
        except KeyError:
            raise KeyError(f"tool '{tool_id}' is not in the catalog") from None

    def by_category(self, category: str) -> list[CatalogEntry]:
        return [e for e in self._entries.values() if e.category == category]

    def auto_updatable(self) -> list[CatalogEntry]:
        """Tools eligible for a one-click sync (safe, non-offensive)."""
        return [
            e for e in self._entries.values() if e.auto_update and not e.manual_review
        ]

    def to_registry(self) -> ToolRegistry:
        """Project the catalog into a :class:`ToolRegistry`."""
        reg = ToolRegistry()
        for e in self._entries.values():
            reg.register(
                ToolSpec(
                    tool_id=e.tool_id,
                    name=e.name,
                    category=e.category,
                    risk=e.risk,
                    requires_network=e.requires_network,
                )
            )
        return reg

    def __len__(self) -> int:
        return len(self._entries)


def load_catalog(path: Path | str | None = None) -> ToolCatalog:
    """Load the catalog from JSON (defaults to the bundled catalog)."""
    catalog_path = Path(path) if path is not None else DEFAULT_CATALOG_PATH
    data = json.loads(catalog_path.read_text(encoding="utf-8"))
    entries = [_entry_from_dict(t) for t in data.get("tools", [])]
    return ToolCatalog(str(data.get("catalogVersion", "0.0.0")), entries)

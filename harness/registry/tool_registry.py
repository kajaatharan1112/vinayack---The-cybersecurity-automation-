"""Tool registry.

Tools are registered with metadata (risk class, required permissions, supported
architectures, network need). The orchestrator loads only the tools a workflow
needs, keeping memory and permissions minimal.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from harness.core.policy import RiskClass


@dataclass(frozen=True)
class ToolSpec:
    """Metadata describing a registered tool."""

    tool_id: str
    name: str
    category: str
    risk: RiskClass = RiskClass.PASSIVE
    requires_network: bool = False
    supported_arch: frozenset[str] = field(
        default_factory=lambda: frozenset({"arm64", "x86_64"})
    )
    version: str = "0.0.0"


class ToolRegistry:
    """A registry of :class:`ToolSpec` entries."""

    def __init__(self) -> None:
        self._tools: dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        if spec.tool_id in self._tools:
            raise ValueError(f"tool '{spec.tool_id}' is already registered")
        self._tools[spec.tool_id] = spec

    def get(self, tool_id: str) -> ToolSpec:
        try:
            return self._tools[tool_id]
        except KeyError:
            raise KeyError(f"tool '{tool_id}' is not registered") from None

    def is_registered(self, tool_id: str) -> bool:
        return tool_id in self._tools

    def by_category(self, category: str) -> list[ToolSpec]:
        return [t for t in self._tools.values() if t.category == category]

    def all(self) -> list[ToolSpec]:
        """All registered tool specs, in registration order."""
        return list(self._tools.values())

    def load_for(self, tool_ids: list[str]) -> list[ToolSpec]:
        """Return specs for exactly the requested tools (and only those)."""
        return [self.get(tid) for tid in tool_ids]

    def __len__(self) -> int:
        return len(self._tools)


def default_registry() -> ToolRegistry:
    """A small starter registry mirroring the project's first tool families."""
    reg = ToolRegistry()
    reg.register(
        ToolSpec("nmap", "Nmap", "network_discovery", RiskClass.ACTIVE, True)
    )
    reg.register(
        ToolSpec("ip_intel", "IP Intelligence", "ip_intelligence", RiskClass.PASSIVE)
    )
    reg.register(
        ToolSpec("tshark", "TShark", "packet_analysis", RiskClass.PASSIVE)
    )
    return reg

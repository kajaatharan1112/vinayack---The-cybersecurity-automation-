"""Terminal interface for the harness.

A thin client: it renders status and routes commands to the harness. It never
bypasses the Policy Engine.
"""

from __future__ import annotations

import argparse

from harness.core.config import HarnessConfig
from harness.core.lifecycle import Harness
from harness.registry.tool_registry import default_registry
from harness.version import __version__


def render_status(harness: Harness, tool_count: int) -> str:
    """Build the status banner (see master plan §12.1)."""
    net = "ENABLED" if harness.policy.network_enabled else "DISABLED"
    stop = "ENGAGED" if harness.policy.emergency_stopped else "clear"
    lines = [
        "=" * 60,
        "         OFFLINE CYBERSECURITY HARNESS ENGINE",
        "=" * 60,
        f"Version             : {__version__}",
        f"Engine Status       : {'RUNNING' if harness.started else 'STOPPED'}",
        f"Operating Mode      : {harness.mode.value}",
        f"Network Permission  : {net}",
        f"Emergency Stop      : {stop}",
        f"AI Model            : {harness.config.model_adapter}",
        f"Registered Tools    : {tool_count}",
        "=" * 60,
    ]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="harness",
        description="Government-Ready Offline Cybersecurity Harness Engine",
    )
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(
        "command",
        nargs="?",
        default="status",
        choices=["status", "tools"],
        help="command to run (default: status)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    harness = Harness(HarnessConfig())
    harness.start()
    registry = default_registry()

    if args.command == "tools":
        print(render_tools(registry))
        return 0

    print(render_status(harness, len(registry)))
    return 0


def render_tools(registry) -> str:
    """Render the registered tools as a simple table."""
    lines = ["Registered tools:"]
    for spec in registry.all():
        lines.append(f"  {spec.tool_id:12} {spec.category:20} risk={spec.risk.name}")
    return "\n".join(lines)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

"""Terminal interface for the harness.

A thin client: it renders status and routes commands to the harness. It never
bypasses the Policy Engine.
"""

from __future__ import annotations

import argparse

from harness.core.config import HarnessConfig
from harness.core.lifecycle import Harness
from harness.registry.tool_registry import default_registry
from harness.tools.catalog import load_catalog
from harness.tools.manager import ToolManager
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
        choices=["status", "tools", "catalog", "sync", "webui"],
        help="command to run (default: status)",
    )
    parser.add_argument(
        "--network", action="store_true", help="allow network-dependent sync"
    )
    parser.add_argument(
        "--execute", action="store_true", help="run real updates (sync); default dry-run"
    )
    parser.add_argument("--host", default="127.0.0.1", help="webui bind host")
    parser.add_argument("--port", type=int, default=8765, help="webui bind port")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    harness = Harness(HarnessConfig())
    harness.start()

    if args.command == "tools":
        print(render_tools(default_registry()))
        return 0

    if args.command == "catalog":
        print(render_catalog())
        return 0

    if args.command == "sync":
        return run_sync(harness, network=args.network, execute=args.execute)

    if args.command == "webui":  # pragma: no cover - blocking server
        from harness.interfaces.webui import serve

        if args.network:
            harness.policy.enable_network()
        serve(
            args.host,
            args.port,
            allow_execute=args.execute,
            policy=harness.policy,
        )
        return 0

    print(render_status(harness, len(default_registry())))
    return 0


def render_tools(registry) -> str:
    """Render the registered (starter) tools as a simple table."""
    lines = ["Registered tools:"]
    for spec in registry.all():
        lines.append(f"  {spec.tool_id:12} {spec.category:20} risk={spec.risk.name}")
    return "\n".join(lines)


def render_catalog() -> str:
    """Render the full tool catalog with install status."""
    from harness.core.policy import PolicyEngine, Scope

    catalog = load_catalog()
    manager = ToolManager(catalog, PolicyEngine(Scope()))
    lines = [f"Tool catalog v{catalog.version}  ({len(catalog)} tools):", ""]
    lines.append(f"  {'TOOL':16} {'CATEGORY':18} {'RISK':12} {'STATUS':14} VERSION")
    for status in manager.status():
        entry = catalog.get(status.tool_id)
        lines.append(
            f"  {entry.name[:15]:16} {entry.category[:17]:18} "
            f"{entry.risk.name:12} {status.state:14} {status.version or '—'}"
        )
    return "\n".join(lines)


def run_sync(harness: Harness, *, network: bool, execute: bool) -> int:
    """Run the one-click tool sync from the terminal."""
    from harness.core.policy import PolicyEngine, Scope

    policy = PolicyEngine(Scope())
    if network:
        policy.enable_network()
    catalog = load_catalog()
    plan = ToolManager(catalog, policy).sync(dry_run=not execute)
    print(f"Tool sync ({'LIVE' if execute else 'dry-run'}):")
    for step in plan.steps:
        print(f"  {step.tool_id:14} {step.action:20} {step.reason}")
    print(f"\nupdatable: {len(plan.updatable)}  skipped: {len(plan.skipped)}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

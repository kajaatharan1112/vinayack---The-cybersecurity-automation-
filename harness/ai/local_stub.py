"""Deterministic offline stub adapter.

Lets the whole harness (and the test suite) run with no AI model and no network.
It produces a small, predictable plan for IP-intelligence style objectives so the
end-to-end flow can be exercised and CI stays fast and hermetic.
"""

from __future__ import annotations

from harness.ai.base import ModelAdapter, PlannedStep, Workflow
from harness.core.policy import OperationRequest, RiskClass


class LocalStubAdapter(ModelAdapter):
    """A rule-based stand-in for a real local model."""

    name = "local_stub"

    def plan(self, objective: str) -> Workflow:
        text = objective.lower()
        steps: list[PlannedStep] = []

        if "discover" in text or "host" in text or "network" in text:
            steps.append(
                PlannedStep(
                    "Discover live hosts on the authorized subnet",
                    OperationRequest(
                        tool="nmap",
                        operation="host_discovery",
                        target=None,
                        risk=RiskClass.ACTIVE,
                        requires_network=True,
                    ),
                )
            )
        if "service" in text or "port" in text or "expos" in text:
            steps.append(
                PlannedStep(
                    "Identify exposed services",
                    OperationRequest(
                        tool="nmap",
                        operation="service_scan",
                        target=None,
                        risk=RiskClass.ACTIVE,
                        requires_network=True,
                    ),
                )
            )
        if not steps:
            # Default to a safe, passive, local-only inspection.
            steps.append(
                PlannedStep(
                    "Passive local inventory review",
                    OperationRequest(
                        tool="ip_intel",
                        operation="local_inventory",
                        target=None,
                        risk=RiskClass.PASSIVE,
                        requires_network=False,
                    ),
                )
            )

        return Workflow(objective=objective, steps=tuple(steps))

    def analyze(self, results: list[dict]) -> str:
        return f"Analyzed {len(results)} result(s) (offline stub)."

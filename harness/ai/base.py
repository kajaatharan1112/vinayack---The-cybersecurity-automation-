"""Model-adapter interface.

A ``ModelAdapter`` turns an operator's natural-language objective into a *proposed*
:class:`Workflow` and interprets tool results into findings. It has no authority:
the Policy Engine validates every proposed step before anything runs.
"""

from __future__ import annotations

import abc
from dataclasses import dataclass, field

from harness.core.policy import OperationRequest


@dataclass(frozen=True)
class PlannedStep:
    """One proposed step: a description plus the operation it maps to."""

    description: str
    request: OperationRequest


@dataclass(frozen=True)
class Workflow:
    """An ordered, *proposed* plan. Proposed ≠ approved."""

    objective: str
    steps: tuple[PlannedStep, ...] = field(default_factory=tuple)


class ModelAdapter(abc.ABC):
    """Base class for all AI model adapters."""

    #: Short adapter name used in config / audit.
    name: str = "base"

    @abc.abstractmethod
    def plan(self, objective: str) -> Workflow:
        """Propose a workflow for ``objective``. Must not execute anything."""

    @abc.abstractmethod
    def analyze(self, results: list[dict]) -> str:
        """Summarize tool results into a human-readable finding string."""

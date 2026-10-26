"""AI harness: model-adapter interface and concrete adapters.

Adapters only *propose* workflows and *interpret* results. They hold no authority
— the Policy Engine decides what actually runs.
"""

from harness.ai.base import ModelAdapter, PlannedStep, Workflow
from harness.ai.local_stub import LocalStubAdapter

__all__ = ["ModelAdapter", "PlannedStep", "Workflow", "LocalStubAdapter"]

"""DeepSeek harness adapter — SCAFFOLD.

This is the module we grow into the real DeepSeek integration. Today it holds the
wiring (config, offline guard, interface) but does NOT reach the network or load
a model: unless an operator explicitly enables network + endpoint, it falls back
to the deterministic offline planner so the system stays offline-first and tests
stay hermetic.

TODO (future phases):
  * Integrate a local DeepSeek-compatible inference runtime (offline).
  * Implement real plan()/analyze() prompting + structured output parsing.
  * Verify model licensing before any commercial distribution.
"""

from __future__ import annotations

from dataclasses import dataclass

from harness.ai.base import ModelAdapter, Workflow
from harness.ai.local_stub import LocalStubAdapter


@dataclass(frozen=True)
class DeepSeekConfig:
    """Connection settings for a local DeepSeek-compatible runtime."""

    #: Local model identifier (e.g. a GGUF path or served model name).
    model: str = "deepseek-local"
    #: Local inference endpoint. Empty => not configured => offline fallback.
    endpoint: str = ""
    #: Must be explicitly True before any network/endpoint call is attempted.
    allow_network: bool = False
    #: Generation controls (used once real inference is wired in).
    temperature: float = 0.2
    max_tokens: int = 2048


class DeepSeekAdapter(ModelAdapter):
    """Adapter around a local DeepSeek-compatible model.

    While unconfigured or offline it delegates to :class:`LocalStubAdapter`, so the
    harness is fully usable without a model and CI needs no network.
    """

    name = "deepseek"

    def __init__(self, config: DeepSeekConfig | None = None) -> None:
        self.config = config or DeepSeekConfig()
        self._fallback = LocalStubAdapter()

    @property
    def is_ready(self) -> bool:
        """True only when a real model call could be made right now."""
        return bool(self.config.endpoint) and self.config.allow_network

    def plan(self, objective: str) -> Workflow:
        if not self.is_ready:
            # Offline-first: no endpoint / network => deterministic fallback.
            return self._fallback.plan(objective)
        return self._plan_with_model(objective)

    def analyze(self, results: list[dict]) -> str:
        if not self.is_ready:
            return self._fallback.analyze(results)
        return self._analyze_with_model(results)

    # -- real-model hooks (to implement in a later phase) ------------------

    def _plan_with_model(self, objective: str) -> Workflow:  # pragma: no cover
        raise NotImplementedError(
            "Real DeepSeek planning is not wired in yet; configure a local "
            "endpoint and implement this in a later phase."
        )

    def _analyze_with_model(self, results: list[dict]) -> str:  # pragma: no cover
        raise NotImplementedError(
            "Real DeepSeek analysis is not wired in yet."
        )

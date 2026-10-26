"""DeepSeek local-runtime adapter.

Talks to a DeepSeek-compatible model served by a *local* inference runtime that
exposes an OpenAI-style ``/chat/completions`` endpoint — e.g. Ollama
(``http://localhost:11434/v1``), llama.cpp server, or LM Studio. No cloud, no
third-party Python packages (uses :mod:`harness.ai.transport`, which is stdlib).

Safety model:
  * The model only *proposes* a workflow. Its output is **untrusted**: it is
    parsed defensively and still passes through the authoritative Policy Engine
    before anything runs. A malicious or confused plan cannot widen scope.
  * Unknown/garbled risk levels fail **closed** (treated as higher risk, so they
    require operator approval).
  * Offline-first: if no endpoint is configured (or network is not allowed), the
    adapter falls back to the deterministic offline stub.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any

from harness.ai.base import ModelAdapter, PlannedStep, Workflow
from harness.ai.local_stub import LocalStubAdapter
from harness.ai.transport import HttpTransport, Transport, TransportError
from harness.core.policy import OperationRequest, RiskClass

_PLAN_SYSTEM = (
    "You are the planning model for an AUTHORIZED, offline cybersecurity testing "
    "harness. Convert the operator's objective into a JSON workflow. Respond with "
    "ONLY a JSON object of this exact shape and nothing else:\n"
    '{"steps": [{"description": str, "tool": str, "operation": str, '
    '"target": str|null, "risk": "PASSIVE"|"ACTIVE"|"INTRUSIVE"|"DESTRUCTIVE", '
    '"requires_network": bool}]}\n'
    "Only propose steps that are necessary and in-scope. Do not include prose."
)

_ANALYZE_SYSTEM = (
    "You interpret cybersecurity tool results for an authorized test. Summarize "
    "the findings concisely and factually in plain text."
)

_RISK_BY_NAME = {r.name: r for r in RiskClass}


def _parse_risk(value: Any) -> RiskClass:
    """Map a risk string to a :class:`RiskClass`, failing CLOSED on anything odd."""
    # Unknown / missing risk => most cautious that still needs approval.
    return _RISK_BY_NAME.get(str(value).strip().upper(), RiskClass.INTRUSIVE)


def _strip_to_json(text: str) -> str:
    """Remove DeepSeek-R1 <think> blocks and markdown fences, then isolate the
    outermost JSON object."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z0-9]*\s*", "", text)
        text = re.sub(r"\s*```$", "", text).strip()
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return text[start : end + 1]
    return text


@dataclass(frozen=True)
class DeepSeekConfig:
    """Connection settings for a local DeepSeek-compatible runtime."""

    #: Served model name (e.g. ``deepseek-r1``, ``deepseek-coder``).
    model: str = "deepseek-r1"
    #: OpenAI-compatible base URL, e.g. ``http://localhost:11434/v1``.
    #: Empty => not configured => offline fallback.
    endpoint: str = ""
    #: Must be explicitly True before any endpoint call is attempted.
    allow_network: bool = False
    temperature: float = 0.2
    max_tokens: int = 2048
    timeout: float = 60.0
    #: Optional bearer token (local runtimes usually ignore it).
    api_key: str = ""


class DeepSeekError(RuntimeError):
    """Raised when the model response cannot be turned into a valid workflow."""


class DeepSeekAdapter(ModelAdapter):
    """Adapter around a local DeepSeek-compatible model.

    While unconfigured/offline it delegates to :class:`LocalStubAdapter`, so the
    harness is fully usable with no model and CI needs no network.
    """

    name = "deepseek"

    def __init__(
        self,
        config: DeepSeekConfig | None = None,
        transport: Transport | None = None,
    ) -> None:
        self.config = config or DeepSeekConfig()
        self._fallback = LocalStubAdapter()
        self._transport: Transport = transport or HttpTransport()

    @property
    def is_ready(self) -> bool:
        """True only when a real model call could be made right now."""
        return bool(self.config.endpoint) and self.config.allow_network

    # -- public API --------------------------------------------------------

    def plan(self, objective: str) -> Workflow:
        if not self.is_ready:
            return self._fallback.plan(objective)
        response = self._chat(
            [
                {"role": "system", "content": _PLAN_SYSTEM},
                {"role": "user", "content": objective},
            ]
        )
        content = _strip_to_json(self._content(response))
        data = self._loads(content)
        return self._to_workflow(objective, data)

    def analyze(self, results: list[dict]) -> str:
        if not self.is_ready:
            return self._fallback.analyze(results)
        response = self._chat(
            [
                {"role": "system", "content": _ANALYZE_SYSTEM},
                {"role": "user", "content": json.dumps(results)},
            ]
        )
        # Drop any <think> reasoning; return the plain summary.
        return re.sub(
            r"<think>.*?</think>", "", self._content(response), flags=re.DOTALL
        ).strip()

    # -- internals ---------------------------------------------------------

    def _chat(self, messages: list[dict[str, str]]) -> dict[str, Any]:
        url = self.config.endpoint.rstrip("/") + "/chat/completions"
        payload: dict[str, Any] = {
            "model": self.config.model,
            "messages": messages,
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
            "stream": False,
        }
        headers = {}
        if self.config.api_key:
            headers["Authorization"] = f"Bearer {self.config.api_key}"
        try:
            return self._transport.post_json(
                url, payload, timeout=self.config.timeout, headers=headers
            )
        except TransportError as exc:
            raise DeepSeekError(str(exc)) from exc

    @staticmethod
    def _content(response: dict[str, Any]) -> str:
        try:
            content = response["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise DeepSeekError("unexpected model response shape") from exc
        if not isinstance(content, str):
            raise DeepSeekError("model response content was not text")
        return content

    @staticmethod
    def _loads(content: str) -> dict[str, Any]:
        try:
            data = json.loads(content)
        except json.JSONDecodeError as exc:
            raise DeepSeekError("model did not return valid JSON") from exc
        if not isinstance(data, dict):
            raise DeepSeekError("model JSON was not an object")
        return data

    @staticmethod
    def _to_workflow(objective: str, data: dict[str, Any]) -> Workflow:
        raw_steps = data.get("steps")
        if not isinstance(raw_steps, list):
            raise DeepSeekError("model JSON missing a 'steps' list")
        steps: list[PlannedStep] = []
        for item in raw_steps:
            if not isinstance(item, dict):
                raise DeepSeekError("each step must be a JSON object")
            tool = item.get("tool")
            operation = item.get("operation")
            if not isinstance(tool, str) or not isinstance(operation, str):
                raise DeepSeekError("each step needs string 'tool' and 'operation'")
            target = item.get("target")
            target = target if isinstance(target, str) and target else None
            request = OperationRequest(
                tool=tool,
                operation=operation,
                target=target,
                risk=_parse_risk(item.get("risk")),
                requires_network=bool(item.get("requires_network", False)),
            )
            description = item.get("description")
            steps.append(
                PlannedStep(
                    description if isinstance(description, str) else operation,
                    request,
                )
            )
        return Workflow(objective=objective, steps=tuple(steps))

"""Minimal HTTP JSON transport for talking to a local inference runtime.

Uses only the standard library (``urllib``) so the harness keeps zero third-party
runtime dependencies and stays offline-capable. The ``Transport`` protocol lets
tests inject a fake transport, so the suite never touches the network.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Protocol


class TransportError(RuntimeError):
    """Raised when an HTTP request fails or returns non-JSON."""


class Transport(Protocol):
    """Anything that can POST a JSON body and return a parsed JSON response."""

    def post_json(
        self,
        url: str,
        payload: dict[str, Any],
        *,
        timeout: float = 60.0,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        ...


class HttpTransport:
    """A tiny ``urllib``-based JSON client.

    Intended for *local* endpoints (e.g. ``http://localhost:11434/v1``). It does
    not disable TLS verification and adds no implicit network behaviour.
    """

    def post_json(
        self,
        url: str,
        payload: dict[str, Any],
        *,
        timeout: float = 60.0,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url, data=body, method="POST")
        request.add_header("Content-Type", "application/json")
        for key, value in (headers or {}).items():
            request.add_header(key, value)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                raw = response.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise TransportError(f"request to {url} failed: {exc}") from exc
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise TransportError(f"response from {url} was not valid JSON") from exc
        if not isinstance(parsed, dict):
            raise TransportError("expected a JSON object in the response")
        return parsed

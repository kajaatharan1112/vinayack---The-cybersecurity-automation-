"""Tests for the stdlib HTTP transport.

``urllib.request.urlopen`` is monkeypatched, so no real network call is made.
"""

from __future__ import annotations

import io
import json
import urllib.error

import pytest

from harness.ai.transport import HttpTransport, TransportError


class _FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
        return False


def test_post_json_round_trip(monkeypatch) -> None:
    captured = {}

    def fake_urlopen(request, timeout=None):
        captured["url"] = request.full_url
        captured["body"] = request.data
        captured["timeout"] = timeout
        return _FakeResponse(json.dumps({"ok": True}).encode())

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    out = HttpTransport().post_json(
        "http://localhost:11434/v1/chat/completions", {"model": "deepseek-r1"},
        timeout=12.0,
    )
    assert out == {"ok": True}
    assert captured["url"].endswith("/chat/completions")
    assert json.loads(captured["body"])["model"] == "deepseek-r1"
    assert captured["timeout"] == 12.0


def test_network_error_becomes_transport_error(monkeypatch) -> None:
    def boom(request, timeout=None):
        raise urllib.error.URLError("refused")

    monkeypatch.setattr("urllib.request.urlopen", boom)
    with pytest.raises(TransportError):
        HttpTransport().post_json("http://localhost:9/v1/chat/completions", {})


def test_non_json_body_becomes_transport_error(monkeypatch) -> None:
    def junk(request, timeout=None):
        return _FakeResponse(b"<html>not json</html>")

    monkeypatch.setattr("urllib.request.urlopen", junk)
    with pytest.raises(TransportError):
        HttpTransport().post_json("http://localhost:11434/v1/chat/completions", {})

"""Tests for the local Web UI (spun up on an ephemeral port)."""

from __future__ import annotations

import json
import threading
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from harness.core.policy import PolicyEngine, Scope
from harness.interfaces.webui import make_handler
from harness.tools.catalog import load_catalog
from harness.tools.manager import ToolManager


@pytest.fixture()
def server():
    catalog = load_catalog()
    manager = ToolManager(catalog, PolicyEngine(Scope()))
    handler = make_handler(manager, catalog, allow_execute=False)
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    host, port = httpd.server_address
    yield f"http://{host}:{port}"
    httpd.shutdown()
    httpd.server_close()


def _get(url: str) -> tuple[int, str]:
    with urllib.request.urlopen(url, timeout=5) as resp:  # noqa: S310 - localhost only
        return resp.status, resp.read().decode()


def _post(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, data=b"", method="POST")
    with urllib.request.urlopen(req, timeout=5) as resp:  # noqa: S310 - localhost only
        return resp.status, resp.read().decode()


def test_dashboard_renders(server: str) -> None:
    status, body = _get(server + "/")
    assert status == 200
    assert "Tool Center" in body
    assert "Update all connected tools" in body
    assert "Nmap" in body


def test_status_api_returns_json(server: str) -> None:
    status, body = _get(server + "/api/status")
    assert status == 200
    data = json.loads(body)
    assert any(s["tool_id"] == "nmap" for s in data)


def test_sync_api_dry_run(server: str) -> None:
    status, body = _post(server + "/api/sync")
    assert status == 200
    plan = json.loads(body)
    assert plan["dry_run"] is True
    ids = {s["tool_id"]: s for s in plan["steps"]}
    # offensive tools must be skipped, never updated
    assert ids["metasploit"]["action"] == "skip-offensive"


def test_unknown_path_404(server: str) -> None:
    with pytest.raises(urllib.error.HTTPError) as exc:
        _get(server + "/nope")
    assert exc.value.code == 404

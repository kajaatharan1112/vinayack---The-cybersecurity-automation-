"""A lightweight local Web UI for the harness.

Goals: *easy to use* and *offline-first*. It uses only the Python standard
library (``http.server``), binds to ``127.0.0.1`` only, ships no external assets
(no CDN, no fonts, no trackers), and exposes exactly three things:

* ``GET  /``            - a dashboard listing every catalog tool + its real status
* ``GET  /api/status``  - the same data as JSON
* ``POST /api/sync``    - the "Update all connected tools" button (one click)

The button calls :meth:`ToolManager.sync`. By default the server runs in
``dry_run`` mode so a click shows the exact plan without changing the system;
pass ``allow_execute=True`` to let the operator actually run updates. Every sync
is recorded in the audit log, and offensive/lab-only tools are never touched.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from harness.core.policy import PolicyEngine
from harness.tools.catalog import ToolCatalog, load_catalog
from harness.tools.manager import SyncPlan, ToolManager, ToolStatus
from harness.version import __version__

_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cybersecurity Harness - Tools</title>
<style>
 :root{{color-scheme:light dark;--bg:#0f1320;--card:#1a2033;--line:#2b3350;
   --fg:#e8ecf5;--muted:#9aa6c4;--blue:#4c8dff;--green:#39c07a;--red:#ff6b6b;
   --amber:#f0b429;}}
 @media(prefers-color-scheme:light){{:root{{--bg:#f4f6fb;--card:#fff;
   --line:#e2e7f0;--fg:#1a2033;--muted:#5b6478;}}}}
 *{{box-sizing:border-box}}
 body{{margin:0;font:15px/1.5 system-ui,sans-serif;background:var(--bg);
   color:var(--fg);padding:24px}}
 h1{{font-size:20px;margin:0 0 4px}} .sub{{color:var(--muted);margin:0 0 20px}}
 .bar{{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:20px}}
 button{{background:var(--blue);color:#fff;border:0;border-radius:8px;
   padding:10px 18px;font-size:15px;font-weight:600;cursor:pointer}}
 button:disabled{{opacity:.5;cursor:wait}}
 .net{{color:var(--muted);font-size:13px}}
 table{{width:100%;border-collapse:collapse;background:var(--card);
   border:1px solid var(--line);border-radius:12px;overflow:hidden}}
 th,td{{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line);
   font-size:14px}}
 th{{color:var(--muted);font-weight:600;font-size:12px;text-transform:uppercase}}
 tr:last-child td{{border-bottom:0}}
 .pill{{display:inline-block;padding:2px 10px;border-radius:999px;font-size:12px;
   font-weight:600}}
 .ok{{background:rgba(57,192,122,.15);color:var(--green)}}
 .no{{background:rgba(154,166,196,.15);color:var(--muted)}}
 .lab{{background:rgba(240,180,41,.15);color:var(--amber)}}
 code{{color:var(--muted);font-size:12px}}
 #out{{margin-top:16px;white-space:pre-wrap;background:var(--card);
   border:1px solid var(--line);border-radius:12px;padding:14px;font-size:13px;
   font-family:ui-monospace,monospace;display:none}}
</style></head><body>
<h1>🛡️ Cybersecurity Harness — Tool Center</h1>
<p class="sub">v{version} · offline-first · localhost only · the Policy Engine
 decides every action</p>
<div class="bar">
 <button id="sync" onclick="sync()">↻ Update all connected tools</button>
 <span class="net">Network mode: <b id="net">{net}</b> ·
  {mode} (set --allow-execute to run real updates)</span>
</div>
<table><thead><tr><th>Tool</th><th>Category</th><th>Risk</th><th>Status</th>
 <th>Version</th><th>Auto-update</th></tr></thead><tbody>{rows}</tbody></table>
<div id="out"></div>
<script>
async function sync(){{
 const b=document.getElementById('sync'),o=document.getElementById('out');
 b.disabled=true;b.textContent='Working…';o.style.display='block';
 o.textContent='Running sync…';
 try{{const r=await fetch('/api/sync',{{method:'POST'}});
  const d=await r.json();o.textContent=render(d);}}
 catch(e){{o.textContent='Error: '+e;}}
 b.disabled=false;b.textContent='↻ Update all connected tools';
}}
function render(d){{
 let out=(d.dry_run?'DRY-RUN (nothing changed)':'EXECUTED')+'\\n\\n';
 for(const s of d.steps){{
  out+=`${{s.tool_id.padEnd(14)}} ${{s.action.padEnd(20)}} ${{s.reason}}\\n`;
  for(const c of (s.commands||[]))out+='    $ '+c.join(' ')+'\\n';
 }}
 return out;
}}
</script></body></html>"""


def _status_row(s: ToolStatus) -> str:
    if s.installed:
        pill = '<span class="pill ok">Installed</span>'
    elif s.manual_review:
        pill = '<span class="pill lab">Controlled-lab</span>'
    else:
        pill = '<span class="pill no">Not installed</span>'
    auto = "yes" if (s.auto_update and not s.manual_review) else "manual"
    return (
        f"<tr><td><b>{s.name}</b><br><code>{s.binary}</code></td>"
        f"<td>{_cat(s)}</td><td>{_risk(s)}</td><td>{pill}</td>"
        f"<td><code>{s.version or '—'}</code></td><td>{auto}</td></tr>"
    )


def _cat(s: ToolStatus) -> str:
    return _CTX.get(s.tool_id, ("", ""))[0]


def _risk(s: ToolStatus) -> str:
    return _CTX.get(s.tool_id, ("", ""))[1]


#: tool_id -> (category, risk) for rendering (filled by make_handler).
_CTX: dict[str, tuple[str, str]] = {}


def make_handler(
    manager: ToolManager, catalog: ToolCatalog, *, allow_execute: bool
) -> type[BaseHTTPRequestHandler]:
    """Build a request handler bound to a specific manager/catalog."""
    _CTX.clear()
    for e in catalog.all():
        _CTX[e.tool_id] = (e.category, e.risk.name)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args: Any) -> None:  # quiet by default
            pass

        def _send(self, code: int, body: str, ctype: str) -> None:
            data = body.encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self) -> None:  # noqa: N802 - http.server API
            if self.path in ("/", "/index.html"):
                statuses = manager.status()
                rows = "".join(_status_row(s) for s in statuses)
                net = "ENABLED" if manager.policy.network_enabled else "DISABLED"
                mode = "preview mode" if not allow_execute else "LIVE mode"
                self._send(
                    200,
                    _PAGE.format(
                        version=__version__, rows=rows, net=net, mode=mode
                    ),
                    "text/html; charset=utf-8",
                )
            elif self.path == "/api/status":
                payload = [asdict(s) for s in manager.status()]
                self._send(200, json.dumps(payload), "application/json")
            else:
                self._send(404, '{"error":"not found"}', "application/json")

        def do_POST(self) -> None:  # noqa: N802 - http.server API
            if self.path != "/api/sync":
                self._send(404, '{"error":"not found"}', "application/json")
                return
            plan: SyncPlan = manager.sync(dry_run=not allow_execute)
            self._send(200, json.dumps(_plan_json(plan)), "application/json")

    return Handler


def _plan_json(plan: SyncPlan) -> dict[str, Any]:
    return {
        "dry_run": plan.dry_run,
        "steps": [
            {
                "tool_id": s.tool_id,
                "action": s.action,
                "commands": s.commands,
                "reason": s.reason,
                "executed": s.executed,
                "ok": s.ok,
            }
            for s in plan.steps
        ],
    }


def serve(
    host: str = "127.0.0.1",
    port: int = 8765,
    *,
    allow_execute: bool = False,
    catalog: ToolCatalog | None = None,
    policy: PolicyEngine | None = None,
) -> None:  # pragma: no cover - blocking server loop
    """Start the local Web UI (blocking). Ctrl-C to stop."""
    from harness.core.policy import Scope

    cat = catalog or load_catalog()
    pol = policy or PolicyEngine(Scope())
    manager = ToolManager(cat, pol)
    handler = make_handler(manager, cat, allow_execute=allow_execute)
    httpd = ThreadingHTTPServer((host, port), handler)
    print(f"Harness Tool Center → http://{host}:{port}  (Ctrl-C to stop)")
    print(f"  mode: {'LIVE updates' if allow_execute else 'preview / dry-run'}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopping…")
    finally:
        httpd.server_close()

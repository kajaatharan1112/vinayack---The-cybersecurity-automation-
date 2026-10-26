# Tool Center — catalog, Web UI, and one-click tool sync

This document covers the tool-integration layer added in Session 6: a structured
**tool catalog** built from the owner's study notes plus curated open-source
extras, a **local Web UI**, and a **one-click / scripted updater**.

> **Safety first.** This layer only answers *"what tools exist, are they
> installed, and how do we keep them current"*. It never runs a security tool
> against a target — that stays behind the Policy Engine and (later) the Job
> Engine. Offensive / lab-only tools are **never** auto-cloned or auto-updated.

## What's included

| Piece | Path |
|---|---|
| Tool catalog (data) | `resources/tools/catalog.json` |
| Catalog loader + registry projection | `harness/tools/catalog.py` |
| Probe + policy-gated sync | `harness/tools/manager.py` |
| Local Web UI (stdlib, localhost) | `harness/interfaces/webui.py` |
| Auto-update script (one-click backend) | `scripts/update_tools.py` (+ `.sh`) |

The catalog carries **all 22 tools from `notes/01_Kali_Tools`** plus extras
(SSLyze, testssl.sh, Nuclei, Trivy, Gitleaks, WHOIS). Each entry records its
risk class, official upstream source, licence, update method, and whether it is
`auto_update` / `manual_review`.

## How "connect many tools + clone + auto-update" is handled safely

- **Catalog = the connection layer.** Adding a tool is a JSON edit; the registry,
  CLI, Web UI, and updater all pick it up with no code change.
- **Clone** → git-based upstreams clone into a **gitignored `vendor/`** dir (never
  committed into this repo), and only for safe, non-offensive tools.
- **Auto-update** → `scripts/update_tools.py` builds a plan and runs it. It is
  **dry-run by default**, needs `--network` for network tools (mirrors enabling
  network mode in the app), and skips every `manual_review` tool.
- **One button** → the Web UI's **"Update all connected tools"** button POSTs to
  `/api/sync`, which calls the same manager. In preview mode it shows the exact
  commands; with `--allow-execute` it runs them. Every sync is audit-logged.

## Usage

```bash
# Terminal
python -m harness.interfaces.cli catalog          # list all tools + install status
python -m harness.interfaces.cli sync --network   # preview the update plan
python -m harness.interfaces.cli webui --network  # open the local Web UI

# Script (what the button / cron calls)
python scripts/update_tools.py                    # preview everything (safe)
python scripts/update_tools.py --network --execute   # actually update safe tools
python scripts/update_tools.py --only nmap tshark --network
```

The Web UI binds to `127.0.0.1:8765` by default, ships no external assets, and
runs in **preview mode** unless started with `--execute`.

## Status labels (honest, never faked)

- **Installed** — binary found on `PATH` (version shown when the tool prints one).
- **Not installed** — safe tool, not present; eligible for sync.
- **Controlled-lab** — offensive / `manual_review` tool; install & update by hand.

## Not done yet (next)

- Real per-tool **adapters** (argv builders + output parsers) behind the Job Engine.
- Wire sync results into the audit/SQLite store once persistence lands.
- Visual selector picker + the Web Scraping Studio (separate module).

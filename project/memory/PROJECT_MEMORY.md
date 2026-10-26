# PROJECT MEMORY — Cybersecurity Harness Engine

> **This is the project's long-term brain.** It is the curated, always-current
> summary of the project: what it is, where it stands, and what matters right now.
> Read this file first at the start of every session. Keep it short and true —
> when something here goes stale, **update it** (don't just append). Full history
> lives in `logs/` (daily) and `DECISION_LOG.md` (decisions); this file is the
> distilled state, not the archive.

**Last updated:** 2026-10-26

---

## 1. What this project is (one paragraph)

A **Government-Ready Offline Cybersecurity Harness Engine** — a local-first,
offline-first, AI-assisted platform that orchestrates many cybersecurity tools
from one place. An authorized operator states a testing objective in natural
language; the harness plans a workflow, checks it against a policy engine, gets
operator approval, runs approved tools within a defined scope, and reports
results. Primary research focus: **IP intelligence / network analysis**. Built
heavily in **ARM64 + x86-64 Assembly** (hybrid with Rust/Go/C++ and a TS UI),
with a **DeepSeek-based local AI** harness and a **custom MCP server**. Sold via
per-customer enterprise/government licensing. Full detail:
[`../PROJECT_MASTER_PLAN.md`](../PROJECT_MASTER_PLAN.md).

## 2. Current status

- **Phase:** Planning & Research (Phase 0). No product code written yet.
- **Repo today:** cybersecurity study `notes/` (322 md files) + this `project/`
  planning space. No harness implementation exists.
- **Goal of the moment:** we are still **planning** — not yet building the engine.

## 3. Hard rules that must never drift (the project's non-negotiables)

1. **Authorized use only** — every capability is gated behind scope + policy +
   operator approval. This is defensive/research tooling for the customer's own
   or explicitly permitted systems.
2. **Offline-first** — must function with no internet; network access only when
   explicitly enabled by the operator.
3. **Local-first** — no mandatory public cloud. Everything runs on the customer's
   machine/infrastructure.
4. **Policy engine is authoritative** — the AI model can never grant itself
   permissions or bypass authorization.
5. **Transparency + audit** — every significant action is observable and logged.
6. **Emergency stop** — the operator can always kill tasks and revoke network
   access instantly.
7. **`notes/` is the user's university notes — do not restructure or disturb
   them for project work.** Project artifacts live under `project/`.

## 4. Key decisions already made

See [`DECISION_LOG.md`](DECISION_LOG.md) for the full list with dates/reasons.
Highlights:
- Deployment = local-first / offline-first (not cloud). *(D-0001)*
- Two assembly targets: ARM64 + x86-64, hybrid with higher-level languages.
- AI foundation = DeepSeek-compatible, multi-model adapter, local inference.
- Initial DB = SQLite; custom MCP server bound to localhost.
- Business model = per-customer licensing.

## 5. Open questions / not yet decided

- Primary OS for initial development (Windows x86-64 vs Linux x86-64).
- Orchestration language choice (Rust vs Go vs C/C++).
- Which DeepSeek-compatible local runtime to use.
- Exact tool plugin contract / interface schema.
- MVP tool: start with IP intelligence module (decided direction) — scope of v0.

## 6. Where things live

| What | Path |
|---|---|
| Master plan (full spec) | `project/PROJECT_MASTER_PLAN.md` |
| This memory (project brain) | `project/memory/PROJECT_MEMORY.md` |
| Decision log | `project/memory/DECISION_LOG.md` |
| Daily work logs | `project/memory/logs/YYYY-MM-DD.md` |
| How to use/update memory | `CLAUDE.md` (repo root) |
| Study notes (do not disturb) | `notes/` |

## 7. Next engineering priorities (from the plan, §31)

1. Finalize component architecture → 2. Pick primary OS → 3. Evaluate DeepSeek
local runtime → 4. Pick orchestration language → 5. Set up ASM dev environments →
6. Define tool plugin contract → 7. Define authorization/policy system →
8. Offline harness lifecycle → 9. First IP intelligence engine → 10. Initial MCP
server → 11. Terminal UI → 12. First desktop dashboard.

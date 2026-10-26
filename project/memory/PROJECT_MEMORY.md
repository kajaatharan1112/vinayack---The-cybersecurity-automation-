# PROJECT MEMORY — Cybersecurity Harness Engine

> **This is the project's long-term brain.** It is the curated, always-current
> summary of the project: what it is, where it stands, and what matters right now.
> Read this file first at the start of every session. Keep it short and true —
> when something here goes stale, **update it** (don't just append). Full history
> lives in `logs/` (daily) and `DECISION_LOG.md` (decisions); this file is the
> distilled state, not the archive.

**Last updated:** 2026-10-26 (Session 6)

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

- **Phase:** Phase 0 — Foundation **in progress** (moved past pure planning).
- **Repo today:** study `notes/`, `project/` planning space, **and a runnable
  harness** (`harness/`) with a full test suite, Docker, and GitHub Actions CI.
- **What works now:** offline-first harness lifecycle, the **authoritative Policy
  Engine** (scope/risk/approval/network/emergency-stop), append-only audit log,
  tool registry, AI model-adapter interface + offline stub + a **working DeepSeek
  local-runtime adapter** (OpenAI-compatible endpoint via stdlib urllib; offline
  fallback; model output treated as untrusted), and a terminal CLI.
  Verified: ruff clean, mypy clean, **50 pytest tests pass**.
- **Architecture:** finalized in `project/architecture/COMPONENT_ARCHITECTURE.md`.
- **Automation:** CI runs ruff + mypy + pytest on **every push** (py3.11/3.12);
  Docker build + offline smoke test gates **main**.

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
- **Phase-0 harness MVP in Python, core stdlib-only (offline/hermetic).** *(D-0010)*
- **Testing mandatory (pytest); every module has tests.** *(D-0011)*
- **Docker + docker-compose; multi-stage, non-root runtime.** *(D-0012)*
- **CI = GitHub Actions on every push; Docker build gates main.** *(D-0013)*
- **DeepSeek = local OpenAI-compatible runtime adapter (not vendored).** *(D-0014)*
- **Model output untrusted; defensive parsing, fail-closed risk.** *(D-0015)*

## 5. Open questions / not yet decided

- Primary OS for initial development (Windows x86-64 vs Linux x86-64).
- Orchestration language for the *performance core* (Rust vs Go vs C/C++) — note
  the Phase-0 *harness* layer is Python by D-0010; this is about the native core.
- Exact tool plugin contract / interface schema.
- MVP tool: start with IP intelligence module (decided direction) — scope of v0.
- Which specific DeepSeek model to standardize on (deepseek-r1 vs deepseek-coder)
  and licence verification before any commercial distribution.

## 6. Where things live

| What | Path |
|---|---|
| Master plan (full spec) | `project/PROJECT_MASTER_PLAN.md` |
| Component architecture (finalized) | `project/architecture/COMPONENT_ARCHITECTURE.md` |
| This memory (project brain) | `project/memory/PROJECT_MEMORY.md` |
| Decision log | `project/memory/DECISION_LOG.md` |
| Daily work logs | `project/memory/logs/YYYY-MM-DD.md` |
| How to use/update memory | `CLAUDE.md` (repo root) |
| Harness code | `harness/` · tests in `tests/` · CI in `.github/workflows/` |
| Study notes (do not disturb) | `notes/` |

## 7. Next engineering priorities

**Done:** ✅ component architecture finalized · ✅ offline harness lifecycle · ✅
authorization/policy system · ✅ tool registry skeleton · ✅ terminal UI (basic) ·
✅ Docker + CI + tests environment · ✅ **DeepSeek local-runtime adapter (working,
offline-first, untrusted-output safe)**.

**Next:**
1. SQLite persistence for audit log + projects + scope (currently in-memory).
2. First **IP intelligence engine** (the MVP research module).
3. **Tool plugin contract** — formal input/output schema + execution adapter.
4. Sandboxed **execution runtime** (process/container isolation).
5. **MCP server** (localhost, authenticated).
6. Rust/Assembly native engine interface + first ARM64/x86-64 module.
7. Pick primary OS + set up ASM dev environments.

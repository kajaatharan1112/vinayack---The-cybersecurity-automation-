# Session Starter Prompt — Cybersecurity Harness Engine

> **எதற்கு:** புது Claude session ஆரம்பிக்கும் போது, கீழே உள்ள prompt-ஐ copy
> பண்ணி முதல் message-ஆ paste பண்ணுங்க. Claude-க்கு project full context உடனே
> கிடைக்கும்.
>
> **எப்படி use பண்றது:** கீழே `---` lines-க்கு இடையில உள்ளதை எல்லாம் copy பண்ணுங்க →
> கடைசி line-la இன்னிக்கு என்ன பண்ணனும்னு எழுதுங்க → paste பண்ணுங்க.

---

You are working on the **Government-Ready Offline Cybersecurity Harness Engine** —
an authorized, defensive cybersecurity research and testing platform. Read this
context fully before doing anything.

### PROJECT OVERVIEW
- **Product:** A local-first, offline-first, AI-assisted "harness" that
  orchestrates many cybersecurity tools from one place. An authorized operator
  states a testing objective in natural language; the harness plans a workflow,
  checks it against a policy engine, gets operator approval, runs approved tools
  within a defined scope, and reports results.
- **Primary research focus:** IP intelligence / network analysis.
- **Deployment:** Local-first + offline-first. NOT a cloud service.
- **Business model:** Per-customer enterprise/government licensing.
- **Status:** Phase 0 — Planning & Research. No product code written yet.

### NON-NEGOTIABLE RULES (never let these drift)
1. **Authorized use only** — every capability is gated behind scope + policy +
   operator approval. This is defensive/research tooling for the customer's own
   or explicitly permitted systems.
2. **Offline-first** — must work with no internet; network access only when the
   operator explicitly enables it.
3. **Local-first** — no mandatory public cloud.
4. **Policy engine is authoritative** — the AI can never grant itself permissions
   or bypass authorization.
5. **Transparency + audit** — every significant action is observable and logged.
6. **Emergency stop** — operator can always kill tasks and revoke network access.
7. **`notes/` is the owner's university study notes — DO NOT restructure or
   disturb them.** All project work goes under `project/`.

### TECH DIRECTION (decided)
- **Assembly:** ARM64 (AArch64) + x86-64 (AMD64/Intel 64), hybrid with
  Rust/Go/C/C++ for orchestration and TypeScript for the UI.
- **AI:** DeepSeek-compatible, multi-model adapter, local inference (offline).
- **Integration:** custom MCP server bound to localhost (Claude Code / Codex /
  Cursor).
- **Database:** SQLite for the first implementation.
- **Interfaces:** Terminal UI + Desktop graphical UI.
- Full detail: `project/PROJECT_MASTER_PLAN.md` (v1.0, 31 sections).

### PROJECT MEMORY — READ AND MAINTAIN IT (very important)
This project keeps a persistent memory. Follow `CLAUDE.md` at the repo root.
- **At session START:**
  1. Read `project/memory/PROJECT_MEMORY.md` (the project brain — current state).
  2. Skim the latest file in `project/memory/logs/`.
  3. Check `project/memory/DECISION_LOG.md` if a decision's context is needed.
- **At session END (required):**
  1. Append today's work + results to `project/memory/logs/YYYY-MM-DD.md`
     (create it if missing).
  2. Add any new decision to `DECISION_LOG.md` as a new `D-xxxx` entry (never
     rewrite old ones; supersede instead).
  3. Curate `PROJECT_MEMORY.md` so it stays the truth of *now* (don't just
     append — move old detail down into logs).

### REPOSITORY LAYOUT
```
CLAUDE.md                         rules for every session
project/
├── PROJECT_MASTER_PLAN.md        full master plan
├── SESSION_STARTER_PROMPT.md     this prompt
└── memory/
    ├── PROJECT_MEMORY.md         project brain (read first)
    ├── DECISION_LOG.md           decisions D-xxxx
    └── logs/YYYY-MM-DD.md        date-wise work logs
notes/                            university study notes (do NOT disturb)
```

### GIT
Develop on the session's assigned branch, commit with clear messages, push when
done. (Pushing needs the Claude GitHub App installed on this repo; if a push
returns 403, tell me to reconnect GitHub.)

### TODAY'S TASK
[REPLACE THIS LINE with what you want to do today]

---

## Examples of session tasks

- "Phase 0: finalize the component architecture and write it into the master plan."
- "Decide the primary OS for initial development and log the decision."
- "Evaluate DeepSeek-compatible local inference runtimes and summarize options."
- "Define the tool plugin contract (interface schema) and save it under project/."
- "Design the first IP intelligence engine — data model + workflow."
- "Draft the local MCP server tool interface and its security controls."
- "Set up the ARM64 + x86-64 assembly dev environment plan."

## Maintenance

Update this prompt when: major decisions change, a new phase starts, the tech
stack changes, or the repository layout changes.

_Last updated: 2026-10-26_

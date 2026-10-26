# CLAUDE.md — How to work in this repository

This repo has two separate parts. Keep them separate.

| Part | What it is | Rule |
|---|---|---|
| `notes/` | The owner's university cybersecurity study notes (322 md files). | **Reference only. Do not restructure, rename, or disturb** for project work. |
| `project/` | The "Cybersecurity Harness Engine" project — plan, memory, logs, and (later) code. | All project work goes here. |

---

## Project memory — read and maintain it

The project has a persistent memory under `project/memory/`. It is the AI's job
to keep it current.

**At the START of every session:**
1. Read `project/memory/PROJECT_MEMORY.md` (the project brain — current state).
2. Skim the latest file in `project/memory/logs/` (what happened recently).
3. Check `project/memory/DECISION_LOG.md` if a decision's context is needed.

**DURING / END of every session (this is required, not optional):**
1. **Daily log** — append to `project/memory/logs/YYYY-MM-DD.md` (today's date;
   create the file if it doesn't exist). Record: what the session worked on, the
   **results**, and anything left pending. Add an entry *when work starts* and
   update it with outcomes.
2. **Decisions** — if a real decision was made (architecture/product/process),
   add a new `D-xxxx` entry to `DECISION_LOG.md`. Never rewrite old entries; if a
   decision changes, add a new one that supersedes the old (mark the old one
   `Superseded by Dxxxx`).
3. **Project brain** — update `PROJECT_MEMORY.md` so it stays true: change status,
   open questions, and next priorities. **Curate, don't just append** — this file
   is the distilled current state, and the `logs/` hold the full history.

## What to keep vs. omit when analyzing memory

When reading memory to decide what matters now:
- **Keep / prioritize:** `PROJECT_MEMORY.md` (always), the hard rules (its §3),
  active decisions in `DECISION_LOG.md`, open questions, next priorities, and the
  **most recent** daily logs.
- **Can omit / skim:** old daily logs once their outcome is already reflected in
  `PROJECT_MEMORY.md` or the decision log; superseded decisions (history only);
  routine notes with no lasting effect.
- Rule of thumb: if it changes what we do next, it belongs in `PROJECT_MEMORY.md`.
  If it's "what happened on a day", it stays in `logs/`.

As memory grows, trim `PROJECT_MEMORY.md` back to the truth of *now*; let `logs/`
be the archive. Don't delete logs or decisions — move detail down, keep the brain
short.

## Project non-negotiables (never let these drift)

Authorized use only · offline-first · local-first · the policy engine is
authoritative over the AI · transparency + audit · always-available emergency
stop. Full detail: `project/PROJECT_MASTER_PLAN.md`.

## Git

Develop on the branch assigned for the session; commit with clear messages; push
when work is complete. (Note: pushing needs the Claude GitHub App installed on
this repo — if a push returns 403, tell the user to reconnect GitHub.)

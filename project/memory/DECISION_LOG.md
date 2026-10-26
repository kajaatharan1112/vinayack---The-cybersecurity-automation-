# DECISION LOG

> Permanent record of **decisions** — architectural, product, or process. One row
> per decision. Never rewrite history here: if a decision is reversed, add a new
> entry that supersedes the old one and mark the old one `Superseded`.
>
> Format per entry: ID · date · decision · why · status (Active / Superseded by Dxxxx).

---

### D-0001 · 2026-10-26 · Local-first / offline-first, not cloud
**Decision:** The product runs on the customer's local machine/private
infrastructure. No mandatory public cloud deployment.
**Why:** Government/enterprise/air-gapped requirements; customer data ownership.
**Status:** Active.

### D-0002 · 2026-10-26 · Two assembly targets (ARM64 + x86-64), hybrid stack
**Decision:** Low-level engines in ARM64 and x86-64 Assembly; orchestration in
Rust/Go/C/C++; UI in TypeScript. Not everything in assembly.
**Why:** Performance for low-level work; portability and maintainability for the
rest.
**Status:** Active.

### D-0003 · 2026-10-26 · DeepSeek-compatible, multi-model, local inference
**Decision:** AI harness built around DeepSeek-compatible models via a model-
adapter layer; must run locally/offline. Licensing to be verified before
commercial distribution.
**Why:** Offline operation + flexibility to swap models.
**Status:** Active.

### D-0004 · 2026-10-26 · Policy engine is authoritative over the AI
**Decision:** Authorization is enforced outside the language model; the AI cannot
grant itself permissions.
**Why:** Safety — AI must not be able to execute tools outside approved scope.
**Status:** Active.

### D-0005 · 2026-10-26 · Custom MCP server, localhost by default
**Decision:** Build a custom MCP server exposing approved capabilities to Claude
Code / Codex / Cursor; binds to localhost with auth + permission validation.
**Why:** Controlled AI-tool integration without opening network exposure.
**Status:** Active.

### D-0006 · 2026-10-26 · Initial database = SQLite
**Decision:** First implementation uses a local SQLite database; larger systems
only when justified.
**Why:** Simple, local, offline-friendly.
**Status:** Active.

### D-0007 · 2026-10-26 · Business model = per-customer licensing
**Decision:** Primary revenue is per-customer enterprise/government licensing, not
a cloud subscription.
**Why:** Matches local-first deployment and target customers.
**Status:** Active.

### D-0008 · 2026-10-26 · MVP centers on the IP intelligence module
**Decision:** First functional research workflow is authorized IP intelligence /
network analysis.
**Why:** It is the stated primary research focus and a self-contained first
deliverable.
**Status:** Active.

### D-0009 · 2026-10-26 · `notes/` stays untouched; project work lives in `project/`
**Decision:** The university study notes are kept as-is; all planning/engineering
artifacts go under `project/`.
**Why:** User requirement — do not disturb the notes.
**Status:** Active.

### D-0010 · 2026-10-26 · Phase-0 harness/orchestration MVP in Python (stdlib-only core)
**Decision:** Build the Phase-0 harness + orchestration layer in Python 3.11+.
Core modules (policy, audit, lifecycle, registry) use the standard library only,
so the system and its tests run fully offline with no third-party runtime deps.
**Why:** Fastest path to a working, CI-gated, testable foundation; hermetic
offline tests match the offline-first requirement. Rust/Assembly stay reserved
for performance-critical and low-level engines (later phases), plugged in behind
the registry's stable adapter interface.
**Status:** Active.

### D-0011 · 2026-10-26 · Testing is mandatory; pytest is the framework
**Decision:** Every module ships with tests under `tests/`. No module merges
without a test. pytest + coverage.
**Why:** User requirement — "ella work ikkum test case mukiyam". Government
project needs a verifiable safety core.
**Status:** Active.

### D-0012 · 2026-10-26 · Containerized with Docker + docker-compose
**Decision:** Multi-stage Dockerfile (test stage + slim non-root runtime stage);
docker-compose runs the harness offline (`network_mode: none`) and the test suite.
**Why:** Reproducible, isolated, flexible environment; least privilege.
**Status:** Active.

### D-0013 · 2026-10-26 · CI/CD via GitHub Actions; main is the release gate
**Decision:** `.github/workflows/ci.yml` runs ruff + mypy + pytest on every push
(py3.11 & 3.12) and on PRs to main; a Docker build + offline smoke-test job gates
the main line. Concurrency cancels superseded runs.
**Why:** User requirement — "Testing automation romba mukiyam ... push panum
pothum main ikku pipeline run akanum".
**Status:** Active.

### D-0014 · 2026-10-26 · DeepSeek integration = local OpenAI-compatible runtime adapter
**Decision:** Integrate DeepSeek through a local-runtime adapter
(`harness/ai/deepseek_adapter.py`) that calls an OpenAI-style
`/chat/completions` endpoint served locally (Ollama / llama.cpp / LM Studio),
using a stdlib-only `urllib` transport. We do NOT vendor a DeepSeek repo; the
model runs in the operator's own local runtime.
**Why:** Keeps the harness dependency-free and offline-first; lets the operator
pick/swap any local DeepSeek-compatible model without changing the harness.
**Status:** Active. (Resolves the open question in PROJECT_MEMORY §5.)

### D-0015 · 2026-10-26 · Model output is untrusted; parsing fails closed
**Decision:** The model only proposes; its JSON is parsed defensively and still
passes through the Policy Engine. Unknown/garbled risk levels fail CLOSED
(escalated to INTRUSIVE, requiring approval); malformed output raises
`DeepSeekError` rather than executing.
**Why:** A model (or prompt injection) must never be able to widen scope or run
an unapproved operation. Authority stays in the Policy Engine.
**Status:** Active.

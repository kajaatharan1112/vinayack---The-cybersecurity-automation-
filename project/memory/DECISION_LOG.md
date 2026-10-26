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

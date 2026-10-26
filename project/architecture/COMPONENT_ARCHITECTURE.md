# Component Architecture (Finalized — Phase 0)

**Status:** Baseline finalized 2026-10-26 · supersedes the high-level sketch in
`PROJECT_MASTER_PLAN.md` §7 with concrete components, boundaries, and the data
flow of a single request.

> **Golden rule of this architecture:** the **Policy Engine** sits between *every*
> request and *every* tool execution. The AI never calls a tool directly. Nothing
> touches the network or a high-risk tool without a Policy Engine `ALLOW`.

---

## 1. Layered component map

```
┌──────────────────────────────────────────────────────────────────────┐
│ L1  INTERFACES        Terminal UI  ·  Desktop UI  ·  MCP Server        │
│                       (all are thin clients → they call L2/L3 only)    │
└───────────────┬────────────────────────────────────────────────────────┘
                │ structured requests (never raw tool commands)
┌───────────────▼────────────────────────────────────────────────────────┐
│ L2  AI HARNESS        ModelAdapter(s)  ·  Planner  ·  ResultAnalyzer    │
│                       Produces a PROPOSED workflow. Has NO authority.   │
└───────────────┬────────────────────────────────────────────────────────┘
                │ proposed workflow
┌───────────────▼────────────────────────────────────────────────────────┐
│ L3  POLICY ENGINE ★   Scope validation · permission check · rate/time   │
│   (AUTHORITATIVE)     limits · approval gate · EMERGENCY STOP kill-switch│
│                       → returns ALLOW / DENY + reasons for each step     │
└───────────────┬────────────────────────────────────────────────────────┘
                │ only ALLOW-ed steps pass
┌───────────────▼────────────────────────────────────────────────────────┐
│ L4  ORCHESTRATION     Scheduler · Tool Selector · Execution Manager ·   │
│                       Process Supervisor · Result Collector             │
└───────────────┬────────────────────────────────────────────────────────┘
                │ load only what the workflow needs
┌───────────────▼────────────────────────────────────────────────────────┐
│ L5  TOOL REGISTRY     Tool metadata · risk class · required perms ·     │
│                       arch/OS support · input/output schema · versions  │
└───────────────┬────────────────────────────────────────────────────────┘
                │ architecture-specific adapters
┌───────────────▼────────────────────────────────────────────────────────┐
│ L6  EXECUTION RUNTIME Local process · container · VM · sandbox ·         │
│                       ARM64 / x86-64 native engine adapters             │
└───────────────┬────────────────────────────────────────────────────────┘
                │ every action emits an audit event
┌───────────────▼────────────────────────────────────────────────────────┐
│ L7  STORAGE + AUDIT   SQLite (projects, scope, tools, findings, audit)  │
│                       Append-only audit log · evidence store · reports  │
└──────────────────────────────────────────────────────────────────────────┘
```

★ = the single point of authority. See §4.

---

## 2. Phase-0 implementation stack (decided)

| Concern | Choice | Why |
|---|---|---|
| Harness / orchestration MVP | **Python 3.11+** | Fastest path to a working, testable, CI-gated foundation; rich stdlib; great test story. |
| Core modules (policy, audit, lifecycle, registry) | **Python stdlib only** | Zero runtime deps ⇒ tests run fully **offline**, anywhere, no network. Matches offline-first. |
| Performance-critical / low-level engines | **Rust + ARM64/x86-64 Assembly** (later phases) | Reserved for packet parsing, crypto primitives, native engines — added behind the stable engine interface. |
| Interfaces | Terminal (Python now) → Desktop (TypeScript later) | Terminal UI first for the MVP; desktop in Phase 6. |
| Database | **SQLite** | Local, offline, zero-config. |
| Packaging | **Docker + docker-compose** | Reproducible, isolated, flexible dev + run environment. |
| CI / test automation | **GitHub Actions + pytest + ruff + mypy** | Every push runs lint + types + tests; `main` runs the full pipeline incl. Docker build. |

> Python is the *harness* language, not the whole product. Low-level engines stay
> in Rust/Assembly and plug in through `harness/registry` adapters, so the stack
> stays flexible.

---

## 3. The modules we build in Phase 0 (this repo, `harness/`)

| Module | Responsibility | Authority |
|---|---|---|
| `harness/core/config.py` | Load config; default to OFFLINE, network DISABLED. | — |
| `harness/core/policy.py` ★ | **The authoritative gate.** Validate scope, permissions, rate/time limits, approvals; honor emergency stop. | **Authoritative** |
| `harness/core/audit.py` | Append-only structured audit log of every significant action. | — |
| `harness/core/lifecycle.py` | Offline-first startup sequence; mode transitions (OFFLINE ⇄ NETWORK); emergency stop. | enforces via policy |
| `harness/ai/base.py` | `ModelAdapter` interface (plan / analyze / report). | **None** (proposes only) |
| `harness/ai/deepseek_adapter.py` | DeepSeek harness adapter — **the scaffold we modify later** to talk to a local DeepSeek runtime. | None |
| `harness/ai/local_stub.py` | Deterministic offline stub adapter so the system + tests run with no model/network. | None |
| `harness/registry/tool_registry.py` | Register tools with metadata + risk class; load only what a workflow needs. | — |
| `harness/interfaces/cli.py` | Terminal UI: status banner + commands. | thin client |

Each module has a matching test in `tests/`. **No module merges without a test.**

---

## 4. Policy Engine — the heart (why it is separate and authoritative)

The AI model (L2) only ever produces a **proposed** workflow. It cannot execute
anything. Every proposed step is passed to the Policy Engine (L3), which returns
an `ALLOW`/`DENY` **per step** with reasons. The Orchestrator (L4) executes
**only** `ALLOW`-ed steps.

A request is `ALLOW`-ed only if **all** hold:
1. **Emergency stop is not engaged** (kill-switch → everything `DENY`).
2. The **target is in the project's authorized scope** (IP/CIDR/domain).
3. The **tool is approved** for this project and its **risk class** is permitted.
4. The **operation category** is permitted.
5. **Network operations** require network mode to be explicitly enabled.
6. **Rate / duration / resource limits** are satisfied.
7. **Required approval level** exists for high-risk operations.

This guarantees the project's non-negotiables: *authorized use only, offline-first,
policy authoritative over the AI, emergency stop.* Prompt-injection or a
misbehaving model cannot widen scope, because authority lives outside the model.

---

## 5. Request data flow (one IP-intelligence request)

```
Operator (CLI/Desktop/MCP)
  │  "Analyze exposed services on the authorized lab subnet"
  ▼
ModelAdapter.plan()  ──►  proposed workflow: [discover_hosts, scan_services]
  ▼
PolicyEngine.evaluate(workflow, project.scope)
  │  per-step ALLOW/DENY (+ reasons)   ◄── emergency-stop & network-mode checked here
  ▼
Orchestrator  ──► loads only the needed tools from the Registry
  ▼
Execution Runtime (sandboxed / arch-specific adapter) ──► results
  │  every step → AuditLog.append(...)
  ▼
ModelAdapter.analyze(results) ──► findings
  ▼
Report  +  stored in SQLite  +  shown in the interface
```

---

## 6. Non-negotiables → where each is enforced

| Non-negotiable | Enforced by |
|---|---|
| Authorized use only | `policy.py` scope + approval checks (§4) |
| Offline-first | `lifecycle.py` starts OFFLINE; `config.py` network DISABLED by default |
| Local-first | SQLite + local process runtime; no cloud dependency |
| Policy authoritative over AI | AI in L2 proposes only; L3 decides; separated by design (§4) |
| Transparency + audit | `audit.py` append-only log on every action |
| Emergency stop | `policy.py` kill-switch + `lifecycle.emergency_stop()` |

---

## 7. What is intentionally deferred (not Phase 0)

Rust/Assembly native engines, container/VM sandboxing runtime, the real DeepSeek
model integration, the MCP server, the desktop UI, and the broader tool catalog.
Phase 0 delivers the **skeleton + the authoritative policy core + CI/Docker/test
environment** so everything after plugs into a solid, automatically-verified base.

_Last updated: 2026-10-26_

# DeepSeek Local-Runtime Integration

**Status:** implemented (Phase 0) · module `harness/ai/deepseek_adapter.py` +
`harness/ai/transport.py` · supersedes the earlier "scaffold / NotImplemented"
version.

---

## What it does

`DeepSeekAdapter` turns an operator's objective into a *proposed* workflow by
calling a **local** DeepSeek-compatible model over an OpenAI-style
`/chat/completions` endpoint. It uses only the Python standard library
(`urllib`), so the harness keeps zero third-party runtime dependencies.

```
objective ──► DeepSeekAdapter.plan() ──► local model (localhost) ──► JSON plan
                        │
                        └─► parsed defensively into a Workflow of OperationRequests
                                    │
                                    └─► Policy Engine gates every step (untrusted!)
```

## Supported local runtimes (any OpenAI-compatible endpoint)

| Runtime | Example endpoint | Example model |
|---|---|---|
| Ollama | `http://localhost:11434/v1` | `deepseek-r1`, `deepseek-coder` |
| llama.cpp server | `http://localhost:8080/v1` | a local DeepSeek GGUF |
| LM Studio | `http://localhost:1234/v1` | a local DeepSeek model |

## How to enable it

```python
from harness.ai.deepseek_adapter import DeepSeekAdapter, DeepSeekConfig

adapter = DeepSeekAdapter(DeepSeekConfig(
    model="deepseek-r1",
    endpoint="http://localhost:11434/v1",
    allow_network=True,          # must be explicit
))
workflow = adapter.plan("Discover exposed services on the authorized lab subnet")
```

- **Offline-first:** if `endpoint` is empty **or** `allow_network` is False, the
  adapter is "not ready" and silently falls back to the deterministic offline
  stub. The harness is always usable with no model.
- `is_ready` is True only when both an endpoint is set **and** `allow_network`
  is True.

## Safety guarantees (why a model can't do harm here)

1. **Model output is untrusted.** The returned JSON is parsed defensively;
   malformed JSON, missing `steps`, or a step without a string `tool`/`operation`
   raises `DeepSeekError` instead of executing anything.
2. **Fail-closed risk.** An unknown/garbled `risk` value is treated as
   `INTRUSIVE` (needs operator approval), never silently `PASSIVE`.
3. **Policy Engine is still authoritative.** A plan proposing an out-of-scope
   target or an unapproved tool is produced but **denied** at evaluation time —
   proven by `tests/test_deepseek_adapter.py::
   test_model_proposed_out_of_scope_target_is_denied_by_policy`.
4. **DeepSeek-R1 noise handled.** `<think>…</think>` reasoning blocks and
   markdown code fences are stripped before JSON parsing.

## Testing

Fully hermetic — a `FakeTransport` stands in for the runtime, and the
`HttpTransport` test monkeypatches `urllib.request.urlopen`. No network is
touched. See `tests/test_deepseek_adapter.py` and `tests/test_transport.py`.

## Not done yet (future)

Streaming responses, multi-model roles (planner/analyst/reporter), model health
checks + auto model discovery, and verifying the chosen DeepSeek model's licence
before any commercial distribution.

_Last updated: 2026-10-26_

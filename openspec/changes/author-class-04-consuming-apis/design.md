## Context

Classes 01–03 already use five ordered notebooks, a numbered VS Code workspace, a class-local uv lockfile, and separate prompt/attempt/commented-loader cells. Existing Observation has label and finite nonnegative value; Report and summarize should remain unchanged.

The user approved simplifying class 04, explaining frontend/backend roles, showing a supplied FastAPI service, and previewing both OpenAI and Ollama. Required AI application building remains class 05. Earlier interview recommendations for World Bank data, five notebooks, and failing the complete load on invalid records were also accepted.

## Goals / Non-Goals

### Goals

- Explain architecture through one small GET exchange.
- Require only request, status, JSON, validation, and useful failure handling.
- Reuse the same internal model for local and World Bank data.
- Demonstrate AI POST/body/header patterns without requiring credentials or a local model.
- Provide deterministic tests, saved recovery routes, and complete timed teaching material.

### Non-Goals

- Required backend construction, frontend coding, pagination/retry algorithms, async, OAuth, a provider abstraction, or AI orchestration.
- Automatically starting services, fetching data, reading secrets, or downloading models on notebook/reference execution.
- Claiming illustrative AI fixtures are live captures, or automated checks are desktop verification.

## Decisions

### Reading sequence and workload

1. 04.1 frontend/backend/HTTP and supplied FastAPI route: 30 class, 15 independent.
2. 04.2 four-step validated client: 30 class, 15 independent.
3. 04.3 failures and two short AI previews: 30 class, 15 independent.
4. 04.4 World Bank mapping and authentication concepts: 60 independent.
5. 04.5 failure tests and AI-envelope review: 75 independent.

Preparation adds 30 independent minutes, for 90/210 totals. The last classroom teaching block allocates ten minutes to failure diagnosis and ten to the two AI previews. Optional extensions fit a separate 180-minute ceiling.

### Minimal implementation

A supplied synchronous FastAPI route reads saved observations and supports one exact-label parameter. Students consume it; server extension is optional. Requests is the required client. get_json handles request/status/JSON failures, parse_observations validates the full list, and fetch_observations joins those boundaries. No custom client class, general replay protocol, or retry framework.

Keep Observation, Report, and summarize compatible with class 03. The World Bank adapter requests only Portugal/Spain population for 2023, maps ISO/year to label and persons to value, rejects missing values and multi-page envelopes, and returns the existing model. A real snapshot enables offline integration.

### AI demonstrations

Use raw Requests POSTs so students recognize the same transport. OpenAI uses the Responses endpoint with an environment-provided bearer key/model. Ollama uses local /api/generate with stream=false and an environment-provided installed model. Both default to explicitly illustrative saved envelopes, reading no environment variables until live=True. No model choice or CPU-performance claim is embedded. Dedicated SDK/application logic stays in week 5.

### Verification and evidence

Use controlled Requests responses for deterministic client tests; leave actual parsing/validation in place. Test the supplied route function directly. Verify real localhost sockets separately on a disposable port and the public API with a separate smoke test. Do not call live AI providers for authoring checks. Verify notebook/reference execution with outbound calls blocked, clean loaders, budgets, links, fresh-copy setup, and a seeded regression in a temporary copy. Record static/protocol checks separately from the pending VS Code desktop task.

## Risks / Trade-offs

- Introducing both client/server roles could expand scope: supply the server and require no route construction.
- Three external service names could distract: World Bank is one small independent integration; AI calls are short instructor previews.
- Saved responses could be mistaken for live evidence: label every path and fixture origin explicitly.
- Statistical revisions change live results: tests assert mapping and validity, not future exact values.
- API/SDK/model details can change: source links are checked during authoring and must be rechecked before teaching.

## Migration Plan

Add the class beside the earlier active distributions, revise only the approved week-04 curriculum scope, extend shared class-04 checks, and update execution records with actual evidence. Preserve earlier classes and all untracked legacy material. Commit/push only if separately requested.

## Open Questions

No implementation decisions remain from the interview. Desktop editor interaction, supported-platform checks, beginner timing trials, and live model demonstrations require separate delivery evidence.

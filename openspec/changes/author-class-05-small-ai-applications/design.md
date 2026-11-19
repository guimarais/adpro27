## Context

The accepted interview fixes the learning depth: explicitly introduce model/prompt/
context/token/SDK/tool/harness relationships and a glossary, while student code
completions remain individual expressions or lines. Earlier classes already provide
five ordered notebooks, class-local workspaces/environments, six exercise references,
and the Observation/summarize contract. The active class-04 snapshot has two countries
in 2023, with attribution retained locally.

## Goals / Non-Goals

### Goals

- Make model proposals versus Python permissions/execution clear.
- Supply the complete harness and make its behavior easy to inspect through traces.
- Validate arguments and final output, preserve call/result linkage, enforce limits.
- Distinguish repeatable application tests from model-behavior evaluation.
- Keep all required completion possible without credits, a key, a GPU, or a model download.

### Non-Goals

- Student implementation of dispatch, schemas, SDK plumbing, a loop, or a test suite.
- New tools/query languages, writes, arbitrary code, RAG, frameworks, multi-agent
  systems, provider hierarchies, async, deployment, or frontend development.
- Claiming an illustrative replay, mocked SDK transport, or static check establishes
  live-model quality, a recording, desktop interaction, or CPU model compatibility.

## Decisions

### Five parts and workload

Parts 05.1–05.3 each allocate 30 class and 15 independent minutes; 05.4 allocates
60 independent, 05.5 75 independent, and preparation 30 independent. This retains
the 90/210 budget. Independent categories are 30 setup/glossary, 60 guided
walkthrough/tiny completions, 60 supplied tests/saved failures, 45 five-prompt
evaluation, and 15 reflection. Every command/check is inside these categories.

### Supplied application and student responsibility

Offer `get_summary()` and `find_observations(label)` over the local class-04 World
Bank snapshot. Preserve exact label matching and empty-list absence. Population
values are persons for PRT:2023 and ESP:2023. Reuse only needed active-project code
and the snapshot, with provenance; no root legacy files are used.

`Answer` has one field, `answer: str`. Strict shape validation is deliberately
separate from factual accuracy. Two small argument schemas forbid extra fields;
the dispatcher selects only the explicit two-entry allowlist.

Students complete a field name, dictionary key, counter literal, or outcome string.
They then inspect supplied traces/tests and write evaluation/reflection evidence.
No required new function, dispatcher, loop, operation, or test suite is assigned.

### One boundary, explicit SDK, fixed replay

The supplied request callable takes history and returns a Responses dictionary.
Live mode calls `client.responses.create` with strict tool schemas and the final
answer schema; a separate first example demonstrates `responses.parse` with
Pydantic. Shared Python code validates final text. Replay returns hand-authored
illustrative subsets and checks actual tool results against the next saved step.
It does not generate responses or evaluate prompt changes.

Default code reads no credentials/live configuration. CLI `--live` explicitly
constructs the OpenAI client. The model ID is configuration rather than an untested
default. Exact model/feature compatibility and live latency/cost remain separate
verification. SDK guidance is source-checked; installed SDK JSON transport is tested
without real HTTP. Live/recorded instructor demonstration remains required delivery work.

### Boundaries and named stops

Process at most one tool proposal per response; request `parallel_tool_calls=False`
and reject unexpected parallel proposals. Python enforces two tool executions and
three total model requests, including final answer generation. Check counters before
their actions. Preserve provider output/history and matching call IDs. Display
observable application events, not private reasoning.

End on valid answer, unknown tool, invalid arguments/output/response, refusal,
incomplete response, API error, replay mismatch, or exhausted limits. Recovery is
manual. The SDK sets `max_retries=0`, timeout 20 seconds per socket operation, and
an output-token budget of 1024 per response. Neither timeout nor counters promise
a strict whole-run wall-clock deadline. Built-in API tool limits do not enforce our
custom-function cap.

### Evaluation and optional work

Supply five prompts: Portugal lookup, two-country total, comparison, missing France,
and attempted modification. Expected behavior specifies numeric facts/operations
and boundaries without requiring exact phrasing. Students compare expected and
observed outcomes manually. Replay evidence is labelled illustrative, and live
evidence includes model/date separately.

Optional work fits 180 minutes combined: prompt revision 45, CPU Ollama exploration
120 including install/download, additional saved-scenario inspection 15. Ollama
prerequisites identify server, downloaded model, and separate Python dependency.
Recommend no specific model until CPU tool/schema support is actually tested.

## Risks / Trade-offs

- The full loop has more branches than students should write: supply it, teach via
  trace, and confine blanks to tiny expressions.
- A one-string schema permits false statements: explicitly demonstrate that and
  compare model claims to deterministic tool results.
- Fixed scripts can look like live inference: label fixture provenance and evidence
  on every path; do not claim replay measures prompt revisions.
- API/SDK/model behavior changes: source-check official guidance, lock the SDK,
  test the installed codec, and keep live compatibility pending without live evidence.
- Planned timings can exceed beginner capacity: keep implementation optional and
  record beginner trials separately.

## Migration Plan

Add the numbered distribution and OpenSpec beside existing classes; update only
agreed week-05 details and shared navigation/verifier/status records. Leave earlier
pending verification tasks pending. No commit or push without a separate request.

## Open Questions

No user design decisions remain. Live model/demo availability, optional CPU model
selection, browser/desktop access, supported-platform setup, and measured beginner
timings require concrete delivery evidence rather than additional curriculum scope.

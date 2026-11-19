# Class 05 instructor notes

## Scope and facilitation

The approved interview requires **really simple missing pieces**: one answer field
name, one dictionary key, one limit literal, one outcome string, and written
evaluation/reflection. Supply all tool implementations, schemas, validation, SDK
handling, orchestration, and meaningful tests. Do not turn these into blank-function
or new-test-suite assignments. Students should inspect and explain the full flow.

Five ordered notebooks follow the previous classes' standalone kernel/import/
exercise conventions. The first three each contain a 20-minute introduction/demo
and a 10-minute exercise. The glossary is progressive reference material, not an
extra memorization assignment. No earlier exercise answers are needed.

| Time | Activity | Emphasis |
| --- | --- | --- |
| 0–8 | Model, prompt, context, token, SDK, harness | A model proposes; Python controls execution |
| 8–20 | One-field structured answer; SDK reading example | Validation checks shape, not truth; live demo or recording if prepared |
| 20–30 | 05.1.E1 | Complete only the answer field name |
| 30–38 | Two supplied read-only operations | Local 2023 data, persons, exact labels, missing is not zero |
| 38–50 | Tool proposal, arguments, allowlist, call ID/result | Inspect supplied dispatch and validation |
| 50–60 | 05.2.E1 | Complete only one dictionary key |
| 60–68 | Supplied bounded loop and a successful trace | Distinguish requests from actual executions |
| 68–80 | Repeated-call trace; tests versus evaluation | Third tool never executes; introduce five-prompt expectations |
| 80–90 | 05.3.E1 | Complete only the assertion literal 2 |

Independent work is preparation 30; guided walkthrough/tiny completions 60
(15 each in parts 1–3 plus first 15 in part 4); tests/saved failures 60 (remaining
45 in part 4 plus first 15 in part 5); evaluation 45; reflection 15. Each check,
reading, terminal command, and table-writing task is inside its allocation.
The project remains additional. These are designed budgets, not measured beginner
timings; trial and shorten activities before delivery if needed.

## Data, provider, and teaching boundaries

- `Observation` and `summarize` are reused from the **active class-04** package.
  Only the needed code/snapshot is adapted locally. No root legacy files are reused
  or tracked. Keep the [World Bank attribution](fixtures/README.md).
- Two countries/one year are enough for exact lookup, total, comparison, and absence.
  Do not call the total world population or imply live current data. The summary
  returns count/total/mean; the comparison intentionally uses two exact lookups.
- `Answer(answer: str)` is the entire final-answer contract. Show a schema-valid
  false sentence to make the factual limitation concrete. Compare claims with the
  deterministic tool results; the evaluation table uses human judgments, not exact
  wording matches or automatic model-quality scores.
- The first standalone SDK demo uses `responses.parse`; the complete harness uses
  `responses.create` with the same strict schema and explicit Pydantic validation.
  Both branches are supplied. Replay and live requests share the application loop.
- `make_replay` is a small callable over a named illustrative script. It checks actual
  tool outputs before returning the next canned response. It is not a model and
  cannot evaluate a changed prompt. No synthetic model response is called a recording.
- The harness validates permitted arguments, uses only an explicit dictionary,
  preserves provider history/call IDs, requests no parallel tools, checks both
  counters, and validates final text. Tool data cannot grant new permissions.
  Trace events describe observable behavior, not private reasoning.
- A returned `refusal` item differs from an ordinary answer explaining read-only
  limits. An empty lookup differs from an invalid call and from an API failure.
  All failures stop the run for manual recovery; the SDK has no hidden retry.
- Required notebook/reference/CLI execution reads neither credentials nor live model
  configuration. No services start, HTTP requests occur, or models download by default.
  [AI_SETUP.md](AI_SETUP.md) supplies explicit live switches and optional local
  prerequisites. No specific local model, live latency, or live SDK/model compatibility
  is asserted without actual delivery evidence.
- The instructor must prepare a live demonstration or genuine recording. This remains
  a separate pending delivery task if access is unavailable. Institution-funded access
  can be offered if available; purchasing credits is never required for completion.
- Optional work totals at most 180 minutes, including local-model installation and
  downloads. RAG, provider abstractions, frameworks, async, arbitrary code execution,
  additional tools, and building a UI are outside required scope.

## References and expected evidence

| Exercise | Reference | Expected evidence |
| --- | --- | --- |
| 05.1.E1 | [answer field](solutions/exercise_05_1_e1.py) | `parsed.answer`; strict shape versus factual truth |
| 05.2.E1 | [dictionary lookup](solutions/exercise_05_2_e1.py) | `allowed_tools[name]`; unknown name and invalid arguments rejected |
| 05.3.E1 | [limit literal](solutions/exercise_05_3_e1.py) | Two results, three proposals/requests, tool_limit |
| 05.4.H1 | [failure outcome](solutions/exercise_05_4_h1.py) | invalid_arguments; valid missing-country result distinguished |
| 05.5.H1 | [five judgments](solutions/exercise_05_5_h1.py) | Five expected/observed rows labelled illustrative replay |
| 05.5.H2 | [failure reflection](solutions/exercise_05_5_h2.py) | Responsible layer, proposed fix/check, honest evidence limit |

## Author verification commands

From this class directory:

```sh
uv sync --locked
uv run --locked python -m pytest -q
uv run --locked ruff check report_app solutions tests
uv run --locked ruff format --check report_app solutions tests
uv run --locked python ../../templates/class-content/verify.py .
uv run --locked python -m report_app --evaluate
```

For offline notebook/reference evidence, use an author-only `sitecustomize` hook
outside the distribution to block real HTTP transports in child processes. SDK
transport tests use `httpx.MockTransport` and do not bypass the actual SDK codec.
Use a temporary copy for a seeded dispatch/limit regression and show that an
unchanged behavior test fails for the intended reason, then restore and rerun.
Recreate the environment from the lockfile in a fresh folder excluding caches/
`.venv`; distinguish a cache-assisted recreation from a first offline installation.
Export HTML outside the release folder and inspect the actual presentation when
a browser surface is available. Run the authoring guide's actual VS Code desktop
reveal/inspect/separately-execute/sentinel checklist on a temporary notebook.

## Verification record

Verified on **19 November 2026**, on Linux/CPU with Python 3.13.11, OpenAI SDK
2.54.0, HTTPX 0.28.1, Pydantic 2.14.4, pytest 9.2.0, Ruff 0.17.6, IPython 9.18.1,
ipykernel 7.4.0, nbformat 5.11.1, nbclient 0.11.0, and nbconvert 7.17.2.
The full package resolution is in the distributed lockfile.

- All **32 deterministic tests** pass. They cover saved data and exact absence,
  strict missing/wrong/extra/malformed arguments, unknown names, invalid final
  answers, refusal/incomplete responses, actual non-execution on invalid proposals,
  actual third-tool blocking, pre-request limits, replay/result mismatch, and
  invalid response envelopes. Provider reasoning items remain in history without
  entering the displayed trace.
- The installed SDK ran through `httpx.MockTransport` for real request serialization
  and response parsing, the one-field `responses.parse` demo, tool-result/call-ID
  history, strict schemas, parallel-tool setting, and a synthetic HTTP 429. That
  429 produced exactly one transport attempt with retries disabled. Timeout and
  connection exceptions stop as safe named outcomes. **No real model was called.**
- All five notebooks passed the shared checker in fresh kernels. All six reference
  modules ran independently. Ordered navigation, local links, class workspace,
  environment paths, 90/210-minute budgets, unique exercise triples, exact commented
  loaders, and clean release outputs/execution counts passed. An external author-only
  `sitecustomize` guard blocked real HTTPX/Requests/urllib transport in kernels and
  subprocesses. Default execution did not attempt HTTP.
- The `%load` kernel-protocol check confirms replacement source, deferred execution,
  and separate execution creating `reference_answer`. This is **not** proof of
  VS Code frontend behavior or answer-cell preservation in that editor.
- The unchanged third-tool test rejected a temporary copy with
  `MAX_TOOL_EXECUTIONS = 3`: its dispatch spy observed **3**, expected **2**. After
  restoring the original cap, the same targeted test passed. The release copy was
  not seeded or altered by this check.
- A fresh copied distribution excluding `.venv`/caches recreated the locked
  environment with `uv sync --locked --offline` using the populated temporary uv
  cache. Its five-row replay CLI and all 32 tests passed with real HTTP blocked.
  This establishes cache-assisted recreation, not a network-free first install.
- Ruff lint and format checks pass for the package, references, and tests. The
  shared template/specimen and classes **01–05** pass the regression verifier with
  each class's own environment and the offline guard. Strict OpenSpec validation
  passes. Code/snapshot reuse is from the active class-04 distribution; the MIT
  notice and World Bank attribution are included locally.
- Five HTML exports were generated under `/tmp/adpro27-class05-preview` and passed
  structural inspection of headings, exercise blockquotes, tables, required/optional
  labels, and lack of external image dependencies. **Browser visual inspection
  remains pending:** the in-app browser rejected the local `file:` preview URL
  under its URL security policy. No alternate route was used to bypass that block.
- **VS Code desktop checks remain pending:** UI inventory exposes no native editor.
  Actual rendering and reveal/inspect/separately-execute with an answer sentinel
  still require the desktop checklist on a temporary copy.
- Live model/feature/access/cost/latency verification and the required instructor
  demonstration or genuine recording remain pending. Replay fixtures are illustrative,
  and mocked SDK transport is not live evidence. No optional Ollama model has passed
  CPU tool/schema tests, so no model is recommended. Windows/other-platform execution
  and beginner timing trials remain pending.
- **Publication:** Class 05 was committed as `568bcaa` and successfully pushed to
  `origin/main` on **19 November 2026**, following the user's explicit request.
  Publication does not complete the pending browser/desktop, live-model/demo,
  optional CPU Ollama, platform, or beginner-timing checks.

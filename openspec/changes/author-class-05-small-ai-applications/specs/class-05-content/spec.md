## ADDED Requirements

### Requirement: Complete ordered class-five distribution

The class SHALL provide five ordered 05.1–05.5 notebooks, six independent explained
references, a progressive glossary, a supplied local package, fixtures, a numbered
VS Code workspace, and a class-local uv manifest/lockfile. Every notebook SHALL run
fresh without earlier answers, services, credentials, or model downloads.

#### Scenario: Student starts with failure practice
- **WHEN** part 05.4 is run in the installed class workspace
- **THEN** its own imports and saved traces work without running earlier parts
- **AND** default execution does not contact a service or read live configuration

### Requirement: Explicit foundations and tiny student completions

The class SHALL explain model, prompt, token, context, SDK, structured output, tool
call, harness, and agent responsibilities before or alongside SDK mechanics. The
glossary SHALL give short definitions and application examples progressively.
All validation, tool implementations, SDK handling, and loop management SHALL be
supplied. Required student code changes SHALL be individual expressions or lines;
no dispatcher, loop, new tool, or test suite implementation SHALL be assigned.

The course outcome SHALL describe building a small harness from supplied components.
Students SHALL connect the permitted lookup, change one validated label in the
existing 15-minute follow-up, and inspect the changed result together with successful
and rejected calls. This SHALL NOT require implementing the supplied dispatcher or loop.

#### Scenario: Student changes a validated lookup input
- **WHEN** the student changes the connected lookup from PRT:2023 to FRA:2023
- **THEN** the same supplied function returns an empty list instead of a Portugal row
- **AND** the student explains that absence is valid while forbidden names and invalid arguments are rejected

#### Scenario: Student attempts the dispatch exercise
- **WHEN** the student follows Exercise 05.2.E1
- **THEN** only one dictionary-key expression needs completing
- **AND** permitted functions and argument validation are already supplied

### Requirement: Two read-only tools over familiar saved observations

The class SHALL preserve Observation(label, value), reuse the attributed class-04
Portugal/Spain 2023 snapshot, and supply get_summary() and find_observations(label).
Lookup SHALL match labels exactly; absent data SHALL return an empty list, not
invented zero. Tools SHALL NOT write data or execute arbitrary model-proposed code.

#### Scenario: Student asks about France
- **WHEN** find_observations receives FRA:2023
- **THEN** it returns an empty list
- **AND** evaluation expects an absent-data explanation without an invented population

### Requirement: Validated contracts and bounded supplied orchestration

The harness SHALL permit only the two supplied tool names, validate strict JSON
arguments before execution, reject multiple simultaneous tool proposals, preserve
call/result linkage and necessary provider history, and validate a final Answer
containing only answer: str. Python SHALL enforce at most two tool executions and
three model requests per run, including final-answer generation. The lesson SHALL
state that valid schema shape does not establish factual accuracy.

#### Scenario: A model proposes a third tool
- **WHEN** two tools have executed and a third is proposed on request three
- **THEN** the run stops with tool_limit
- **AND** no third tool executes and no fourth model request is sent

#### Scenario: A forbidden name is proposed
- **WHEN** the response names delete_data
- **THEN** the run stops with unknown_tool before executing that operation

### Requirement: Explicit named failure outcomes and manual recovery

The supplied harness SHALL end the current run on unknown tools, invalid arguments,
invalid output/response, refusal, incomplete responses, API errors, replay mismatch,
or exhausted limits. Recovery SHALL be manual; live SDK retries SHALL be disabled.
Traces SHALL describe observable application events without exposing private reasoning
or API credentials. An ordinary answer explaining read-only limits SHALL be
distinguished from a provider refusal item.

#### Scenario: The provider response is incomplete
- **WHEN** the response status is incomplete
- **THEN** no partial output is accepted as a valid answer and no tool executes

### Requirement: Direct OpenAI SDK and honest replay fallback

The main live path SHALL use direct OpenAI SDK Responses calls. The first structured
example SHALL demonstrate Pydantic parsing. A small saved-script callable SHALL
replace only the model-request boundary while shared application validation,
dispatch, counters, and traces remain active. Default execution SHALL use explicitly
illustrative replay without reading credentials or live model configuration. Live
execution SHALL require explicit opt-in and model/key configuration. A live instructor
demonstration or genuine recording SHALL be a distinct delivery task.

#### Scenario: A tool implementation produces an unexpected result during replay
- **WHEN** the next replay step expects the actual result
- **THEN** a mismatch stops as replay_error rather than silently returning a canned success

### Requirement: Deterministic tests and five-prompt evaluation

The class SHALL supply meaningful deterministic checks for policy, arguments,
outputs, failures, actual executions, model-request limits, and installed SDK
request/response integration with replaced HTTP transport. Five supplied prompts
SHALL cover Portugal, combined total, comparison, absent country, and modification.
Students SHALL record expected/observed behavior and explain a failure at the
schema/tool/prompt/application layer. Replay, mocked SDK, and live evidence SHALL
remain distinct; replay SHALL NOT be claimed to evaluate a changed prompt.

#### Scenario: Student records replay evaluation
- **WHEN** the five supplied scripts are evaluated without model access
- **THEN** the table is labelled illustrative replay
- **AND** it does not claim live model quality or prompt-improvement evidence

### Requirement: Complete approved workload and optional local scope

The class SHALL allocate 90 classroom and 210 independent minutes including all
setup, reading, exercises, tests, evaluation, and reflection. Preparation SHALL use
30 independent minutes; parts 1–3 SHALL each use 30 classroom/15 independent,
part 4 60 independent, and part 5 75 independent. Independent categories SHALL be
30 preparation, 60 guided walkthrough/tiny edits, 60 tests/saved failures, 45
evaluation, and 15 reflection. Optional work SHALL fit 180 separate minutes.
Ollama SHALL remain a separate extension with server/model/Python prerequisites;
no specific model SHALL be recommended before CPU tool/schema verification.

#### Scenario: Student sums required work
- **WHEN** preparation and the five part budgets are summed
- **THEN** they total 90 classroom and 210 independent minutes without additional setup

### Requirement: Honest verification and publication records

Checks SHALL cover fresh kernels, independent references, clean loaders/release
state, paths/navigation, workload, offline execution, meaningful regression
detection, fresh-copy environment recreation, and earlier-class regression checks.
Static exports/inspection, browser visual review, actual VS Code desktop interaction,
live-model demonstration, CPU Ollama, supported-platform checks, and beginner trials
SHALL have separate evidence. Unavailable checks SHALL remain pending; publication
SHALL only be recorded after a successful publication action.

#### Scenario: Only automated and static checks are available
- **WHEN** the execution record is updated
- **THEN** those checks do not complete desktop or live-model tasks


### Requirement: Offline teaching illustrations

The approved course-wide review SHALL be reflected in local teaching illustrations
(5 in this class), captions, meaningful alternative text, and source/license
records. Reused images SHALL retain file-specific credits and licenses. Original
course-specific diagrams SHALL retain editable Mermaid sources and CC BY 4.0
credits, alongside local PNG renderings. Images SHALL explain existing concepts
within the unchanged workload; their display SHALL NOT require network access or
a student-installed renderer.

#### Scenario: Student opens the complete class folder offline
- **WHEN** a notebook displays a teaching illustration
- **THEN** it reads the bundled PNG and supplies a textual explanation and credit
- **AND** editable source and license information are available locally or through the source guide

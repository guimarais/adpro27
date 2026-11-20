# Class 06 instructor notes

## Approved scope and facilitation

The user confirmed both interview recommendations on **20 November 2026**:
continue tiny student edits with supplied UI/workflow/tests/configuration, and
publish class contents at the root of each student's separate GitHub repository.
No new project rubric, assessment weights, or student orchestration/UI/test-suite
implementation is assigned. The course repository's nested workflow is an example
for that distribution, not an active course-root workflow.

Supply the five standalone notebooks and six explained references. Default
notebook/reference execution reads local files and imports modules only. Run the
actual server manually; do not start it, run Git, create accounts, or publish from
Run All or reference loaders. Every part has its own setup/imports. Preparation
includes accounts, dependency installation, and VS Code kernel selection.

| Time | Activity | Expected observation |
| --- | --- | --- |
| 0–10 | Browser/server/entrypoint and supplied modules | UI calls existing functions; saved year/units visible |
| 10–20 | Run supplied UI, filter, inspect absence/replay | 58,930,702 total; absent France is not zero |
| 20–30 | 06.1.E1, one heading line | Local heading changes, numbers stay correct |
| 30–40 | Separate student root/GitHub/account authorization | Hidden workflow/lockfile/ignore files preserved |
| 40–50 | Start hosting build; inspect stages/logs/Python | Correct entrypoint, Python 3.13, manifest+lock route |
| 50–60 | 06.2.E1, one filename and diagnosis | Saved case available while build/access is pending |
| 60–70 | Read one supplied Actions job | Offline tests/lint/format; no model/API credentials |
| 70–80 | Explain exact commit, logs/secrets, host updates | CI is separate from auto-deployment |
| 80–90 | 06.3.E1, release line and evidence | Check run and visible hosted release recorded separately |

Independent allocation: preparation 45; deployment 60 (10 each in 06.1–06.2,
40 in 06.4); CI 60 (10 in 06.3, 50 in 06.4); logs/docs 30 and peer handover 15
in 06.5. Optional private AI 45 plus Podman 135 has a separate maximum of 180.
Project work remains additional. These are designed budgets, not beginner trials.

## Boundaries and teaching risks

- Required online completion is an actual public saved-data app usable without
  AI credentials, plus an actual passing Actions run for a later commit, visible
  release, useful safe diagnostics, README, and peer result. Saved logs and local
  AppTest cannot replace hosted evidence. Leave failures/unavailable access pending.
- Account preparation includes sign-in/connection for the intended student repo;
  organization restrictions may need human support. Never put auth tokens in
  commands, screenshots, or notebooks. The guide instructs manual Git operations
  in a separate copied folder, not the course checkout, and stages explicit paths.
- Host and local/CI Python minors must match. The class selects 3.13 in the pin,
  manifest, workflow, and hosting instructions. Documentation recognizes uv.lock;
  actual hosting installer/runtime behavior still needs a real build check.
- `Observation`, data/functions, bounded AI package, fixtures, and 32 harness tests
  are reused from active class 05. The live constructor additionally accepts
  explicit settings without writing process-wide environment variables. All
  default paths remain saved/replay. Retain MIT and World Bank attribution.
- The UI's live branch is disabled by default. It requires complete server-side
  model/key/access-code configuration, code entry, and one browser-session run.
  The harness retains two executions/three requests, no retries, and 1024 output
  tokens per response. Use only private hosting for optional instructor live
  demonstrations. The code/session gate is not identity or a global cost cap.
  A new session can run again; do not expose an unrestricted key anonymously.
- The public required app uses no live configuration and no laptop Ollama.
  A remote localhost is the remote server. No local model or GPU is required.
- Logs show event names/types and counters, not credential values or raw provider
  bodies. Errors in optional settings preserve useful data/replay behavior.
- AppTest checks Python/widgets headlessly; browser presentation and VS Code
  reveal/inspect/separate execution need their own actual checks on temporary
  notebooks, preserving an answer sentinel. Do not mark those from a protocol test.

## Reference evidence

| Exercise | Reference | Expected evidence |
| --- | --- | --- |
| 06.1.E1 | [one heading](solutions/exercise_06_1_e1.py) | Title edit and actual local UI result |
| 06.2.E1 | [entrypoint](solutions/exercise_06_2_e1.py) | Correct filename; separate actual build/URL record |
| 06.3.E1 | [release](solutions/exercise_06_3_e1.py) | Later commit, check result, hosted release |
| 06.4.H1 | [test command](solutions/exercise_06_4_h1.py) | All checks retained; adapted command in actual run |
| 06.5.H1 | [safe diagnostic](solutions/exercise_06_5_h1.py) | Stage/cause/fix/check without private exception text |
| 06.5.H2 | [handover](solutions/exercise_06_5_h2.py) | Actual peer/URL/README result or honest pending record |

## Author verification

From this class directory:

```sh
uv sync --locked
uv run --locked python -m pytest -q
uv run --locked ruff check streamlit_app.py report_app solutions tests
uv run --locked ruff format --check streamlit_app.py report_app solutions tests
uv run --locked python ../../templates/class-content/verify.py .
```

The last command is an instructor tool in the course checkout, not a dependency
of the standalone student repository/CI. For release verification, execute
notebooks/references with an external HTTP-blocking hook; export HTML outside
the release tree. Recreate a fresh copied standalone folder from its lockfile.
Use a temporary copy for a seeded behavior regression and prove an unchanged
test detects it. Keep runtime/no-dev app checks separate from default dev checks.
Rehearse actual hosting, exact-commit CI, public handover, optional container,
and platform/timing work separately before delivery.

## Verification record — 20 November 2026

Verified on Linux/CPU with Python **3.13.11**, Streamlit **1.67.0**, OpenAI SDK
**2.54.0**, Pydantic **2.14.4**, pytest **9.2.0**, Ruff **0.17.6**, IPython
**9.18.1**, ipykernel **7.4.0**, nbformat **5.11.1**, nbclient **0.11.0**, and
nbconvert **7.17.2**. Exact package resolution is in `uv.lock`.

- All **39 tests** pass: the 32 reused harness/SDK/data checks and seven new UI
  checks. The real Streamlit script is exercised through AppTest for filtering,
  absent-country behavior, labelled replay, case-specific result display,
  incomplete/disabled live settings, access-code gating, the session allowance,
  and safe error/log handling. Live requests are replaced; no real model is called.
  Ruff lint/format checks pass for the app, package, solutions, and tests.
- All five notebooks and six references pass in fresh kernels/processes, including
  setup/navigation/links, the workspace, clean release cells, exercise triples,
  exact commented loaders, 90/210-minute allocations, and `%load` replacement,
  deferred execution, and separate execution. An external author-only
  `/tmp/adpro27-class06-guard/sitecustomize.py` blocks real HTTPX, Requests, and
  urllib transports in tests, kernels, and child references. No default HTTP
  attempt occurred. Local Jupyter sockets required sandbox permission.
- The shared template/specimen and classes **01–06** pass the same guarded
  regression verifier using each class's own environment. A temporary README
  changing class-06 preparation from 45 to 30 minutes was rejected. The final
  part-5 timing clarification was also checked without changing code or budgets.
- A fresh standalone copy recreated its locked environment with
  `uv sync --locked --offline` using the populated temporary cache. All 39 tests
  passed. A temporary seed resetting the stored live-session allowance to false
  caused two live-boundary calls; the unchanged behavior test expected one and
  failed. Restoring the original made that targeted test pass. No release file
  was seeded. After `uv sync --locked --offline --no-dev`, the real app still ran
  through AppTest with the expected saved total and missing-secret defaults.
  This is cache-assisted recreation, not an offline first installation.
- In that copied folder, a scratch Git repository confirmed the workflow at root,
  the app/manifest/lockfile paths, and exclusion of a harmless disabled
  `.streamlit/secrets.toml` sentinel plus `.venv`. Its explicit staged path list
  was inspected; no remote, commit, push, or real credential was involved. The
  supplied workflow parses as YAML with one job, push/PR triggers, read-only
  content permissions, and all three check commands. Hosted execution is separate.
- The app was run on a loopback-only server with real outbound HTTP blocked and
  telemetry disabled. In the in-app browser its actual initial layout, saved
  total **58,930,702**, Portugal **10,578,174**, absent-France message with no
  numeric metric, and saved replay result (two requests/one execution) were
  checked. The page clearly displayed saved year/units/attribution and disabled
  live AI. This establishes local browser evidence, not public hosting or VS Code.
- All five HTML previews were exported under `/tmp/adpro27-class06-preview` and
  passed structural/release-state checks. **HTML browser visual review remains
  pending:** the in-app browser rejected the `file:` preview protocol under its
  URL policy. No workaround was attempted. **VS Code desktop remains pending:**
  the UI inventory exposes no native editor. Actual notebook rendering and the
  answer-sentinel reveal/inspect/separate-execution check are still required.
- The optional Containerfile was built and run with rootless **Podman 4.9.3** on
  **Linux/amd64**, using isolated temporary storage outside the restricted sandbox.
  The image runs without dev dependencies or secrets. Container AppTest checks
  cover the saved total, absence, replay, and case-specific display; the running
  server's loopback-mapped health endpoint returned HTTP 200/`ok`. This is local
  packaging/runtime evidence only. macOS/Windows VM setup was not exercised.
- Official hosting/authentication/dependency/secrets, uv CI/container integration,
  GitHub Actions, and Podman guidance was checked on 20 November; links are in
  the guides. Strict OpenSpec validation passes for all seven changes. Source
  documentation is not a hosted build or a live-model compatibility check.
- **Pending delivery:** actual GitHub/Community Cloud authorization, hosted
  dependency/Python build, exact-commit hosted Actions, public URL/later release,
  and peer handover were not performed. Optional live model/private-sharing
  verification, supported-platform setup, and beginner timing remain pending.
  **Publication at the initial authoring check:** no course commit/push or public
  app publication had been performed. The follow-up record below documents the
  later successful course-file publication separately from hosted app delivery.


## Course-wide review follow-up — 20 November 2026

**Implementation:** 5 local illustrations now support the existing material.
See [sources, credits, licenses, and editable Mermaid diagrams](IMAGE_SUGGESTIONS.md).
The course-wide changes correct prose/navigation/timing drift while preserving
exercise IDs, answer/loader separation, standalone starts, and the 90/210 budget.

**Difficult-topic cue:** Local checkout, hosted repository, runner, hosting process, and browser are distinct locations. Trace checks and deployment independently, and keep public saved-data behavior separate from optional private live AI.

**Automated/static verification:** the template/specimen and all six authored
classes pass the shared fresh-kernel/reference/navigation/release/workload and
`%load` protocol checks, with Requests, HTTPX, and urllib real HTTP blocked.
The existing class-02–06 suites total 100 passing tests; their Ruff lint/format
checks pass. Local image paths, PNG signatures/dimensions, alt text, and embedded
HTML exports pass across all 30 notebooks. No application runtime behavior was
changed by this review.

**Browser verification:** all five class exports load in local headless Chrome
157.0.8103.78 with external HTTP requests blocked. All images load, no page-wide
horizontal overflow was detected, and the actual image cells/captions/credits
and first exercise card of each part were visually inspected in browser
screenshots. The overly tall failure map was compacted and diagrams use their
natural display size. Mermaid CLI 12.2.0 / Mermaid 12.3.0 produced the original
PNGs. Authoring tools/previews live under `/tmp/adpro27-course-visuals`; they are
not new student dependencies. This supersedes earlier local-file-policy limits
for static HTML previews only.

**Still pending:** actual VS Code desktop rendering and reveal/inspect/separately
execute behavior. Browser screenshots and kernel protocol checks do not complete
that task. Beginner timings, supported-platform trials, real hosted PR/deployment/
CI/peer evidence, and live-model checks retain their existing separate status.
Published in `705efd3`, pushed to `origin/main` on **20 November 2026** following the user's explicit commit/push request. No public app deployment or new desktop/live-model/beginner trial is implied.

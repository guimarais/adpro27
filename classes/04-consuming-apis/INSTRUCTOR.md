# Class 04 instructor notes

## Agenda and depth

The user-approved simplification keeps API consumption to request → status → JSON → validated records. Frontend/backend roles and a supplied FastAPI route motivate the exchange. Server implementation, pagination, and retry loops are optional; students do not need async code, OAuth, provider SDKs, model installations, or a framework for HTTP clients.

| Time | Activity | Instructor emphasis |
| --- | --- | --- |
| 0–10 | 04.1 architecture and HTTP | Trace client/server/data roles; localhost is this machine |
| 10–20 | Supplied FastAPI route and one GET | Manual server start; show query and JSON; saved fallback |
| 20–30 | 04.1.E1 | Prepare/change one parameter, inspect a useful field |
| 30–50 | 04.2 small Requests client | Timeout, status, JSON, validation; preserve Observation/Report |
| 50–60 | 04.2.E1 | Write four-step client with a supplied response boundary |
| 60–70 | 04.3 failure diagnosis | Distinguish network/status/body/record; do not silently skip |
| 70–80 | OpenAI and Ollama previews | Two POST contracts; use saved envelopes when unprepared |
| 80–90 | 04.3.E1 | Diagnose three saved failures and give next actions |

Required independent time: preparation 30; parts 1/2/3 each 15; part 4 reading/integration 60 (20 + 40); part 5 tests/review 75 (45 + 30). All checks/reflection count inside these allocations. The project remains additional. These are planning allocations, not measured beginner timings; trial before teaching.

## Distribution and facilitation

- Supply the whole folder and its lockfile. Reuse the supplied code even if earlier exercises were unfinished. The model/calculation/Report files were copied from the active class-03 package; no root legacy material is reused or newly tracked.
- Run the default CLI first. It uses saved data. Start the localhost server only as an explicit terminal demonstration. A server occupies its terminal until Ctrl+C; the client uses a second terminal. The notebooks never start background servers.
- `/docs` is an example browser frontend; its external JavaScript/CSS can be unavailable. Plain JSON URLs and `/openapi.json` work without those UI assets. Do not let this become a frontend-development exercise.
- A direct call to the route function is not HTTP. A prepared Requests request sends nothing. A supplied Response fixture is not a service. The route-function test checks filtering without sockets; real localhost HTTP is verified separately. Name these distinctions as evidence boundaries.
- The core client does not retry. Its errors retain causes. Inspect the cause for the precise invalid record but avoid displaying authorization headers. TypeAdapter validates the whole list; one malformed row rejects the result.
- World Bank integration is two countries/one year/one page. `label=ISO:year`, value=persons. Missing is not zero. Do not describe this total as world population. The fixture is a real snapshot; live values may change. Preserve the [source/attribution record](fixtures/README.md).
- Use the two five-minute AI previews as familiar API examples, with [AI_DEMOS.md](AI_DEMOS.md). Live calls are explicit and instructor-prepared; replay is enough for required completion. The AI fixtures are illustrative subsets, not live captures. No model/CPU recommendation has been tested. Dedicated AI behavior and SDK teaching belongs in class 05.
- Optional extensions total at most 180 minutes. Keep pagination/rate-limit retry algorithms, extra routes, and live model setup outside required completion.
- [Creative Commons diagram suggestions](IMAGE_SUGGESTIONS.md) follow class 03's optional source-link approach. Three candidates have verified file-page creators/licenses and placement/credit notes. They are not embedded assets; direct downloads were rate-limited, and their actual rendered legibility remains to be checked before inclusion.

## Exercise references

| Exercise | Reference | Expected evidence |
| --- | --- | --- |
| 04.1.E1 | [query and field](solutions/exercise_04_1_e1.py) | Prepared URL, saved status/body, north value 2.5, architecture roles |
| 04.2.E1 | [small client](solutions/exercise_04_2_e1.py) | Explicit timeout/status/decode/validation and one-record summary |
| 04.3.E1 | [failure diagnosis](solutions/exercise_04_3_e1.py) | Three distinct failure layers and actionable messages |
| 04.4.H1 | [public-data mapping](solutions/exercise_04_4_h1.py) | ISO/year, persons, two-country scope, saved/live distinction |
| 04.5.H1 | [two failure tests](solutions/exercise_04_5_h1.py) | Timeout and invalid-record checks that detect regressions |
| 04.5.H2 | [AI envelope explanation](solutions/exercise_04_5_h2.py) | Known-fixture text extraction and honest evidence labels |

## Author checks

From this directory:

```sh
uv sync --locked
uv run --locked python ../../templates/class-content/verify.py .
uv run --locked python -m pytest -q
uv run --locked python -m pytest -q solutions/exercise_04_5_h1.py
uv run --locked ruff check report_app examples solutions tests
uv run --locked ruff format --check report_app examples solutions tests
```

Run local server/client smoke tests with a disposable port and terminate the server afterward. Run a public-data smoke test separately from the deterministic suite. Check a fresh copied distribution excluding .venv/caches. Execute all notebooks/references with network disabled or intercepted. For regression evidence, deliberately bypass validation only in a temporary copy and ensure the unchanged failure tests detect it. Render all five static notebooks for presentation review. Verify each source-link path and budget using the shared checker.

## Verification record

Verified on **19 November 2026**, on Linux/CPU with Python 3.13.11, Requests 2.34.2, FastAPI 0.165.0, Uvicorn 0.54.0, Pydantic 2.14.4, pytest 9.2.0, Ruff 0.17.6, IPython 9.18.1, ipykernel 7.4.0, nbformat 5.11.1, nbclient 0.11.0, and nbconvert 7.17.2. The lockfile records the full resolution.

- All five notebooks passed the shared checker in fresh kernels, including ordered navigation, workspace/environment paths, 90/210-minute budgets, six exercise chains, local links, independent references, and untouched release outputs/counts/loaders. An author-only sitecustomize hook blocked real Requests session calls in kernels and reference/test subprocesses; no default activity attempted HTTP.
- All six references executed independently. The `%load` replacement-payload probe confirmed that loading inserts source without executing it, then separate execution creates the expected result. This is a kernel-protocol check, not a VS Code GUI check.
- The default suite passed **15 tests**; the independently targeted failure-test reference passed **2 tests**. Ruff lint and format checks passed. The suite checks transport/status/body/schema failures, route-function filtering, World Bank mapping/missing values/page boundaries, replay without credentials/network, and the live AI branches' HTTP shapes using replaced POSTs.
- A temporary copy with validation deliberately bypassed caused the unchanged missing-value test to fail with **DID NOT RAISE**, not an import/collection error. Restoring validation made the same test pass.
- A fresh copy excluding environments/caches recreated the locked environment using a populated package cache, produced the expected saved-data CLI summary, and passed all 15 tests with HTTP calls blocked. Initial dependency installation still needs network access; this check does not establish a network-free first installation.
- A real temporary localhost Uvicorn server was contacted using Requests. All-record, north, unknown-label, empty-label, 404, and OpenAPI checks passed. The server was terminated afterward. These checks are separate from direct route-function calls and saved responses.
- The real public World Bank request succeeded: two validated records, total **58,930,702**, mean **29,465,351** persons for the selected two-country 2023 query. Its actual response is the attributed fixture. These values are an authoring snapshot, not a guarantee of later live estimates.
- The generic template/specimen and all classes 01–04 passed the shared regression verifier with each class's own environment. OpenSpec strict validation passed. Five HTML previews were exported under /tmp and structurally inspected: headings, tables, exercise blockquotes/labels, and required/optional labels are present.

**Pending visual/editor checks:** browser inventory and native-app inventory were empty in the available UI tools. Actual browser visual review of the HTML previews and VS Code desktop rendering/reveal/inspect/execute remain unverified. On a temporary copy, preserve an answer-cell sentinel while loading a reference, then execute the populated cell separately; record actual editor/extension versions. HTML structure and kernel protocol are not substitutes for those interactions.

**Other delivery limits:** Windows execution and beginner timing trials were not performed. No live OpenAI/Ollama call, account-cost/access verification, model download, or CPU-model benchmark was performed; AI HTTP contracts were checked against official documentation and tested with controlled responses. The required AI path is illustrative replay. Publication had not occurred at initial verification; see PROJECT_STATUS.md at the repository root for the current publication record.

## Content review and image follow-up — 19 November 2026

[Independent standards/specification review](REVIEW.md) found one P3 setup issue: the credential prompt was advertised as POSIX syntax but requires Bash. This is corrected and checked with harmless supplied input. No confirmed spec violation was found. A minor reference-completeness concern was also resolved: 04.4.H1 now explicitly demonstrates rejection of a missing population value, matching its full prompt.

After these changes, all 15 tests, the updated standalone reference, Ruff, and all five fresh notebooks/six references passed. Real Requests session calls were blocked in the notebook/reference checks; the release notebooks remain clean. The new [image guide](IMAGE_SUGGESTIONS.md) and three notebook placement notes add no required workload or network execution. Individual source pages/licenses were verified, but direct asset downloads returned HTTP 429 and the UI inventory again had no browsers/apps. No browser/VS Code or rendered-candidate visual check is marked complete. Original live-smoke evidence above was not rerun or relabelled during this follow-up.

**Images remain pending:** download, embed, and visually inspect the selected diagram assets with their credits/alternative text before treating the illustration work as complete. The source-suggestion guide is complete; OpenSpec task 4.5 retains the unfinished image work.

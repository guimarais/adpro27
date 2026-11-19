# Class 04 — Consuming APIs

Understand frontend/backend roles, inspect a supplied FastAPI service, and consume JSON with one small Requests client. Validate at the boundary, report useful failures, and keep the existing Observation/Report model. OpenAI and Ollama appear as short HTTP demonstrations; building the AI application belongs in class 05.

**Images pending:** [diagram suggestions and credits](IMAGE_SUGGESTIONS.md) are prepared; downloading, embedding, and visually checking the selected images remain outstanding.

## Read in this order

| File | In class (minutes) | Independent (minutes) | Focus |
| --- | --- | --- | --- |
| Preparation and VS Code setup | 0 | 30 | Install the supplied environment; verify kernel and saved-data run |
| [04.1 — Frontend, backend, and HTTP](04.1-frontend-backend-and-http.ipynb) | 30 | 15 | Trace a request; inspect the supplied FastAPI route and a query parameter |
| [04.2 — A small validated client](04.2-a-small-validated-client.ipynb) | 30 | 15 | Request → check status → decode JSON → validate records |
| [04.3 — Failures and AI API previews](04.3-failures-and-ai-api-previews.ipynb) | 30 | 15 | Diagnose failures; short OpenAI/Ollama HTTP demonstrations |
| [04.4 — Public data and authentication](04.4-public-data-and-authentication.ipynb) | 0 | 60 | Map two-country World Bank data; distinguish parameters/body/header |
| [04.5 — Testing and consolidation](04.5-testing-and-consolidation.ipynb) | 0 | 75 | Test meaningful failures; explain both AI envelopes and hand over results |
| **Total required** | **90** | **210** | **Five hours, including setup and completion checks** |

The first three parts each contain 20 minutes of teaching/demo plus a ten-minute exercise. Independent work is preparation 30 + three follow-ups of 15 + public-data work 60 + testing/review 75. Part 04.4 includes 20 minutes guided reading and 40 exercise; part 04.5 contains 45 + 30 minute exercises. Optional pagination/retries/server extensions are excluded, with at most 180 additional minutes. The instructor-designed project is additional workload.

## Prepare — 30 minutes, included above

1. Download the **complete class folder**, or from the course repository use `git pull --ff-only` when your working tree permits it. For a new checkout use `git clone <instructor-provided-course-repository-url>`, then open this numbered class folder. No answers from earlier classes are required. You need basic Python and the class-01/02 concepts; the complete code is supplied again.
2. With [uv](https://docs.astral.sh/uv/getting-started/installation/), Python 3.11+, and [VS Code](https://code.visualstudio.com/) available, open a terminal in **this class directory** and run `uv sync --locked`. This installs the kernel, Requests, Pydantic, FastAPI/Uvicorn, pytest, and author/test tools. The first installation needs network access. Use the matching lockfile; do not maintain a separate requirements file.
3. Open [04-consuming-apis.code-workspace](04-consuming-apis.code-workspace) using **File → Open Workspace from File…**. Install the recommended Microsoft Python/Jupyter extensions. Open 04.1, choose **Select Kernel → Select Another Kernel… → Python Environments**, and select this class's `.venv`.
4. If the environment is missing, run `uv run --locked python -c "import sys; print(sys.executable)"`. Use that path in **Python: Select Interpreter → Enter interpreter path…**, then select it separately in the notebook kernel picker. Each notebook prints its interpreter and checks its working directory. Do not fix imports by changing sys.path or silently changing directory.
5. Run `uv run --locked python -m report_app`: expect count 2, total 6, mean 3. Use **Restart Kernel → Run All** separately for each notebook. Finish any setup problems within this preparation allowance; use the saved-data route during class if the local server is not ready.

Default Run All and reference solutions use saved inputs and offline checks. They do not start a service, contact external APIs, read credentials, download models, or install packages. Restart the kernel after changing a Python module in a scratch copy. A running server is required only for the explicit local HTTP demonstration below.

## Try real local HTTP — two terminals

In terminal A, from this directory:

```sh
uv run --locked python -m uvicorn report_app.service:app --host 127.0.0.1 --port 8000
```

Keep it running. Visit `http://127.0.0.1:8000/observations?label=north` in a browser. `/docs` provides an interactive API frontend; its standard assets need internet access, so the plain JSON URL and `/openapi.json` are the recovery route if the docs page does not load.

In terminal B, also in this directory:

```sh
uv run --locked python -m report_app --local
```

Expect the same summary as the saved-data run. A missing server produces a useful connection error; start terminal A and check the address. If port 8000 is occupied, stop your earlier teaching server or choose another port and call `fetch_observations` with that explicit URL. Stop your server with **Ctrl+C** when finished. The service binds only to this machine; deployment is class 06.

## Public data and AI previews

```sh
uv run --locked python -m report_app --public
uv run --locked python -m examples.ai_http openai
uv run --locked python -m examples.ai_http ollama
```

The first command contacts the **World Bank** for Portugal/Spain population in 2023 and needs internet but no key. The two AI commands read **illustrative saved JSON**. See [AI_DEMOS.md](AI_DEMOS.md) for the instructor's explicit live switches. Required work needs no paid key, Ollama installation, model download, or GPU. If the public request is unavailable, complete the saved mapping and label it offline. See [fixture provenance and attribution](fixtures/README.md).

## Files and completion

```text
report_app/       # existing model/Report/calculation, small client, supplied service, public adapter
examples/         # saved HTTP setup and explicit AI HTTP demonstrations
fixtures/         # normal/failure data, actual public snapshot, illustrative AI envelopes
solutions/        # six independent references; attempts remain in separate notebook cells
tests/            # deterministic normal/failure/route/AI-transport checks
```

Exercise IDs run from `04.1.E1` to `04.5.H2`. Attempt first; uncomment the separate `%load solutions/...` line and run to reveal, then execute that populated cell separately. Kernel restart/clearing outputs does not restore a loaded source cell. References are accessible teaching material, not hidden answers.

Completion evidence: a request with a timeout, validated records, useful failures, two failure tests, the public-data mapping, and an explanation of frontend/backend and AI request/response roles. Label saved versus live evidence. See [instructor agenda and verification](INSTRUCTOR.md) and [optional Creative Commons diagram suggestions](IMAGE_SUGGESTIONS.md).

Checks from this directory:

```sh
uv run --locked python -m pytest -q
uv run --locked ruff check report_app examples solutions tests
uv run --locked ruff format --check report_app examples solutions tests
```

The normal suite is offline. The route-function check is a direct Python call; real localhost HTTP is verified separately. Students write HTTP calls with Requests. Server construction and pagination/retry implementations remain optional.

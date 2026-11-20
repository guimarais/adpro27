# Class 06 — Deployment and automated delivery

Publish a supplied data explorer and explain how a tested change reaches another
person. The app, read-only AI harness, workflow, tests, and configuration handling
are supplied. Required edits are small lines and settings; no UI framework,
deployment system, or new test suite needs implementing. The saved-data app works
without AI credentials. Hosting and GitHub accounts are needed for actual online
completion; installation and account preparation are included below.

## Read in this order

| File | In class (minutes) | Independent (minutes) | Focus |
| --- | --- | --- | --- |
| Preparation and VS Code setup | 0 | 45 | Install/run; prepare GitHub and hosting accounts |
| [06.1 — A thin local interface](06.1-a-thin-local-interface.ipynb) | 30 | 10 | Run the supplied app and change one heading |
| [06.2 — From GitHub to hosting](06.2-from-github-to-hosting.ipynb) | 30 | 10 | Select the entrypoint and interpret a build log |
| [06.3 — Automated checks and updates](06.3-automated-checks-and-updates.ipynb) | 30 | 10 | Inspect CI and verify a subsequent release |
| [06.4 — Guided deployment and CI practice](06.4-guided-deployment-and-ci-practice.ipynb) | 0 | 90 | Finish hosting (40) and adapt supplied checks (50) |
| [06.5 — Configuration, logs, and handover](06.5-configuration-logs-and-handover.ipynb) | 0 | 45 | Diagnostics/documentation (30), peer handover (15) |
| **Total required** | **90** | **210** | **Five hours including accounts and completion checks** |

The first three parts each contain 20 minutes teaching/demo and 10 minutes
exercise. Independent categories are preparation 45, deployment 60 (10 in each
of parts 1–2 and 40 in part 4), CI 60 (10 in part 3 and 50 in part 4), logs/docs
30, and peer handover 15. These are designed allocations, not measured beginner
timings. The separately designed project is additional work.

## Prepare — 45 minutes, included above

1. **5 minutes:** obtain this complete folder, including hidden `.github`,
   `.streamlit`, `.gitignore`, and `.python-version` files. Use the course download
   or clone/pull the instructor-provided repository. Earlier answers are not needed.
2. **10 minutes:** install [uv](https://docs.astral.sh/uv/getting-started/installation/)
   if needed. From this class folder run `uv sync --locked`. The supplied
   `.python-version` selects **Python 3.13**; let uv install it when necessary.
   First installation needs network access. The lockfile includes the app/kernel;
   the default dev group supplies pytest, Ruff, and notebook authoring tools.
3. **5 minutes:** open [06-deployment.code-workspace](06-deployment.code-workspace)
   through VS Code **File → Open Workspace from File…**. Install the recommended
   Microsoft Python/Jupyter extensions. Select **Select Kernel → Select Another
   Kernel… → Python Environments → this class's .venv**. If missing, run
   `uv run --locked python -c "import sys; print(sys.executable)"`, use **Python:
   Select Interpreter → Enter interpreter path…**, and then separately select
   that environment as the notebook kernel. Check each notebook's printed path.
4. **5 minutes:** run `uv run --locked streamlit run streamlit_app.py
   --browser.gatherUsageStats=false`. Open the printed local URL. Expect total
   **58,930,702 persons** for the two saved 2023 observations. Select `PRT:2023`
   for **10,578,174**; `FRA:2023` means absent, not zero. Stop the server with Ctrl+C.
5. **20 minutes:** sign in to your GitHub account and Streamlit Community Cloud;
   authorize the GitHub connection for your own intended student repository.
   Read the first two sections of [the deployment guide](DEPLOYMENT.md).
   Account/authentication delays use this budget; ask the instructor for help or
   use the saved log exercise while access is resolved. Saved logs do not replace
   the eventual public URL/check evidence. Never paste credentials into a notebook.

## Run and check locally

From the class folder, later the root of your student repository:

```sh
uv sync --locked
uv run --locked streamlit run streamlit_app.py --browser.gatherUsageStats=false
```

In another terminal, in the same folder:

```sh
uv run --locked python -m pytest -q
uv run --locked ruff check streamlit_app.py report_app solutions tests
uv run --locked ruff format --check streamlit_app.py report_app solutions tests
uv run --locked python -m report_app --evaluate
```

The tests, notebooks, reference solutions, saved data, and replay need no external
service after installation. The local browser talks to your Streamlit server;
that does not make the app public. Do not run a server or Git commands inside a
Python notebook cell. Default notebook Run All reads supplied files only.

## Create the student repository

Copy the **contents** of this folder to a separate working folder, retaining hidden
files and excluding `.venv`, caches, and any real secrets. Initialize your own
repository there as described in [DEPLOYMENT.md](DEPLOYMENT.md). Its root must
contain `streamlit_app.py`, `pyproject.toml`, `uv.lock`, and `.github/workflows`.
A fork that leaves the files nested under `classes/06-deployment` is a different
layout and will not activate the supplied nested workflow. Do not initialize a
nested Git repository inside the course checkout.

The complete class folder is both the runnable starter and the supplied reference
application. Your small exercise edits remain separate from the explained
[reference solutions](solutions/exercise_06_1_e1.py). Attempt each notebook answer
cell first; uncomment and run its separate `%load` cell to reveal the reference,
then execute the populated loader as a second action. Keep your answer intact.
Use a clean copy to restore original commented loaders after exploration.

## Hosting, configuration, and completion

- [Deployment and secrets](DEPLOYMENT.md): root layout, GitHub authentication,
  Python selection, dependency detection, logs, subsequent updates, optional AI.
- [Supplied workflow](.github/workflows/checks.yml): one job for offline tests and
  lint/format checks; installation itself needs network access.
- [Failure cases](fixtures/deployment-failures.json): explicitly illustrative logs.
- [Instructor agenda and evidence](INSTRUCTOR.md): actual author checks and pending
  hosted/browser/desktop/platform checks.

Completion evidence is a public app URL usable without AI credentials, the exact
commit and passing Actions run for a later small change, its visible hosted
release, one diagnosed failure, safe useful logs, and a peer's README/URL result.
Record actual results in the final notebook; leave unavailable evidence pending.
CI and automatic hosting updates are separate mechanisms: a red check does not
itself stop Community Cloud from updating the app. GitHub Pages serves static
files and cannot run this Python server.

Optional extensions share **180 minutes maximum**: private instructor/live-AI
exploration up to 45 minutes including setup, and [Podman packaging](PODMAN.md)
up to 135 minutes including installation/download. No GPU or paid model access
is needed for required completion. Never put a paid unrestricted key behind a
public anonymous button. A remote server's localhost cannot reach laptop Ollama.

Code is copyright 2026 Luis Guimarais under the [MIT license](LICENSE). The local
`report_app`, harness tests, and small fixtures are reused from active class 05;
the live request constructor additionally accepts explicit server-side settings.
The new UI/tests and lessons are local to class 06. Snapshot provenance and
separate World Bank terms are in [fixtures/README.md](fixtures/README.md).
No root legacy content is reused.


## Local illustrations

5 local teaching visuals are embedded with captions, alternative text, and credits. Keep `images/` with the notebooks. [Sources, licenses, editable Mermaid files, and teaching notes](IMAGE_SUGGESTIONS.md). These explain existing material within the allocated time; no renderer or internet connection is needed to display them.

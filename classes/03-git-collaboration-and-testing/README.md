# Class 03 — Git, collaboration, and testing

Make changes that another person can inspect and verify. Git basics start this block; pytest then turns behavior contracts into repeatable evidence. Basic Python is sufficient to start. The complete local Report/Observation package is supplied again, so earlier answers and notebook state are unnecessary.

## Read in this order

| File | In class (minutes) | Independent (minutes) | Focus |
| --- | --- | --- | --- |
| Preparation and VS Code setup | 0 | 30 | Environment, Git installation, and account/access checks |
| [03.1 — Git basics](03.1-git-basics.ipynb) | 30 | 15 | Inspect, stage, review, and commit in a scratch repository |
| [03.2 — Branches and collaboration](03.2-branches-and-collaboration.ipynb) | 30 | 15 | Branches, remotes, pull requests, and review packets |
| [03.3 — Testing behavior with pytest](03.3-testing-behavior-with-pytest.ipynb) | 30 | 15 | Read a failure, specify behavior, and detect a seeded bug |
| [03.4 — Fixtures and parametrized tests](03.4-fixtures-and-parametrized-tests.ipynb) | 0 | 60 | Fresh setup, meaningful cases, and controlled input boundaries |
| [03.5 — Review and conflict practice](03.5-review-and-conflict-practice.ipynb) | 0 | 75 | Review a change for 45 minutes; diagnose/resolve for 30 |
| **Total required** | **90** | **210** | **Five hours including preparation** |

The first three parts each contain 20 minutes of teaching/demo and a ten-minute highlighted exercise. Independent work maps to 60 minutes of Git/setup (preparation plus 03.1–03.2 follow-ups), 45 of peer review, 75 of testing (03.3 follow-up plus 03.4), and 30 of failure/conflict diagnosis. All checks and reflection fit those allocations. Optional extensions are excluded. The instructor-managed project is additional workload.

## Prepare — 30 minutes, included above

1. Download the **complete class folder**. Install [VS Code](https://code.visualstudio.com/), Microsoft's Python and Jupyter extensions, [uv](https://docs.astral.sh/uv/getting-started/installation/), Python 3.11+, and [Git](https://git-scm.com/downloads). Check `git --version` in a terminal.
2. In a terminal in this class directory, run `uv sync --locked`. It installs Pydantic, the notebook kernel, pytest, and quality/authoring tools. Initial installation may require network access; default notebook execution uses only local assets.
3. Open [03-git-collaboration-and-testing.code-workspace](03-git-collaboration-and-testing.code-workspace) with **File → Open Workspace from File…**. Install recommended extensions. Open 03.1 and use **Select Kernel → Select Another Kernel… → Python Environments** to choose this folder's `.venv`.
4. If it is missing, run `uv run --locked python -c "import sys; print(sys.executable)"`. Select that path through **Python: Select Interpreter → Enter interpreter path…**, then choose it separately in the notebook kernel picker. Check `sys.executable` in each notebook setup cell.
5. Create a NEW scratch folder outside the course checkout and copy everything in [practice/git-starter](practice/git-starter/), including `.gitignore`, into it. All Git writing commands belong in that copy. Keep the supplied class source unchanged. Confirm GitHub/classroom access if available; [REVIEW_GUIDE.md](REVIEW_GUIDE.md) gives an explicit offline alternative for review practice.

Before class, also prepare a separate complete application scratch copy outside the course checkout, excluding `.venv`, `.git`, and caches; run `uv sync --locked` in that copy. This preparation belongs to the same 30 minutes above and keeps copying/installing outside the ten-minute bug-fixing exercise. Keep the tiny Git starter and application copy separate. If installation exceeds preparation time, use an instructor-prepared copy and record the setup issue.

After Git basics in 03.1, an existing instructor repository can instead be obtained with:

```sh
git clone <instructor-provided-course-repository-url> adpro-course
cd adpro-course/classes/03-git-collaboration-and-testing
```

The URL is supplied by the instructor. Keep manual Git-writing exercises in the separate starter repository. Follow [the review guide](REVIEW_GUIDE.md) when choosing an existing classroom baseline versus your own new remote; do not combine unrelated histories.

An offline review packet is **provisional**. Part 03.5.H1 reserves 15 of its 45 minutes for actual PR publication/peer review or catch-up, followed by 30 minutes for the supplied regression review. If access remains blocked, schedule those same reserved 15 minutes later with the instructor and leave hosted completion pending; this does not add a second task to the budget.

Use **Restart Kernel → Run All** separately for each part. Each imports its own names and reads class-local files. After changing Python modules in a scratch copy, restart its notebook kernel to refresh imports. Default cells do not initialize repositories, change Git configuration, stage/commit/push, install packages, read credentials, or contact GitHub. Terminal commands are manual exercises; identify your working directory before running them.

## The runnable example

```text
report_app/       # models, calculation, Report state, local input boundary, CLI
  source.py      # reads bundled JSON; validates records before returning them
  sample.json    # two observations: 2.5 and 3.5
  __main__.py    # explicit entry point
practice/
  git-starter/   # tiny independent starter for manual scratch Git work
  snapshots/    # recorded status and diffs, not your checkout's live state
  review/       # proposed patch that breaks the empty-mean contract
  conflicts/    # a recorded conflict for offline reasoning
  buggy_mean.py # intentional bug, outside the passing default test suite
  test_buggy_mean.py
solutions/       # six references, revealed with commented %load cells
```

From the class directory:

```sh
uv run --locked python -m report_app
uv run --locked python -m pytest -q
uv run --locked ruff check report_app solutions tests
uv run --locked ruff format --check report_app solutions tests
```

The application produces name `class-03`, count `2`, total `6`, mean `3`. The default test suite should pass. Its test discovery is limited to `tests/` through `pyproject.toml`; it deliberately excludes the broken practice target.

To observe the intentional bug, run this **separate** command:

```sh
uv run --locked python -m pytest -q practice/test_buggy_mean.py
```

Expect **two failed assertions and exit code 1**. An import/collection error is a setup problem, not successful bug detection. Correct only a scratch copy and keep the supplied teaching example available for comparison.

## Working and revealing references

Exercises use IDs such as `03.1.E1` and `03.5.H1`. Each has a highlighted prompt, answer cell, and separate commented `%load solutions/...` cell. Attempt first. Uncomment the load line and run to reveal source; run the populated cell separately to execute it. Loading may replace its invoking cell, and a kernel restart does not remove loaded source. References never run Git mutations or installations; manual terminal steps stay comments.

Completion evidence is a coherent local commit, an actual hosted pull request with peer review, an explained review comment, a test that detects wrong behavior, and an explained conflict resolution. You must be able to explain and modify AI-assisted work. See [review guidance](REVIEW_GUIDE.md), [Creative Commons image suggestions](IMAGE_SUGGESTIONS.md), and [instructor notes](INSTRUCTOR.md).


## Local illustrations

4 local teaching visuals are embedded with captions, alternative text, and credits. Keep `images/` with the notebooks. [Sources, licenses, editable Mermaid files, and teaching notes](IMAGE_SUGGESTIONS.md). These explain existing material within the allocated time; no renderer or internet connection is needed to display them.

# Teaching class 03

Use [the class index](README.md) and the five ordered notebooks. Begin with Git basics; no Git knowledge is assumed. The complete local Report example supplies state, validation, calculation, and a small replaceable input boundary without requiring class-01/02 answers.

## Ninety-minute agenda

| Time | Activity | Evidence |
| --- | --- | --- |
| 0–20 | 03.1 working files, staging, history, status, two diffs | Explain which version a commit records |
| 20–30 | 03.1.E1 | A coherent scratch commit and inspected staged diff |
| 30–50 | 03.2 branches, remotes, fetch/pull/push, PRs | Distinguish fetch from integration and push from review |
| 50–60 | 03.2.E1 | A small branch plus review description; online PR or labeled offline packet |
| 60–80 | 03.3 pytest behavior/failures | Read the intended assertion failure, not a setup error |
| 80–90 | 03.3.E1 | Detect the bug, correct a scratch copy, keep the expectations |

Independent minutes: preparation 30 + Git follow-ups 30 = Git/setup 60; 03.5.H1 review 45; 03.3 follow-up 15 + 03.4 60 = testing 75; 03.5.H2 diagnosis/conflict 30. These total 210; checks and reflection are included. The separate project is additional workload. These are teaching estimates, not measured student completion times; trial with beginners and shorten if necessary.

## Facilitation and boundaries

- Have students copy the tiny Git starter into a new directory **outside** the actual course checkout, including `.gitignore`. Check their working directory before a writing command. Use repository-local identity configuration, named staging, and diff inspection.
- The notebooks read recorded output. Default execution and reference scripts never initialize, stage, commit, push, change configuration, install packages, or read credentials. GitHub activity is an explicit manual exercise using authorized repositories.
- Explain that `git diff` excludes untracked file contents and shows tracked unstaged edits; `git diff --staged` shows the proposed commit. Stage again if a subsequent edit should be included.
- Use the guided online PR route when access permits. The [offline route](REVIEW_GUIDE.md) practices the same review reasoning but must not be presented as an actual pull request. If setup/authentication is incomplete, use that route during class rather than consuming the exercise with account setup.
- For safe committed-change recovery, make an ordinary, disposable single-parent commit first, inspect it, then demonstrate `git revert --no-edit HEAD`. Revert records an inverse change and can conflict. Keep history-rewriting recovery outside this beginner block.
- Default pytest discovery is restricted to `tests/`. Running the explicit broken practice target must yield two assertion failures, exit code 1. A collection/import error is a setup problem. Never require a failing release Run All to teach failures.
- Show normal imports and fresh subprocess test runs. A monkeypatched reader still passes raw dictionaries through real schema validation. A fixture does not prove the behavior of a future live API.
- [Image suggestions](IMAGE_SUGGESTIONS.md) offer optional CC diagrams and ready credits. The staging and branch diagrams contain terminology that needs the supplied explanation; use text alongside them. No online images are required for a notebook run.

## References

| Exercise | Reference | Expected evidence |
| --- | --- | --- |
| 03.1.E1 | [local commit](solutions/exercise_03_1_e1.py) | Inspect → stage named files → staged diff → commit |
| 03.2.E1 | [branch and review](solutions/exercise_03_2_e1.py) | Clear source/target and problem/behavior/checks |
| 03.3.E1 | [corrected mean](solutions/exercise_03_3_e1.py) | Normal, empty, zero behavior; original tests retained |
| 03.4.H1 | [fixture/parameter/input checks](solutions/exercise_03_4_h1.py) | Fresh setup and controlled input with real validation |
| 03.5.H1 | [review](solutions/exercise_03_5_h1.py) | Concrete None/zero regression comment and evidence |
| 03.5.H2 | [diagnosis/conflict](solutions/exercise_03_5_h2.py) | Meaningful corrected behavior and resolved text |

Run from this class directory:

```sh
uv sync --locked
uv run --locked python ../../templates/class-content/verify.py .
uv run --locked python -m pytest -q
uv run --locked python -m pytest -q solutions/exercise_03_4_h1.py
uv run --locked ruff check report_app solutions tests
uv run --locked ruff format --check report_app solutions tests
```

The solution-specific pytest target is separate from default discovery. For the deliberate failures use `uv run --locked python -m pytest -q practice/test_buggy_mean.py`; expect two failures. To check correction, work on a temporary copy, replace the mean implementation according to its contract, and rerun the same two tests. To check the review patch, apply it only to another copy, confirm empty-input assertions fail, correct the behavior, then rerun the passing suite.

For Git drills, use disposable repositories with local identity and optionally a local bare remote; no real remote is needed for author verification. The reproducible conflict steps are in 03.5. A two-clone check should demonstrate that fetch alone leaves working files unchanged and `pull --ff-only` integrates a compatible update. Static previews can be exported with `jupyter nbconvert --to html` into a temporary directory.

## Verification record

Verified on **19 November 2026**, on Linux/CPU with Python 3.13.11, pytest 9.2.0, Pydantic 2.14.4, Ruff 0.17.6, IPython 9.18.1, ipykernel 7.4.0, nbformat 5.11.1, nbclient 0.11.0, and nbconvert 7.17.2. The supplied `uv.lock` is the full resolution.

- All five notebooks passed fresh-kernel Run All with untouched answer cells. Structure, ordered navigation, workspace/environment paths, six exercise chains, commented loaders, local links, and the 90/210-minute budget passed the shared checker. Outputs and execution counts remained empty in the release files.
- All six references executed independently as modules from the class directory. The `%load` probe returned source for replacement without creating `reference_plan` until a separate execution. This verifies the kernel protocol, not VS Code's GUI.
- The default suite passed **10 tests**. The separately targeted fixture/parameter/input reference passed **6 tests**. Ruff lint and format checks passed for `report_app`, `solutions`, and `tests`.
- The explicit broken practice target produced two intended assertion failures (exit code 1), with no collection error. Correcting only the implementation in a temporary copy made those same two tests pass. Applying the review patch in another temporary-copy state produced two empty-contract failures; restoring the intended behavior made all 10 default tests pass.
- A fresh copy excluding `.venv`/caches recreated its locked environment using the populated package cache, ran the expected CLI JSON (count 2, total 6, mean 3), and passed all 10 tests. First-time package installation can require network access; this cached recreation does not establish a network-free first installation.
- Git commands were verified only in disposable local repositories using local identities and a local bare remote: status/two diffs, named staging/commit, branch/merge, prepared ordinary revert, same-line conflict/resolution, push, fetch without working-file integration, and compatible `pull --ff-only`. Recorded snapshots came from that drill. No real course remote or history was changed; a hosted GitHub PR/authentication flow was not exercised by the author checks.
- The generic template/specimen and all class-01/02 notebooks/references passed regression checks. The checker now launches each authored class with its own environment; the template's environment does not need pytest simply because class 03 does.
- All five static HTML previews were visually inspected: exercise cards, timing, attempt/loader separation, code, and optional labels were readable. The three image suggestions' file-specific creators and CC licenses were checked against their source pages; illustrations remain optional links.

**Pending:** actual VS Code desktop rendering and reveal/inspect/execute interaction. The available UI tools do not expose the desktop editor. On a temporary class copy, select its `.venv`, restart/run each notebook, preserve an answer-cell sentinel while revealing a reference, then run the revealed reference separately. Record editor/extension versions when that check is performed. Static HTML review and IPython replacement-payload checks do not establish the desktop GUI result.

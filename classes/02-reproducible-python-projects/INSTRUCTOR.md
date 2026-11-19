# Teaching class 02

Use [the index](README.md) and five ordered notebooks. Students work with a complete local package; no class-01 runtime state or unfinished answer is required. Keep Git instruction in class 03.

## Ninety-minute agenda

| Time | Activity | Check |
| --- | --- | --- |
| 0–20 | 02.1 module layout/imports/entry point | Ask which file owns validation, calculation, state, and I/O |
| 20–30 | 02.1.E1 | A moved calculation is imported normally, without path hacks |
| 30–50 | 02.2 interpreters/venv/pip | Distinguish the kernel, terminal, and scratch Python |
| 50–60 | 02.2.E1 | Record the exact interpreter/package paths |
| 60–80 | 02.3 uv/manifest/lock/recreation | Contrast declared ranges with resolved versions |
| 80–90 | 02.3.E1 | Add a dependency in a new scratch project; inspect both files |

Independent work retains the agreed mapping: preparation/layout 30; refactoring 75 (02.1 follow-up 15 plus 02.5.H1 60); environments 60 (02.2/02.3 follow-ups 30 plus 02.5.H2 30); quality/docs 45 (02.4). Exercise checks/reflection belong inside these totals. Trial the tasks with a beginner before delivery.

## Implementation boundaries

- The provided Report composes validated Observations. Its calculation is a function, and its entry point owns file/print operations.
- `__main__` is guarded so importing it does not run the app. The package's input path is relative to the module file, not an accidental terminal directory.
- Notebook execution/reference inspection never installs dependencies or rewrites student files. Terminal/file-editing instructions remain comments in reference scripts.
- Use scratch projects for venv/pip and `uv init --bare --vcs none`; do not overwrite the notebook environment. A uv-managed environment can lack the pip module even though uv can install dependencies.
- Windows examples use explicit executable paths so activation-policy changes are unnecessary. On systems without venv support, resolve the Python installation with teaching support rather than installing into the system interpreter.
- Keep package publication, build-backend configuration, advanced mypy use, and automated Git hooks optional.

## References and expected evidence

| Exercise | Reference | Evidence |
| --- | --- | --- |
| 02.1.E1 | [module reference](solutions/exercise_02_1_e1.py) | A pure mean calculation plus normal import/call instructions |
| 02.2.E1 | [environment reference](solutions/exercise_02_2_e1.py) | Exact interpreter, prefix, and installed package paths |
| 02.3.E1 | [uv reference](solutions/exercise_02_3_e1.py) | Explicit scratch commands and manifest/lock interpretation |
| 02.4.H1 | [quality reference](solutions/exercise_02_4_h1.py) | Readable function, empty-data contract, and minimal run guide |
| 02.5.H1 | [refactor reference](solutions/exercise_02_5_h1.py) | Responsibilities in modules; original summary preserved |
| 02.5.H2 | [handover reference](solutions/exercise_02_5_h2.py) | Fresh-copy procedure and explicit run/check commands |

To verify from the class directory:

```sh
uv sync --locked
uv run --locked python ../../templates/class-content/verify.py .
uv run --locked python -m unittest discover -s tests -v
uv run --locked ruff check report_app solutions tests
uv run --locked ruff format --check report_app solutions tests
```

For static review, export the five notebooks to a temporary directory using `jupyter nbconvert --to html`. Test scratch install/recreation procedures on temporary copies, preserving the released material and lockfile. GUI verification must use VS Code's actual notebook editor and stay distinct from kernel/protocol checks.

## Verification record

Verified on **19 November 2026**, on Linux with Python 3.13.11, Pydantic 2.14.3, Ruff 0.17.5, ipykernel 7.4.0, IPython 9.18.1, nbformat 5.11.1, nbclient 0.11.0, and nbconvert 7.17.2. The exact dependency resolution is in the supplied lockfile.

- All five notebooks passed fresh-kernel Run All with blank answer cells. The shared checker validated ordered navigation, class workspace/environment paths, all six exercise chains, links, clean commented loaders, and the 90/210-minute budget.
- All six references ran independently as modules from the class directory. The `%load` probe returned the expected source-replacement payload without creating the reference's result variable until separate execution. This is a protocol check, not a GUI check.
- Four standard-library behavior tests passed: separate report state, empty-data contract, expected CLI JSON, and imports that do not run the application. Ruff lint and format checks passed for `report_app`, `solutions`, and `tests`; the deliberately messy practice input is excluded from that clean-reference scope.
- A temporary working copy excluding `.venv` recreated the locked environment from the populated cache and produced the expected application summary and passing Ruff checks. The documented no-Git `uv init --bare --vcs none`, `uv add pydantic`, and locked run commands were tested in another temporary project with network access for resolution.
- Standard `python -m venv`, interpreter-bound pip inspection, and Pydantic installation were tested in a disposable Linux environment. Windows PowerShell paths are provided but were not executed on Windows. Fresh dependency resolution/install can need the network; cached locked recreation and default notebook execution are separate cases.
- The existing generic template and all class-01 parts/references passed regression checks after reference execution changed to ordinary module invocation. Original class-01 files were preserved.
- All five notebooks were rendered to HTML and visually inspected in the browser. Exercise cards, time labels, code, and the explicit required/optional distinctions were readable; entry-point names and PowerShell relative executable paths were checked in the rendered text.

**Pending:** actual VS Code desktop rendering and reveal/inspect/execute interaction. The available UI tools do not expose the desktop editor. On a temporary class copy, choose its `.venv`, restart/run each notebook, preserve an answer-cell sentinel while revealing a solution, and record the editor/extension versions. Static HTML and kernel tests do not establish that desktop GUI result.

The time allocations are internally checked estimates, not a measured student trial. Trial and shorten required tasks if they exceed the five-hour core budget.

## Illustration update — 19 November 2026

Three local diagrams now support the existing demonstrations; see [sources and teaching notes](IMAGE_SUGGESTIONS.md). Their captions distinguish the analogy from the actual Python behavior. Discuss them within the allocated teaching/reading time. PNG assets retain their source content, with white display backgrounds for transparent diagrams. Creator/license metadata and local image links were checked; the existing pending VS Code desktop verification still applies.

The six updated notebook previews across classes 01 and 02 were rendered and inspected in the browser: all local images loaded, white display backgrounds were applied, and captions/credits were readable. Notebook schema, local links, image paths/dimensions, clean outputs/counts, and exact commented solution loaders passed static checks. No dependency or executable lesson-code changes were needed.

# Authoring a weekly block

Use [NN-topic](NN-topic/README.md) as the copyable template and [class 01](example/01-oop-and-schemas/README.md) as a short runnable specimen. The [course redesign](../../COURSE_REDESIGN.md) defines the agreed curriculum. The specimen demonstrates the format; authoring all six finished lessons is separate work.

## File responsibilities

| Format | Authoritative content |
| --- | --- |
| `.ipynb` | Teaching narrative, small demonstrations, exercise prompts, answer cells, solution loaders, timetable, and completion checks |
| `.py` | Reusable code, script-based exercises, reference solutions, and meaningful behavior checks |
| `README.md` | Prerequisites, preparation/launch instructions, and links to the lesson and supporting files |
| `.code-workspace` | VS Code class-folder root, default environment path, and Python/Jupyter extension recommendations |

Do not copy whole application modules into the notebook or repeat the full lesson in the README. Import a module for demonstrations. Use normal imports from the class directory, without changing `sys.path`.

## Numbering and copying

| Number | Directory and main notebook stem |
| --- | --- |
| `01` | `01-oop-and-schemas` |
| `02` | `02-reproducible-python-projects` |
| `03` | `03-git-collaboration-and-testing` |
| `04` | `04-consuming-apis` |
| `05` | `05-small-ai-applications` |
| `06` | `06-deployment` |

1. Copy the whole `NN-topic` folder to the chosen lesson location. Rename the folder, `NN-topic.ipynb`, and `NN-topic.code-workspace` using the same numbered stem above.
2. Rename `solutions/exercise_NN_*.py`, replacing `NN` with the two-digit class number.
3. Replace `NN` and the `{{...}}` authoring fields throughout Markdown, notebook cell source **and metadata**, solution filenames, and loader paths. Replace template-only links to this guide with links correct for the new location. Edit notebooks with Jupyter or nbformat so their JSON remains valid.
4. Replace the small demonstration, every exercise prompt, and the comment-only reference placeholders with the actual class material. Preserve the timed structure, cell roles, and solution workflow.
5. Replace the template README's environment placeholders and command with resolved instructions for the new location. Declare the class's dependencies through its selected uv project and distribute the matching lockfile. Update the workspace's `python.defaultInterpreterPath` to that environment directory. Keep its sole folder as `.` and `jupyter.notebookFileRoot` as `${workspaceFolder}` so the numbered class directory is the notebook working directory.

`NN` and `topic` are literal authoring placeholders, not class numbers. The first real class is `01`, never `00`. Exercise IDs such as `01.1` do not number separate classes.

The available supporting directories have distinct purposes:

- `examples/`: reusable demonstrations imported by the lesson.
- `exercises/`: scripts students edit when a notebook answer cell is insufficient.
- `solutions/`: local reference source used by `%load`; every referenced file must exist.
- `tests/`: behavior checks when the code needs them.
- `fixtures/`: small saved inputs/API/model responses that keep the default path offline.

Only create optional directories when they contain useful material. The template and specimen intentionally avoid empty scaffolding directories. Download/distribute complete class folders, not the notebook alone.

## Ordered lesson parts

The [authored first class](../../classes/01-oop-and-schemas/README.md) demonstrates a multipart variant: `01.1-objects-and-state.ipynb` through `01.5-practice-and-review.ipynb`, under one `01-oop-and-schemas` class directory and workspace. Its README is the ordered index and full workload table. Keep the original single-notebook template/specimen available for a block that fits that format.

For ordered parts, each notebook supplies its own imports, small teaching definitions, input, setup check, and links to the index and neighboring parts. Repeating a short week-01 class definition is intentional self-containment; do not import another notebook or depend on an earlier exercise answer. Application code can later be factored into modules when that topic is taught.

Use lesson-prefixed exercise IDs such as `01.2.E1` and `01.5.H1`, mapping to `solutions/exercise_01_2_e1.py` and `solutions/exercise_01_5_h1.py`. Preserve the three tagged prompt/answer/loader cells and the commented `%load` pattern. Each part's `course_lesson` notebook metadata records its ID, `in_class_minutes`, and `independent_minutes`; the checker compares these with the README and aggregates the whole class's budget. Do not force each file to contain all three interim exercises or a full five-hour schedule.

To verify a multipart class, pass its **directory** to the shared checker, for example from the repository root:

```sh
uv run --project classes/01-oop-and-schemas --locked python templates/class-content/verify.py classes/01-oop-and-schemas
```

The class owns its environment/lockfile and local fixtures, so students can download just that complete folder. The checker remains an instructor repository tool. Its default invocation checks the original template/specimen and the authored first class when present.

[Class 02](../../classes/02-reproducible-python-projects/README.md) uses the same ordered format with an explicitly supplied local Python package. Its notebooks import their own names from those files rather than repeat application code or import another notebook. The checker discovers authored class directories by default and executes each reference as a module from its class root, preserving ordinary imports.

[Class 03](../../classes/03-git-collaboration-and-testing/README.md) continues the format with Git basics first, followed by collaboration and pytest. Its default cells read recorded Git examples and keep writing commands as manual scratch-repository work. Independent time shifts to 60 minutes in part 4 and 75 in part 5 while preserving the 90/210 totals. The checker launches authored-class checks with each class's own `.venv` Python, so install each class with `uv sync --locked` before a full regression run. Its [image guide](../../classes/03-git-collaboration-and-testing/IMAGE_SUGGESTIONS.md) shows how to suggest process illustrations with file-specific CC credits, alternative text, and placement notes without adding an online execution dependency.

## Weekly structure and timing

Preserve purpose, outcomes, prerequisites, preparation, the class agenda, teaching/exercise cycles, guided independent work, completion checks/reflection, optional extensions, and references.

The class is three cycles of **20 minutes teaching/demo + 10 minutes exercise**: `0–20`, `20–30`, `30–50`, `50–60`, `60–80`, `80–90`. Use the class to introduce the initial portion of the block; guide students through the remaining material independently.

Independent work totals **210 minutes**, including preparation, reading, exercises, and review. The template starts with 30 + 45 + 90 + 45 minutes; rebalance those rows as needed while preserving the total. Exercise durations belong inside their matching budget, not on top of it. Assign setup/account preparation before the relevant class and count it once within that week's independent work.

Use the visible labels **In class**, **Independent work**, and **Optional extension**. Extensions can add up to 180 minutes and are excluded from required totals. The instructor's separately designed project is additional workload; this template supplies no project rubric, milestones, or new assessment weights. Git basics begin at the start of class 03; the first two classes require only downloaded starter folders and supplied launch instructions.

Trial tasks with a beginner before teaching. Reduce required content if it does not fit; do not absorb overruns into an unannounced workload increase.

## Highlighting exercises

Keep the portable Markdown heading and blockquote card. Each exercise must show its ID/title, time/classification, goal, starting point, task, observable completion criterion, and hint. The literal word **Exercise** and text labels keep it readable without color or emoji rendering. No custom CSS or notebook extensions are needed.

| Kind | Exercise IDs | Python solution paths |
| --- | --- | --- |
| Interim | `01.1`, `01.2`, `01.3` | `solutions/exercise_01_1.py`, `exercise_01_2.py`, `exercise_01_3.py` |
| Independent | `01.H1`, `01.H2`, … | `solutions/exercise_01_h1.py`, `exercise_01_h2.py`, … |

Each exercise has three separate cells:

1. Markdown prompt tagged `exercise`.
2. Student code/answer cell tagged `exercise-answer`.
3. Reference loader cell tagged `solution-loader`.

All three carry the same `exercise_id` cell metadata, for example `"01.1"`. Set these in Jupyter's property inspector/metadata editor or with nbformat. Keep IDs unique. The generic agenda cell is tagged `class-agenda`; its independent-work budget is tagged `independent-budget`, allowing the verification command to check totals.

For terminal tasks, the answer cell can contain comments recording commands/results or link to a script. Do not require a student to run Git commands from a Python cell.

## Revealing solutions with `%load`

Use a separate cell with exactly this pattern, substituting only the filename:

```python
# Reveal only after attempting the exercise.
# Remove the leading '# ' from the next line and run this cell.
# %load solutions/exercise_01_1.py
```

Students uncomment the last line and run the cell. IPython sends the file source as a `set_next_input` replacement payload, which VS Code's Jupyter extension handles by replacing the invoking cell. Executing the populated cell is a **second** action. Loading inside an answer cell could overwrite the student's attempt, so keep the cells separate. Verify this interaction in VS Code before release using the checklist below. See [IPython %load](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-load).

The commented form keeps an untouched Run All from revealing or executing references. Once a student loads a solution, its source is part of that notebook; later Run All can execute it. **Clearing outputs or restarting a kernel does not restore the original loader source.**

Reference files must include explanatory comments, independent setup/imports, and expected results. They can rely on documented class setup but not on unfinished answers. For terminal/prose tasks, use Python comments showing commands and explanations; never auto-run shell commands, downloads, or repository changes from those references. Distributing solutions makes them accessible reference material, not secret instructor-only content.

Relative paths are resolved from the **kernel working directory**. Open the supplied class workspace in VS Code and keep the visible setup check. If it fails, report the expected directory and workspace/kernel recovery steps; do not silently call `chdir`, mutate `sys.path`, or fetch a solution URL.

## Environment and verification

Use **VS Code desktop** with Microsoft's **Python** and **Jupyter** extensions. The class workspace files recommend these extensions and point to the shared [uv environment](pyproject.toml). Runtime dependencies are `ipykernel` and Pydantic; standard notebook verification/export tools are in the development group. Install uv and use Python 3.11 or newer. The first dependency installation needs network access; notebook activities and checks then use local data. A browser notebook server is not part of the student workflow. [VS Code notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), [kernel management](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management).

Students follow the numbered class README: run `uv sync --project <relative-project-path> --locked --no-dev`, open its `.code-workspace` through **File → Open Workspace from File…**, open the notebook, and select the shared `.venv` through **Select Kernel → Select Another Kernel… → Python Environments**. The first setup cell prints the interpreter path so they can confirm the selected environment.

If VS Code does not list that environment, the README's `uv run ... python -c "import sys; print(sys.executable)"` command prints its exact interpreter path. Select it using **Python: Select Interpreter → Enter interpreter path…**, then select the same environment in the notebook kernel picker. Terminal interpreter selection and notebook kernel selection are separate. `python.defaultInterpreterPath` is an initial default; an existing selection can override it. [Interpreter setting](https://code.visualstudio.com/docs/python/settings-reference).

The supplied workspaces open the numbered class folder, not the repository root. Keep this convention even when an editor's default notebook directory differs. Workspace paths use an environment **directory** rather than a Linux/Windows-specific executable path. [Workspace configuration](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces).

From this `templates/class-content` directory:

```sh
uv sync --locked
uv run --locked python verify.py
```

The verification command checks valid notebook structure, class/workspace names, workspace paths and extension recommendations, timing, exercise triples, local links, solution paths, clean outputs/execution counts, and the **exact commented loader source**. It executes copies in fresh kernels without writing outputs back to the release notebooks. The specimen has a shorter illustrative schedule; the full weekly totals are checked on the generic template. To inspect another authored class, pass its notebook path; it must preserve the documented exercise IDs/cell roles (additional independent exercises are permitted). Headless kernel execution does not establish that the VS Code frontend interaction works.

Run the specimen's meaningful state/validation checks from its directory:

```sh
uv run --project ../.. --locked python -m unittest discover -s tests -v
```

For a static preview, still from that numbered class directory, export outside the release tree:

```sh
uv run --project ../.. --locked jupyter nbconvert --to html --output-dir /tmp/adpro-preview 01-oop-and-schemas.ipynb
```

On Windows, replace `/tmp/adpro-preview` with a directory under your temporary folder. Open the exported HTML in a browser and confirm that the exercise cards and required/optional labels are visible.

### Frontend and release checklist

1. Work on a **temporary copy** of the notebook and its supporting files.
2. Open the class's `.code-workspace` in VS Code as documented in its README. Install the recommended extensions, select the course `.venv` notebook kernel, and use **Restart Kernel**, then **Run All**; empty answer cells must not fail and references must remain unrevealed.
3. Type a harmless comment in an answer cell. Uncomment and run the corresponding `%load` cell. Confirm that the reference appears in that loader cell, the answer survives, and the reference has not yet executed. Run the populated reference cell and check its expected result.
4. Inspect the exercise card and labels in VS Code's notebook editor and the static HTML preview. Text must convey meaning without relying on color. Also check that Python scripts open normally in the same workspace and the integrated terminal starts in the class directory.
5. Inspect the actual release copy's **source**: restore every original commented loader after testing. Clear outputs and execution counts, and remove private credentials or machine-specific paths. Do not distribute the temporary test copy.
6. Re-run verification, review local links and dependency instructions, and record the supported frontend/environment below. Existing course notebooks and historical projects remain untouched.

### Verification record — VS Code workflow

Environment and installed editor components inspected on **18 November 2026**, on Linux with CPU-only examples:

| Component | Version |
| --- | --- |
| Python | 3.13.11 |
| VS Code desktop (CLI) | 1.145.1 |
| Microsoft Jupyter extension | 2025.9.1 |
| Microsoft Python extension | 2026.10.0 |
| IPython / ipykernel | 9.18.1 / 7.4.0 |
| Pydantic | 2.14.3 |
| nbformat / nbclient / nbconvert | 5.11.1 / 0.11.0 / 7.17.2 |

- `uv run --locked python verify.py`: both distributed notebooks passed structure, IDs/tags, timing (template), local paths/links, clean loader source, and fresh-kernel Run All. No outputs were written back.
- The specimen's three `unittest` checks passed: independent object state, rejection of invalid input, and documented numeric-string coercion. Both reference solution modules produced their expected results independently of student answers.
- Negative checks on temporary copies rejected an active `%load`, overwritten loader source, a 211-minute independent budget, and retained execution counts. Launching each setup check from the wrong directory produced the documented recovery message.
- The installed VS Code Jupyter extension's `handleSetNextInput` implementation was inspected: replacement payloads edit the invoking cell's document. The kernel-level `%load` payload and deferred execution are checked separately from GUI behavior.
- The existing static HTML exercise presentation was reviewed. **VS Code GUI verification remains pending:** the available UI tools do not expose the desktop editor in this session. The frontend/release checklist above must be run in VS Code; earlier verification in a browser notebook editor does not establish a VS Code GUI result.
- The lockfile was generated from the declared uv project. Existing teaching notebooks and historical project materials were preserved. The first package installation requires network access; the verified notebook activities use local files.

Re-run automated checks after authoring or editing a class. Record the actual VS Code frontend result and extension versions when the pending GUI checks are performed.

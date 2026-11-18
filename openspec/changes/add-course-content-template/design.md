## Context

[COURSE_REDESIGN.md](../../../COURSE_REDESIGN.md) defines six weekly blocks for students who know basic Python. Every block has a 90-minute class and 210 minutes of independent work. Three approximately 20-minute teaching segments alternate with ten-minute exercises. The course project adds separate workload and is owned by the instructor.

The agreed order is:

| Number | Topic slug |
| --- | --- |
| `01` | `oop-and-schemas` |
| `02` | `reproducible-python-projects` |
| `03` | `git-collaboration-and-testing` |
| `04` | `consuming-apis` |
| `05` | `small-ai-applications` |
| `06` | `deployment` |

Current lessons are Jupyter notebooks with Python examples elsewhere in the repository. Their exercise callouts use HTML, but they do not have a consistent solution-loading or exercise metadata convention. No Markdown/notebook synchronization system is configured.

## Goals / Non-Goals

### Goals

- Make a weekly block straightforward to author, navigate, teach, and study independently.
- Keep explanation, runnable application code, and setup instructions in clear locations.
- Make each interim exercise obvious in both Jupyter and a static notebook preview.
- Reveal solutions from separate files using the user's requested `%load` workflow.
- Preserve student attempts and keep solutions absent from an untouched student notebook.
- Provide a copyable template plus a small real-numbered specimen that demonstrates its use.
- Make verification possible with ordinary notebook tools and a short documented checklist.

### Non-Goals

- Authoring all six complete classes or the separately assessed project.
- Building a template generator, synchronization service, LMS integration, or custom notebook extension.
- Moving the complete application into notebook cells.
- Treating downloadable solutions as confidential or access-controlled material.
- Requiring model credits, a local model, a GPU, or live external services to inspect and verify the template.

## Decisions

### 1. Use notebooks for the lesson narrative, modules for reusable code, and Markdown for entry/setup

The notebook holds explanations, small demonstrations, exercise prompts, answer space, and solution-loader cells. Python files hold reusable functions/classes and exercise/reference implementations. A short `README.md` gives launch instructions and links to the lesson and supporting files.

Keep each explanation in one authoritative location. The README links to the lesson rather than duplicating it. The notebook imports or points to application modules instead of copying whole modules into cells.

Markdown-only lessons would require students to move between prose and an execution surface. Notebook-only applications would weaken the course's module, testing, and Git goals. The hybrid gives each format a specific job without introducing automatic synchronization.

### 2. Provide a literal template directory and one compact specimen

Planned layout:

```text
templates/class-content/
  AUTHORING.md
  NN-topic/
    README.md
    NN-topic.ipynb
    examples/
    exercises/
    solutions/
      exercise_NN_1.py
      exercise_NN_2.py
      exercise_NN_3.py
      exercise_NN_h1.py
    tests/
    fixtures/
  example/
    01-oop-and-schemas/
      README.md
      01-oop-and-schemas.ipynb
      examples/
      exercises/
      solutions/
      tests/
      fixtures/
```

`NN` and `topic` are explicit template placeholders. When copied into a real block, use the two-digit number and the matching topic slug above. Do not use `00` for the first class or `01.1` to number a separate class notebook. Supporting Python filenames use valid identifiers such as `exercise_01_1.py`.

Only include meaningful supporting files in an authored class; document optional directories instead of filling them with dummy programs. Every provided loader, however, must point to an existing solution file. Include a short class-01 specimen under `example/` so it is clearly a demonstration of the format rather than the finished first class.

The specimen includes small plain-class and schema examples, one completed interim exercise chain, and one independent-exercise chain. Its introduction labels the content as illustrative; it does not pretend to supply a finished five-hour lesson. The generic template still allocates the complete weekly schedule and all three interim exercise slots.

### 3. Structure the entire weekly block explicitly

The notebook has these recognizable sections:

1. Class number, title, purpose, learning outcomes, and prerequisites.
2. Preparation, with its time counted inside the independent-work allowance.
3. Class agenda: `0–20`, `20–30`, `30–50`, `50–60`, `60–80`, `80–90` minutes.
4. Three teaching segments and exercises in that same order.
5. Guided independent work totaling 210 minutes, with independent exercise prompts.
6. Completion checks and a short reflection.
7. Optional extensions, clearly excluded from required time.
8. Key references and links to supporting materials.

Mark material as **In class**, **Independent work**, or **Optional extension** using text, not color alone. Include the class exercise time in the 90 minutes and the independent exercise time in the 210 minutes. Count setup and account preparation once. The assessed project is separate and has no template-imposed tasks or rubric.

### 4. Make exercise highlights portable and identifiers stable

Use standard Markdown: a level-three heading with the literal word `Exercise`, an optional puzzle symbol, and a blockquote containing the exercise fields. This renders without custom CSS in Jupyter and Markdown notebook previews. Do not rely solely on HTML colors or an editor-specific admonition syntax.

Example:

```markdown
### 🧩 Exercise 01.1 — Independent object state

> **In class · 10 minutes**
>
> **Goal:** Distinguish the state of two instances.
>
> **Start here:** The setup example above; use the answer cell below.
>
> **Task:** Create two instances, modify one, and inspect the other.
>
> **Check:** The second instance is unchanged; explain why.
>
> **Hint:** Inspect where the mutable state is created.
```

Classroom IDs are `01.1`, `01.2`, `01.3`; independent IDs are `01.H1`, `01.H2`, and so on. Number each category independently. Map `01.1` to `solutions/exercise_01_1.py` and `01.H1` to `solutions/exercise_01_h1.py`.

Notebook prompt cells use the `exercise` tag; student code cells use `exercise-answer`; solution cells use `solution-loader`. Each of these cells carries the same `exercise_id` metadata value. This enables inspection of the release state without requiring a custom frontend.

### 5. Reveal solutions through commented, opt-in `%load` cells

After each exercise prompt and answer space, provide a separate code cell:

```python
# Reveal only after attempting the exercise.
# Remove the leading '# ' from the next line and run this cell.
# %load solutions/exercise_01_1.py
```

Keep the magic commented in the distributed notebook. An untouched Run All therefore does not reveal solutions. Students choose to uncomment the command; IPython loads the file into the frontend for inspection. In a standard notebook frontend the invoking cell is replaced with the loaded source; executing that populated cell is a separate action. Confirm this interaction in the supported editor. [IPython `%load`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-load).

The answer cell remains separate because `%load` can replace its invoking cell. Solution files include an explanation, the reference implementation where relevant, and a small expected result. They work from the documented setup rather than depending on an earlier unfinished student answer.

For Git, terminal, or prose exercises, the `.py` solution contains Python comments with the steps and explanation. Loading or executing that comment-only solution does not run shell commands or modify a repository. The template does not turn solutions into automated infrastructure actions.

Active `%load` cells would expose solutions during Run All. Collapsible inline solutions would put the full answer in notebook source. Imports would execute a module instead of showing its code. Commented local `%load` cells meet the requested interaction directly.

### 6. Make the working directory and release state explicit

Relative `%load` paths resolve from the kernel's working directory. Document launching the notebook from the numbered class directory and include a small visible setup check for its `solutions/` directory. Do not silently change directories, fetch a solution from a URL, or modify `sys.path` as a path-recovery mechanism.

The authoring guide supplies environment instructions and identifies any specimen dependencies. Use the agreed uv workflow for the runnable specimen and explain the minimal week-01 launch steps without requiring prior Git or package-management instruction. The template README has clear authoring placeholders for the future class's dependency/run instructions; the worked specimen's instructions are fully resolved.

Distributed notebooks have empty outputs and null execution counts. Release inspection also verifies that every `solution-loader` cell contains only the documented commented loader, not loaded solution source. Clearing outputs or restarting a kernel cannot undo source inserted by `%load`.

### 7. Verify the artifact, not just the OpenSpec structure

Validate notebook format and metadata; inspect timing, IDs, links, file paths, exercise readability, and solution source state. Execute the unmodified template and specimen from a fresh kernel in offline/replay mode. Unanswered exercise cells and optional checks must not make Run All fail. Separately verify reveal/inspect/execute behavior on a temporary notebook copy in a supported Jupyter frontend, preserving the distributable source.

Use existing notebook validation/execution tools and documented checks; do not introduce a generator, service, or large validation framework. Notebook tooling added for the specimen should be declared in its environment. The implementation tasks include visual review because structural validity does not establish a readable exercise highlight.

## Risks / Trade-offs

- `%load` changes the invoking cell's source → use a separate loader cell, document the two-step reveal/execute process, and verify the frontend behavior.
- Run All can reveal or execute solutions after a user edits the notebook → distribute commented loaders and verify cell source on a clean release copy.
- Relative paths can fail when an editor uses a different kernel working directory → document the class launch directory, add a visible path check, and test the supported editor.
- A hybrid format can duplicate content → assign one authoritative location to explanations, code, and setup; link between them.
- A short specimen might be mistaken for a completed class → label it as a template demonstration, while preserving all weekly scheduling slots in the generic template.
- Exercise duration estimates can be optimistic → include completion criteria and authoring guidance to trial tasks with a beginner; optional work stays separate.

## Migration Plan

Add the template and specimen alongside the current materials. Document how to copy and number a new block. Later lesson-authoring changes can use the template without renaming or overwriting historical notebooks. Reverting this additive template change does not require moving the existing course materials.

## Open Questions

No user-facing design decisions remain. Implementers must verify `%load` in the supported notebook frontend and declare/test the specimen environment as part of the tasks below.

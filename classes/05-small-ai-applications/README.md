# Class 05 — Small AI applications

Build a small AI harness from supplied components that read two saved population observations.
Understand what the model proposes and what Python controls. Complete only tiny
expressions or single lines: the validation, SDK handling, tools, and loop are
supplied. No paid key, GPU, local model, or answers from earlier classes are needed.

## Read in this order

| File | In class (minutes) | Independent (minutes) | Focus |
| --- | --- | --- | --- |
| Preparation and VS Code setup | 0 | 30 | Install/run replay; read the first glossary group |
| [05.1 — Models, prompts, and structured answers](05.1-models-and-structured-answers.ipynb) | 30 | 15 | Model/application responsibilities; inspect one answer field |
| [05.2 — Two read-only tools](05.2-two-read-only-tools.ipynb) | 30 | 15 | Validate a proposed call; complete one dictionary lookup |
| [05.3 — A bounded harness](05.3-a-bounded-harness.ipynb) | 30 | 15 | Inspect traces; complete one limit assertion |
| [05.4 — Guided failure practice](05.4-guided-failure-practice.ipynb) | 0 | 60 | Follow supplied code and diagnose saved contract failures |
| [05.5 — Tests, evaluation, and review](05.5-tests-evaluation-and-review.ipynb) | 0 | 75 | Run supplied tests; evaluate five prompts; explain one failure |
| **Total required** | **90** | **210** | **Five hours including preparation and completion checks** |

Classroom parts contain 20 minutes teaching/demo and 10 minutes exercise each.
Independent work is preparation 30; guided walkthrough/tiny edits 60 (parts 1–3
follow-ups, 15 each, and part 4's first 15); supplied tests/saved failures 60
(part 4's next 45 and part 5's first 15); five-prompt evaluation 45; reflection 15.
No new dispatcher, loop, or tool implementation is assigned. Optional extensions
have a separate combined ceiling of 180 minutes. The instructor's project is additional.

## Prepare — 30 minutes, included above

1. **5 minutes:** obtain the complete folder, including fixtures and solutions.
   Download it, use `git pull --ff-only` when your working tree permits it, or
   `git clone <instructor-provided-course-repository-url>`. Basic Python and the
   earlier schema/function/test ideas help; all application code is supplied again.
2. **10 minutes:** with [uv](https://docs.astral.sh/uv/getting-started/installation/),
   Python 3.11+, and VS Code available, open a terminal in **this class directory**
   and run `uv sync --locked`. First installation needs network access. This installs
   the notebook kernel, Pydantic, the OpenAI SDK, pytest, and authoring tools.
3. **5 minutes:** open [05-small-ai-applications.code-workspace](05-small-ai-applications.code-workspace)
   using **File → Open Workspace from File…**, install the recommended Microsoft
   Python/Jupyter extensions, open 05.1, and select **Select Kernel → Select Another
   Kernel… → Python Environments → this class's .venv**. If missing, run
   `uv run --locked python -c "import sys; print(sys.executable)"`; use **Python:
   Select Interpreter → Enter interpreter path…**, then select that environment
   separately in the notebook kernel picker. Check the interpreter printed by the
   notebook. Open the numbered class folder, not the repository root.
4. **10 minutes:** run `uv run --locked python -m report_app` and read the first
   group in [the glossary](GLOSSARY.md). Expect `mode: replay`, `outcome: answered`,
   two model requests, one tool execution, and Portugal **10,578,174 persons** in
   the saved 2023 data. No key is required. If setup fails, check the folder and
   interpreter, rerun the locked sync, and use a supplied instructor environment;
   do not spend the lesson creating accounts or installing a model.

## Run and inspect

From this directory:

```sh
uv run --locked python -m report_app --structured
uv run --locked python -m report_app --case compare
uv run --locked python -m report_app --case repeated
uv run --locked python -m report_app --evaluate
uv run --locked python -m pytest -q
```

All these commands are offline after installation. A replay “model request” is a
call to a saved-script function, not an HTTP request. `repeated` stops with
`tool_limit`: three proposals, two actual executions, no fourth model request.
The five evaluation rows include expected behavior and an observed answer/trace;
you judge whether each expectation is met. They carry no automatic model-quality score.

## Working on exercises

Attempt the small blank in the notebook's separate answer cell. Untouched answer
cells contain comments, so Run All works. Each prompt has a hint and an observable
check. After attempting it, uncomment the separate `# %load solutions/...` line and
run that loader. The source appears there without executing; run it a second time
to execute it. Your answer cell should survive. Restarting/clearing outputs does
not restore a revealed loader; use a clean distribution copy when needed.

## Files and boundaries

- [Glossary](GLOSSARY.md): short definitions with examples from this application.
- [Supplied package](report_app/__init__.py): small [tools](report_app/tools.py),
  [provider/replay boundary](report_app/provider.py), [harness](report_app/harness.py),
  and [evaluation table](report_app/evaluation.py).
- [Saved-data provenance](fixtures/README.md): actual World Bank snapshot;
  model-response subsets are explicitly **illustrative**, not live captures.
- [Live OpenAI and optional Ollama](AI_SETUP.md): explicit opt-in only.
- [Instructor agenda and verification record](INSTRUCTOR.md).

`Observation(label, value)` and `summarize` continue class 04. Labels are `PRT:2023`
and `ESP:2023`; values are persons. An absent label returns `[]`, not zero. The two-country
summary is not world population. The final `Answer` contains only `answer: str`;
a schema-valid string can still state a false number. Check it against tool results.

Code provenance: `Observation` in `report_app/models.py` and `summarize` in
`report_app/analysis.py` are adapted/copied from the active
`classes/04-consuming-apis/report_app/` files. Course code is copyright 2026 Luis
Guimarais under the [included MIT license](LICENSE). Data attribution and the
snapshot's separate terms are recorded in [fixtures/README.md](fixtures/README.md).

## Completion and optional extensions

Show your connected permitted-function lookup, a one-line change from a present
to an absent validated label with the observed changed result, one inspected
trace, one rejected input, the two execution limits, passing supplied tests, a five-row expected/observed evaluation table with replay/live
labels, and a short explanation assigning one fix to schema/tool/prompt/application
logic. AI coding assistants may help; explain and modify the tiny lines yourself.

Optional, **180 minutes total maximum**: compare one prompt revision live (up to
45), investigate CPU Ollama using the separate setup guide (up to 120 including
downloads), or inspect one additional saved scenario (up to 15). Stop local setup
at its time budget. Required completion remains available through replay.


## Local illustrations

5 local teaching visuals are embedded with captions, alternative text, and credits. Keep `images/` with the notebooks. [Sources, licenses, editable Mermaid files, and teaching notes](IMAGE_SUGGESTIONS.md). These explain existing material within the allocated time; no renderer or internet connection is needed to display them.

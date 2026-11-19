# Class 02 — Reproducible, maintainable Python projects

Turn a small report script into a project another person can understand and run. This class assumes basic Python and familiarity with the Report/Observation idea, but supplies the complete example locally. No previous notebook, completed exercise, Git account, or model access is needed.

## Read in this order

| File | In class (minutes) | Independent (minutes) | Focus |
| --- | --- | --- | --- |
| Preparation and VS Code setup | 0 | 30 | Prepare the environment; read the layout and naming guide |
| [02.1 — Modules and imports](02.1-modules-and-imports.ipynb) | 30 | 15 | Split responsibilities and run a module entry point |
| [02.2 — Virtual environments and pip](02.2-virtual-environments-and-pip.ipynb) | 30 | 15 | Identify the interpreter and isolate installation |
| [02.3 — uv projects and lockfiles](02.3-uv-projects-and-lockfiles.ipynb) | 30 | 15 | Declare, lock, run, and recreate dependencies |
| [02.4 — Readable code and documentation](02.4-readable-code-and-documentation.ipynb) | 0 | 45 | Names, small functions, hints/docstrings, Ruff, and run instructions |
| [02.5 — Practice and handover](02.5-practice-and-handover.ipynb) | 0 | 90 | Refactor for 60 minutes and recreate/hand over for 30 |
| **Total required** | **90** | **210** | **Five hours including preparation** |

Each of the first three parts has a 20-minute teaching/demo segment and a ten-minute interim exercise. Independent activity maps to 30 minutes of preparation/layout reading, 75 of refactoring, 60 of environment work, and 45 of quality/documentation. Checks and reflection are included. Extensions are optional and the instructor's separate course project is additional workload.

## Prepare — 30 minutes, included above

1. Download the **complete class folder**. Install [VS Code](https://code.visualstudio.com/), its Microsoft Python/Jupyter extensions, [uv](https://docs.astral.sh/uv/getting-started/installation/), and Python 3.11 or newer if needed.
2. In a terminal in this folder run `uv sync --locked`. This installs the notebook kernel, Pydantic, and the authoring/quality tools including Ruff. Initial installation and the explicit scratch package-install exercises can need network access; notebook Run All itself uses local code/data.
3. Open [02-reproducible-python-projects.code-workspace](02-reproducible-python-projects.code-workspace) using **File → Open Workspace from File…**. Install its recommended extensions, open 02.1, and select this folder's `.venv` through **Select Kernel → Select Another Kernel… → Python Environments**.
4. If it is absent, run `uv run --locked python -c "import sys; print(sys.executable)"`, select that path through **Python: Select Interpreter → Enter interpreter path…**, then select the same environment in the notebook kernel picker. The terminal interpreter and notebook kernel are separate choices.
5. Run the setup cell and check the printed interpreter path. Reopen the class workspace/restart the kernel if local paths are missing. Read the package tree and the short naming/docstring introduction in 02.4 as part of this preparation; its practical exercise belongs to 02.4's own budget.

Open parts in order, but use **Restart Kernel → Run All** for each. Every part imports its own required names from the explicitly supplied package. It does not import another notebook or depend on earlier answers. After changing a `.py` module, restart the kernel to avoid confusing a cached import with the edited source. No browser notebook server is required.

## The example project

```text
report_app/
  __init__.py       # package identity; no automatic CLI run
  models.py         # Observation input contract
  analysis.py       # pure summary calculation
  report.py         # Report owns state and uses the calculation
  __main__.py       # explicit input/output entry point
  sample.json       # two bundled input records
```

Run it from the class directory:

```sh
uv run --locked python -m report_app
```

Expected data: `{"count": 2, "mean": 3.0, "name": "class-02", "total": 6.0}`. JSON key ordering is not the behavior being assessed.

[The monolithic starter](practice/monolithic_report.py) and [messy function](practice/messy_summary.py) are practice inputs. Work on copies in a separate scratch folder; do not overwrite the supplied teaching package or `.venv`. The messy input is intentionally outside the clean example's quality checks.

## Everyday checks and references

```sh
uv run --locked ruff check report_app solutions tests
uv run --locked ruff format --check report_app solutions tests
uv run --locked python -m unittest discover -s tests -v
```

The last command is an instructor behavior check, not this week's pytest lesson. Testing and Git workflows are taught in class 03. [Instructor notes](INSTRUCTOR.md) record verification and facilitation guidance.

Exercises have IDs such as `02.1.E1` or `02.5.H1`. Write in the answer cell; reveal a reference by uncommenting `%load` in its **separate** cell. Loading reveals source, then a second run executes it. Untouched Run All leaves references commented. Terminal instructions in reference files are comments: they do not install packages, write projects, or create environments automatically.

Completion evidence is a runnable module layout, a recreated environment, readable code, and a README another person can follow. You must be able to explain and modify any AI-assisted work.

## Illustrations

Three local Creative Commons illustrations are embedded at the relevant teaching points. Keep the `images/` folder with the notebooks. [Sources, credits, alternative text, and teaching notes](IMAGE_SUGGESTIONS.md) identify the exact license or CC0 dedication for each image.

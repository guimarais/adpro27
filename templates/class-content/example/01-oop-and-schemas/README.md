# Class 01 — OOP and schemas: format specimen

Open [01-oop-and-schemas.ipynb](01-oop-and-schemas.ipynb). This short, runnable specimen demonstrates the content template; it is not the completed five-hour first class. The complete weekly structure is in the [copyable template](../../NN-topic/NN-topic.ipynb).

## Prerequisites

You should know Python variables, functions, lists, dictionaries, and loops. No Git, model account, GPU, or live data service is needed.

Install [VS Code](https://code.visualstudio.com/) with Microsoft's **Python** (`ms-python.python`) and **Jupyter** (`ms-toolsai.jupyter`) extensions, [uv](https://docs.astral.sh/uv/getting-started/installation/), and Python 3.11 or newer. Download the **whole `templates/class-content` directory**, preserving its subdirectories. The [shared environment](../../pyproject.toml) supplies `ipykernel` and Pydantic; its lockfile fixes the resolved dependencies. The first setup downloads those packages. After installation, the specimen works offline.

## Open in VS Code

Open a terminal **in this `01-oop-and-schemas` directory** and run:

```sh
uv sync --project ../.. --locked --no-dev
```

1. In VS Code, choose **File → Open Workspace from File…** and open [01-oop-and-schemas.code-workspace](01-oop-and-schemas.code-workspace). This makes the numbered class directory the workspace root. Install the recommended Python and Jupyter extensions if prompted.
2. Open `01-oop-and-schemas.ipynb`. Use **Select Kernel → Select Another Kernel… → Python Environments** and select the shared `.venv` in `templates/class-content`, two directories above this class. The workspace supplies that default interpreter location, but VS Code may remember a previous notebook kernel.
3. Run the first code cell. Check its printed interpreter path and local-file check, then use **Run All**. Keep solutions commented until you choose to reveal them.

If the shared environment is absent from the picker, run this command from the class directory:

```sh
uv run --project ../.. --locked --no-dev python -c "import sys; print(sys.executable)"
```

Copy the path it prints. In VS Code's Command Palette, use **Python: Select Interpreter → Enter interpreter path…**, then return to the notebook kernel picker and choose that environment. The terminal's interpreter and the notebook kernel are separate selections.

If the setup check reports the wrong directory, reopen the supplied workspace and restart the notebook kernel. The notebook does not silently change paths. No browser notebook server is required. See [VS Code notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) and [kernel selection](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management).

These are copyable launch instructions for week 01. The course explains environments and uv in week 02.

## Supporting material

- [Record schema and report class](examples/records.py)
- [Saved input records](fixtures/observations.json)
- [Reference solutions](solutions/)
- [Behavior checks](tests/test_records.py)

Attempt an exercise in its answer cell. To reveal the reference, uncomment `%load` in the separate solution cell and run it. Loading reveals source; running the populated cell is a second action. Your answer cell remains intact. Restarting the kernel does not remove loaded source.

From this same directory, run the behavior checks with:

```sh
uv run --project ../.. --locked python -m unittest discover -s tests -v
```

The sample exercise times are illustrative. The full template budgets 90 class minutes and 210 independent minutes. The assessed project is additional and designed separately by the instructor.

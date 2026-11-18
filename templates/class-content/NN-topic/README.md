# Class NN — {{CLASS_TITLE}}

Start with [the lesson](NN-topic.ipynb). It contains the learning outcomes, timetable, three interim exercises, independent work, and completion checks. See the [authoring guide](../AUTHORING.md) before adapting this template.

## Prerequisites and preparation

- Basic Python programming.
- {{CLASS_PREREQUISITES}}
- Complete the lesson's preparation before class; its time is included in the 210-minute independent-work allowance.

## Open the copyable template in VS Code

Install [VS Code](https://code.visualstudio.com/), its Microsoft **Python** (`ms-python.python`) and **Jupyter** (`ms-toolsai.jupyter`) extensions, [uv](https://docs.astral.sh/uv/getting-started/installation/), and Python 3.11 or newer. From **this `NN-topic` directory**, run:

```sh
uv sync --project .. --locked --no-dev
```

In VS Code, use **File → Open Workspace from File…** to open [NN-topic.code-workspace](NN-topic.code-workspace). It opens this class folder as the workspace root and recommends the required extensions. Open `NN-topic.ipynb` and use **Select Kernel → Select Another Kernel… → Python Environments** to choose the shared `.venv` one directory above this class. VS Code remembers a previous kernel, so confirm the selection rather than relying on the display name alone.

If the environment is not listed, run `uv run --project .. --locked --no-dev python -c "import sys; print(sys.executable)"` in this directory. Copy the printed path, use **Python: Select Interpreter → Enter interpreter path…** in the Command Palette, then return to the notebook's kernel picker and choose that environment. Selecting the terminal interpreter alone does not select the notebook kernel.

Run the setup cell, check the printed kernel path, then use the notebook toolbar's **Run All**. The workspace keeps relative `examples/` and `solutions/` paths rooted here. No JupyterLab server is needed. See [VS Code's notebook guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

## Before publishing a copied class

Replace this section and the template setup command with **{{CLASS_ENVIRONMENT_AND_RUN_INSTRUCTIONS}}**. Rename the workspace to match the class and update its `python.defaultInterpreterPath` to the selected uv environment (use a directory path for portability). Declare dependencies and supply the matching lockfile. Keep the numbered class folder as the workspace root; do not assume global packages are installed on student machines.

No Git commands are required for classes 01 or 02. Students can download the complete folder and follow the supplied commands.

## Supporting files

- [Reusable demonstration](examples/summary.py): import it from the notebook.
- [Reference solutions](solutions/): revealed through the notebook's commented `%load` cells.
- Add `exercises/` for script-based student tasks, `tests/` for meaningful checks, and `fixtures/` for saved data when needed. Notebook answer cells are sufficient for short tasks.

## Solutions

Attempt the exercise first. In its **separate solution cell**, uncomment the `%load` line and run the cell to reveal the source. Inspect it, then run the populated cell separately to execute the example. Do not put the loader in your answer cell: loading can replace the cell that invoked it.

Solutions are downloadable reference material. An untouched **Run All** leaves them unrevealed. After you load one, its source stays in your notebook even if you restart the kernel or clear outputs.

The core block is five hours, including class and preparation. The instructor-managed project is additional workload; extensions are optional.

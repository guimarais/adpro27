# Class 01 — Object-oriented programming and schemas

How do we keep related behavior understandable and stop invalid data entering a program? This block develops a small report over labelled, nonnegative quantities. You need basic Python variables, functions, loops, lists, and dictionaries; no pandas, Git, API key, local model, or GPU is needed.

## Read in this order

| File | In class (minutes) | Independent (minutes) | Focus |
| --- | --- | --- | --- |
| Preparation and VS Code setup | 0 | 30 | Follow the setup instructions below |
| [01.1 — Objects and state](01.1-objects-and-state.ipynb) | 30 | 15 | Instances, attributes, constructors, and separate mutable state |
| [01.2 — Behavior and composition](01.2-behavior-and-composition.ipynb) | 30 | 15 | Functions/methods, composition, brief inheritance and polymorphism |
| [01.3 — Schemas and validation](01.3-schemas-and-validation.ipynb) | 30 | 15 | Type hints, constraints, validation errors, coercion, and strictness |
| [01.4 — Serialization and JSON Schema](01.4-serialization-and-json-schema.ipynb) | 0 | 45 | Instance data, JSON, round trips, and contracts |
| [01.5 — Practice and review](01.5-practice-and-review.ipynb) | 0 | 90 | Validate a dataset, extend the model, and check behavior |
| **Total required** | **90** | **210** | **Five hours, including setup** |

Parts 01.1–01.3 introduce the initial material in class. Their guided follow-ups supply 45 minutes of reading. The 45 minutes in 01.4 include its exercise and reflection; the 90 minutes in 01.5 include all checks and review. Do not add those durations again. Optional extensions are excluded. The instructor's separately designed course project is **additional workload**.

Read in order to build understanding, but execute each file independently: every notebook includes its own imports, small definitions, and inputs. Use **Restart Kernel**, then **Run All** when starting a different part. Definitions are repeated deliberately for this first block; week 02 develops project/module organization.

## Preparation and VS Code setup — 30 minutes

1. Download the **complete `01-oop-and-schemas` folder**, including `solutions/`, `fixtures/`, the workspace, and the dependency files.
2. Install [VS Code](https://code.visualstudio.com/), Microsoft's **Python** (`ms-python.python`) and **Jupyter** (`ms-toolsai.jupyter`) extensions, [uv](https://docs.astral.sh/uv/getting-started/installation/), and Python 3.11 or newer. No Git knowledge is required.
3. Open a terminal in this class folder and install its environment:

   ```sh
   uv sync --locked --no-dev
   ```

4. In VS Code choose **File → Open Workspace from File…** and open [01-oop-and-schemas.code-workspace](01-oop-and-schemas.code-workspace). It opens only this class folder and recommends the two extensions.
5. Open part 01.1. Choose **Select Kernel → Select Another Kernel… → Python Environments**, then this class's `.venv`. Confirm the notebook kernel even if the terminal already uses the intended interpreter.
6. Run the setup cell. It prints the actual interpreter path and checks the local solution path. Continue with **Run All**. No browser notebook server is needed.

If the environment is not listed, run this in the class terminal:

```sh
uv run --locked --no-dev python -c "import sys; print(sys.executable)"
```

Copy that path into **Python: Select Interpreter → Enter interpreter path…** in the Command Palette, then return to the notebook kernel picker and choose the same environment. VS Code remembers older choices; the workspace default does not override an existing selection automatically.

If a notebook reports missing local paths, reopen the supplied workspace and restart its kernel. The notebook never silently changes directories or edits `sys.path`. Initial installation requires network access; the lesson activities then use local data and work offline. [VS Code notebook guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), [kernel selection](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management).

## Exercises and references

Exercise `01.2.E1` belongs to lesson `01.2`; independent exercise `01.5.H1` belongs to lesson `01.5`. Each highlighted card contains its time, goal, starting point, task, expected result, and hint.

Write your attempt in the answer cell. Its separate reference cell contains a commented command such as:

```python
# %load solutions/exercise_01_2_e1.py
```

After attempting the task, uncomment that line and run the cell to reveal source. Inspect it, then execute the populated cell separately. Loading can replace its invoking cell, so keep your answer separate. An untouched Run All leaves references hidden; after loading, the source remains in your notebook even if you clear outputs or restart the kernel. Solutions are downloadable reference material.

The [saved practice records](fixtures/observations.json) are included. [Instructor notes](INSTRUCTOR.md) explain facilitation and release checks. No earlier notebook or completed student answer is needed to run the reference solutions.

## Completion evidence

- A class whose instances have independent state.
- A justified choice of function or method and a brief explanation of composition.
- A validated record and an explanation of a rejected record.
- A distinction between type hints, instance JSON, and JSON Schema.
- A working validation/collection loop and meaningful checks of a small extension.

AI coding assistance is permitted. You remain responsible for explaining, testing, and making a small change to your work.

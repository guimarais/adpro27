## Why

Students can now represent and validate records, but need to organize that code into a project another person can run. Class 02 must connect modules, environments, dependencies, readability, and handover without assuming Git knowledge.

## What Changes

- Author five ordered VS Code notebooks, `02.1`–`02.5`, under `classes/02-reproducible-python-projects/`.
- Supply a complete local `report_app` package with ordinary imports, a module entry point, validated input, and predictable output.
- Explain venv/pip fundamentals, then use uv for project dependency declaration, locking, execution, and recreation.
- Teach naming, small functions, type hints, useful docstrings, Ruff, and a runnable README.
- Provide three interim exercises and independent practice with separate commented `%load` references.
- Keep each notebook independent of earlier kernel state; its supplied local modules are explicit learning assets.
- Verify the 90/210-minute allocation, fresh execution, references, package behavior, quality checks, and recreation in a fresh working copy.

## Capabilities

### New Capabilities

- `class-02-content`: Complete teaching materials for reproducible, maintainable Python projects.

### Modified Capabilities

None in the accepted main spec tree. This change builds on the existing unarchived template/class-01 changes and extends their shared verifier to discover class 02. Existing GUI-check limitations remain explicit.

## Impact

Adds the class-02 distribution, its uv environment, runnable package, references, and instructor notes. Updates course navigation and the shared release checker. Git instruction remains in class 03. This change does not create a new project assessment or require a browser notebook server.

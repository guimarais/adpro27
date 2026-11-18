## Context

The agreed first block is OOP and schemas, taught to students with basic Python knowledge. The user approved five ordered notebooks, independent fresh-kernel execution, lesson-specific exercise IDs, and the existing Report/Observation example. VS Code desktop with the Python/Jupyter extensions is the supported environment.

`add-course-content-template` exists as an unarchived change, with its VS Code GUI checks pending. No accepted specs exist in `openspec/specs/`. This new capability therefore uses ADDED requirements and records its dependency rather than pretending to modify an accepted capability.

## Goals / Non-Goals

### Goals

- Deliver the complete first block as readable, runnable teaching materials.
- Make the reading order explicit without creating execution dependencies between notebooks.
- Teach applied OOP, data validation, and external data contracts at a beginner-appropriate depth.
- Make setup, exercise checks, reference solutions, and workload explicit.
- Reuse the established VS Code, uv, exercise-card, and clean-release conventions.

### Non-Goals

- Authoring the other five weekly blocks or the assessed project.
- A notebook generator, provider framework, new teaching dependency stack, or advanced OOP catalog.
- Access-controlled solutions or live network/model requirements.
- Claiming headless execution is a VS Code frontend test.

## Decisions

### Ordered notebooks and class-level navigation

Use these filenames in `classes/01-oop-and-schemas/`:

1. `01.1-objects-and-state.ipynb`
2. `01.2-behavior-and-composition.ipynb`
3. `01.3-schemas-and-validation.ipynb`
4. `01.4-serialization-and-json-schema.ipynb`
5. `01.5-practice-and-review.ipynb`

The README is the entry point, reading index, and authoritative workload table. Every notebook links to the index and its neighbors and states what it assumes. One class-level `01-oop-and-schemas.code-workspace` opens the class directory as the kernel working directory.

### Independent execution with small repeated definitions

Each notebook includes the imports, small Report/Observation definitions, and example data it uses. The first two parts begin with plain dictionaries and a Report class; the third introduces validated Observation objects. Later parts recap the complete required definitions. This deliberate repetition makes each file useful in isolation and keeps week-01 imports simple. Week 02 can later turn the repeated application ideas into modules.

Reference `.py` files also supply their own setup and do not depend on student attempts. The practice notebook uses a small included JSON fixture, explicitly documented in its setup. No notebook imports another notebook, loads an earlier solution automatically, changes directories, or modifies `sys.path`.

### Workload allocation

| Activity | In class | Independent |
| --- | --- | --- |
| Preparation and VS Code setup | 0 | 30 |
| 01.1 | 30 | 15 |
| 01.2 | 30 | 15 |
| 01.3 | 30 | 15 |
| 01.4 | 0 | 45 |
| 01.5 | 0 | 90 |
| Total | 90 | 210 |

Parts 01.1–01.3 each have a 20-minute teaching/demo portion and a ten-minute interim exercise. Their 15-minute follow-ups make up the 45-minute guided-reading allocation. Part 01.4 includes reading/demos, a 15-minute contract exercise, and review inside its 45 minutes. Part 01.5 has practice tasks of 35, 35, and 20 minutes, including checks/reflection. Optional extensions and the separate project are excluded.

### Exercise and solution identities

Interim IDs are `01.1.E1`, `01.2.E1`, and `01.3.E1`. Independent exercises are `01.4.H1` and `01.5.H1`–`01.5.H3`. Filenames replace dots with underscores and lowercase the exercise suffix: `solutions/exercise_01_2_e1.py`.

Use the established exercise/answer/loader metadata tags, with the full ID. Keep the exact commented `%load` pattern and keep attempts separate. Do not execute a reference during an untouched Run All. Legacy single-notebook template IDs remain valid in that template; lesson IDs and exercise IDs are distinct in the new materials.

### Depth and data contracts

Use one main Report class and the Observation schema. Include a short provided inheritance/polymorphism demonstration in 01.2's follow-up, not an inheritance-heavy application design. Explain mutable state, composition, function-versus-method choices, type hints versus runtime validation, expected validation failures, coercion, one strict-field example, serialization versus schema, and schema limits.

Keep numeric examples as nonnegative quantities rather than implying all measurements must be nonnegative. Catch expected validation errors explicitly. Use no pandas, APIs, models, or unfamiliar domain mathematics.

### Environment and verification

The class owns its `pyproject.toml`, `uv.lock`, and `.venv`; students can download just the complete class folder. Runtime dependencies are ipykernel and Pydantic. Standard notebook checking/export tools are development dependencies.

Extend the existing template checker rather than create a second framework. It recognizes both the original single-notebook convention and ordered class parts, checks the shared class workspace, aggregates schedules/IDs at class level, and executes every notebook in a fresh kernel. Verify reference solutions in separate fresh namespaces and test the IPython `%load` replacement payload independently of GUI claims. Keep release outputs empty and counts null.

## Risks / Trade-offs

- Repeated short definitions can drift → keep each part's version explicit and verify its observable results; do not claim the files share hidden state.
- Exercise and lesson numbers could collide → use `.E`/`.H` exercise suffixes and full IDs consistently.
- A shared checker could break the existing template → retain its single-notebook checks and rerun template/specimen regression verification.
- Apparent workload can exceed the budget if reading is counted twice → use the README table and include task checks/review inside each allocation.
- Desktop VS Code cannot be driven by the current UI tools → record GUI checks as pending; do not relabel protocol checks as GUI verification.

## Migration Plan

Add the actual class beside the template and historical notebooks. Link it from the course blueprint and authoring guide. Relax the open template change's single-notebook-only wording to permit the approved multipart variant. Preserve its original specimen and existing GUI-check status.

## Open Questions

No curriculum decisions remain after the user's confirmation. Actual VS Code visual and reveal interaction checks require access to the desktop editor and will remain explicitly pending if unavailable.

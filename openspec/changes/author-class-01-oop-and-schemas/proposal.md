## Why

Class 01 currently has a curriculum blueprint and a short format specimen, but no complete teaching materials. Students need a clearly ordered set of small lessons they can read and execute independently in VS Code.

## What Changes

- Author five notebooks under `classes/01-oop-and-schemas/`, ordered `01.1` through `01.5`.
- Cover objects/state, behavior/composition, schemas/validation, serialization/JSON Schema, and practice/review.
- Make each notebook executable from a fresh kernel, with its own imports, small definitions, and local input. Repeat short teaching definitions deliberately rather than importing another notebook or requiring previous exercise answers.
- Continue the Report/Observation story, using local labelled numeric records and only Python/Pydantic.
- Use exercise IDs such as `01.2.E1` and `01.5.H1`, separate answer cells, and commented local `%load` reference cells.
- Supply a class-local uv environment, lockfile, VS Code workspace, reading index, and instructor notes.
- Extend the existing release checker to validate one class's ordered parts and aggregate workload, while executing each notebook independently.
- Preserve the 90-minute class and 210-minute independent-work budget, with the separately assessed project additional.

## Capabilities

### New Capabilities

- `class-01-content`: Complete, ordered and independently executable OOP/schema teaching materials for class 01.

### Modified Capabilities

None in the accepted main specification tree, which is currently empty. This change builds on the implemented portions of `add-course-content-template`; its still-open delta and authoring guidance will explicitly permit ordered lesson parts alongside the original single-notebook template. The existing VS Code GUI verification tasks remain separate and pending.

## Impact

Adds actual class materials under `classes/01-oop-and-schemas/`. Updates the course navigation, template authoring guidance, and release checker for multipart classes. It does not author weeks 02–06, alter historical materials, redesign the project, or claim unavailable VS Code GUI checks have passed.

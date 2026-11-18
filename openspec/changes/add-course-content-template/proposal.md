## Why

The redesigned course needs a repeatable authoring structure that makes teaching, independent work, exercises, and solutions easy to find. Existing notebooks use inconsistent numbering and exercise presentation; a common template will make the six new blocks coherent while retaining Python modules as the home for reusable application code.

## What Changes

- Define a reusable weekly-content template aligned with [COURSE_REDESIGN.md](../../../COURSE_REDESIGN.md).
- Use two-digit class numbering from `01` to `06`, including the main lesson filename.
- Combine a guided Jupyter lesson, Python examples/exercises/solutions, and a short Markdown entry point.
- Support VS Code desktop with a per-class workspace, Python/Jupyter extension recommendations, and explicit uv notebook-kernel selection.
- Give interim exercises prominent, portable highlights, stable identifiers, ten-minute allocations, hints, and observable completion criteria.
- Separate student answer cells from opt-in `%load` solution cells backed by local Python files.
- Include the complete weekly structure: outcomes, preparation, three class cycles, 210 minutes of independent work, completion checks, and optional extensions.
- Supply an authoring guide and a short worked `01` specimen demonstrating the conventions.
- Define verification of notebook structure, timing, links, solution paths, clean release state, and offline execution.

## Capabilities

### New Capabilities

- `course-content-template`: A consistent, reusable weekly lesson format, including numbered artifacts, exercise presentation, and on-demand file-backed solutions.

### Modified Capabilities

None. No accepted OpenSpec capabilities currently exist in this repository.

## Impact

- Implementation will add a template and a small specimen under `templates/class-content/`.
- The authoring guide will map the template to the agreed six-block sequence.
- Teaching notebooks run inside VS Code using its standard Python/Jupyter extensions and the uv environment's IPython kernel; students do not need a browser notebook server or a notebook-generation pipeline.
- Existing teaching materials, historical projects, and assessment policy remain source references for later authoring.
- This change specifies the template. Writing all six complete lessons and redesigning the assessed project are separate work.

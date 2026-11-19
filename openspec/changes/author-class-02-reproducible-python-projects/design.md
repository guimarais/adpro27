## Context

The agreed week-02 blueprint covers modules/entry points, venv/pip, uv manifests and lockfiles, readability, and reproducible handover. Students know basic Python and have studied OOP/schemas, but should not need earlier notebooks to run the new materials. VS Code is the supported editor.

## Goals / Non-Goals

### Goals

- Deliver five ordered, independently executable lesson notebooks and a complete local example.
- Make module imports, interpreter selection, and dependency state visible.
- Give students a minimal everyday uv and code-quality workflow.
- Keep required activity inside 90 class minutes plus 210 independent minutes.

### Non-Goals

- Git workflows, pytest instruction, package publication, build backends, complex CLI frameworks, or advanced static checking.
- Automatically installing packages, modifying source, or creating environments during notebook Run All or solution reveal.
- Treating a lockfile as a record of external datasets or model responses.

## Decisions

### Ordered parts

1. `02.1-modules-and-imports.ipynb`
2. `02.2-virtual-environments-and-pip.ipynb`
3. `02.3-uv-projects-and-lockfiles.ipynb`
4. `02.4-readable-code-and-documentation.ipynb`
5. `02.5-practice-and-handover.ipynb`

Use a class-root workspace, local uv environment, index, instructor guide, and lesson-prefixed exercise IDs. Each part imports its own needed names and explains the supplied local files; none depends on another notebook's execution or student answers.

### Real modules as the learning artifact

Supply `report_app` with record validation, a pure summary calculation, a Report class, local input data, and `__main__.py`. Run it with `uv run --locked python -m report_app`. Imports should define reusable behavior without automatically running the program. Use ordinary imports and a class-root working directory rather than `sys.path` workarounds.

The provided package replaces week-01's deliberate repeated teaching definitions with visible module boundaries. All required assets stay inside the complete class folder. A monolithic practice script provides the refactoring starting point; students work in a separate scratch copy.

### Environment teaching without notebook side effects

Show venv/pip commands for POSIX and Windows, using explicit interpreter paths so activation-policy changes are unnecessary. Use a separate scratch environment rather than overwriting the teaching `.venv`. Explain that uv-managed environments need not contain pip itself.

Use `uv init --bare --vcs none` for a disposable new-project exercise, then add Pydantic, inspect `pyproject.toml`/`uv.lock`, and run/sync the result. Package installation is an explicit student terminal action and can require network access. Default notebook execution and reference scripts only inspect local state and data.

### Quality and workload

Use Ruff as a development dependency, with a small configuration and separate lint/format commands. Explain readability, types, and docstrings through a small function. Keep deliberately messy practice code outside the clean example's quality checks.

| Activity | Class minutes | Independent minutes |
| --- | --- | --- |
| Preparation/layout/setup | 0 | 30 |
| 02.1 | 30 | 15 |
| 02.2 | 30 | 15 |
| 02.3 | 30 | 15 |
| 02.4 | 0 | 45 |
| 02.5 | 0 | 90 |

The independent mapping matches the blueprint: 30 preparation/reading; 75 refactoring (15 in 02.1 plus 60 in 02.5); 60 environment recreation (15 each in 02.2/02.3 plus 30 in 02.5); 45 quality/documentation. Exercise checks and reflection are included.

### Verification

Reuse the shared release checker for ordered notebooks, links, timing, clean loaders, and fresh execution. Add class-02 IDs and its first-reference probe. Check actual package behavior and CLI/import semantics using small standard-library tests, run Ruff, and recreate the application in a temporary fresh working copy using the lockfile/cache. Record desktop VS Code checks as pending if unavailable.

## Risks / Trade-offs

- Students may install into the wrong environment → explicit interpreter commands, visible kernel paths, and a separate scratch project.
- Notebook imports can cache edited modules → document restarting the kernel after source changes.
- Installation may require network access → make it an explicit terminal activity; keep default Run All and references local.
- Splitting too many tiny modules can obscure the program → use only boundaries with a clear role and show the full import flow.

## Migration Plan

Add the class alongside class 01, link it from the blueprint and authoring guide, and extend existing checks without changing the class-01 artifacts or their verification status.

## Open Questions

No curriculum decisions remain. Actual VS Code GUI checks require editor access and must be reported separately from automated checks.

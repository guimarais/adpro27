## Context

The agreed third block starts with Git and then teaches collaboration/testing. Students know basic Python, applied OOP/schemas, and reproducible modules/environments. The same five-part reading pattern, fresh-kernel execution, VS Code workspace, highlighted exercises, and local `%load` references continue.

## Goals / Non-Goals

### Goals

- Connect working tree, staging, commits, branches, remotes, and review to observable examples.
- Teach normal/failure assertions, pytest fixtures, parametrization, and a small monkeypatched input boundary.
- Provide a meaningful bug that tests actually detect and a review/conflict exercise requiring judgment.
- Preserve the 90/210-minute budget and offline default execution.
- Suggest process diagrams with verifiable Creative Commons attribution.

### Non-Goals

- Advanced Git graph theory, rebasing, destructive reset recovery, CI setup, or a full testing-framework catalog.
- Automatically mutating any Git repository, changing global identity, contacting GitHub, or revealing credentials during notebook/reference execution.
- Claiming an offline review packet is a real GitHub pull request or that kernel tests establish VS Code GUI behavior.

## Decisions

### Reading sequence

1. `03.1-git-basics.ipynb`
2. `03.2-branches-and-collaboration.ipynb`
3. `03.3-testing-behavior-with-pytest.ipynb`
4. `03.4-fixtures-and-parametrized-tests.ipynb`
5. `03.5-review-and-conflict-practice.ipynb`

Each part includes its own imports, recorded input or explicit local package assets, setup check, navigation, and exercise chains. A class-local uv project/workspace makes the full folder independently usable.

### Budget

| Activity | Class | Independent |
| --- | --- | --- |
| Preparation/Git/VS Code/account setup | 0 | 30 |
| 03.1 | 30 | 15 |
| 03.2 | 30 | 15 |
| 03.3 | 30 | 15 |
| 03.4 | 0 | 60 |
| 03.5 | 0 | 75 |

This matches 60 minutes Git preparation/practice, 45 review, 75 testing, and 30 failure/conflict diagnosis. Parts 03.1–03.3 each have 20 teaching plus ten exercise minutes. 03.4 includes 30 minutes reading/demos and a 30-minute exercise; 03.5 allocates 45 minutes review plus 30 diagnosis. Checks/reflection are included; the project remains additional.

### Git is explicit practice, not a notebook side effect

Use recorded status/diffs for default demonstrations. Students copy the small Git starter to a new folder outside the course checkout and configure identity locally. Teach inspect → stage explicit files → inspect staged diff → commit. Cover branches, local/remote distinction, fetch, push, fast-forward-only pull, and a GitHub PR guide. Use a prepared ordinary commit for revert and a local text conflict; avoid destructive reset instructions.

GitHub account/network actions are manual. If access is unavailable during class, draft a clearly labelled review packet using the provided patch; perform real PR work when access is available. Do not describe the offline packet as a published PR. Automated validation uses only disposable local repositories and a local bare remote.

### Test behavior and the input boundary

Reuse a complete local Report/Observation package, with a source module that reads bundled records. Provide passing tests under `tests/`. Put a deliberately wrong mean and two detecting tests under `practice/`; pytest's configured `testpaths` excludes them from the passing default suite. A notebook may run that explicit target, capture the expected failure, and explain it without failing Run All.

Fixtures create fresh observations; parametrization covers several cases without duplicated tests; pytest.raises checks expected invalid input; monkeypatch replaces the name used by a source loader and is restored after the test. No real API is needed, preparing the seam used in later API/AI blocks.

### Image suggestions

Keep third-party candidates as source links and metadata in `IMAGE_SUGGESTIONS.md`, with placements in the notebook narrative. Verify the individual file's license, author, and credit; do not infer image rights from Commons' structured-data footer. Include useful cautions where an older diagram uses checkout/reset terminology, GitLab calls a review a merge request, or a testing diagram depicts broader TDD. No downloaded image or remote embed is required for default learning.

### Verification

Extend the existing checker for the class-03 budget and IDs. Run notebooks fresh, references independently, the passing pytest suite, and seeded failure detection. Test init/stage/commit/branch/merge/revert/local-remote/conflict commands only in temporary repositories. Render/inspect static lessons and verify image source metadata. Keep desktop GUI checks pending when unavailable.

## Risks / Trade-offs

- Students may run Git in the wrong folder → explicit separate-repository instructions and recorded default demonstrations.
- Authentication can consume practice time → count setup within preparation and offer a labelled offline review packet during access problems.
- An intentionally broken example could look like a broken release → isolate it in practice and assert its expected failure; default pytest only collects passing tests.
- Images can teach unnecessary complexity → suggest a small shortlist, explain caveats, and retain text explanations without image/network requirements.

## Migration Plan

Add class 03 beside the earlier classes, link it from the blueprint, and extend shared verification without changing real Git history or earlier teaching content.

## Open Questions

No curriculum decisions remain. Actual VS Code GUI interaction must be checked separately when desktop access is available.

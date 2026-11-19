# Class 04 content review — 19 November 2026

Reviewed the complete new class-04 distribution, including untracked notebooks, modules, references, fixtures, dependency/workspace metadata, and teaching instructions. Published baseline: `04bd438633a9f06c14c136a1d34447bc8747a96e` (also HEAD at review time; no later commits). A tracked-only diff would omit this new folder, so the review treated its complete contents as additions. Unrelated working-tree changes were excluded.

Standards and specification were reviewed independently, then their findings were checked against the actual files. Standards sources: AGENTS.md, templates/class-content/AUTHORING.md, COURSE_REDESIGN.md, and PROJECT_STATUS.md. No CONTRIBUTING.md or CODING_STANDARDS.md was present. Specification source: openspec/changes/author-class-04-consuming-apis/specs/class-04-content/spec.md and its design, plus the user-approved simplification recorded in the blueprint.

## Standards

**One P3 setup finding, resolved.** AI_DEMOS.md described `read -r -s -p` as POSIX-shell syntax even though those prompt options require Bash. This can fail under dash or zsh. The instructions now explicitly say Bash, tell other-shell users to start Bash first, and add a newline after the non-echoing prompt. The corrected prompt was checked with harmless supplied input, without credentials or a live API call. The independent reviewer confirmed resolution.

No remaining hard authoring-standard breaches or actionable code-smell findings. Repeated notebook setup checks are intentional self-containment; acquisition and validation wrappers have explicit teaching responsibilities. The existing model, exercise triples, commented loaders, saved/live labels, and honest pending desktop checks fit the documented standards.

## Spec

**Zero confirmed violations.** The materials match the five-part sequence, 90/210-minute allocation, supplied FastAPI backend, minimal synchronous Requests client, whole-load validation, useful failure handling, public-data mapping, and two AI HTTP previews. Default execution is offline. Pagination/retry implementation and new server development remain optional. No blocking scope or behavior error was found.

**One reference-completeness improvement, completed.** Exercise 04.4.H1 asks students to set a population value to None and explain rejection. Its reference previously showed only the successful mapping and a comment about missing values. The reference now reloads the fixture independently, introduces None, checks the adapter's expected ValueError, and explicitly fails if the invalid input is accepted. The independent reviewer confirmed it now covers the full prompt.

## Image review

Added [three Creative Commons diagram suggestions](IMAGE_SUGGESTIONS.md), following class 03's source-link format, with placements, proposed alternative text, ready credits, individual source/license links, and teaching caveats. Notebook placement notes link to the guide. Request/response, HTTP response parts, and the API boundary are the selected concepts; no new required activity is introduced.

Source-page/creator/license verification passed. Direct candidate downloads returned HTTP 429 and the UI inventory exposed neither browsers nor native apps. No local image assets were added, and rendered image suitability/legibility is not claimed. The guide explicitly requires visual inspection before embedding a chosen copy. Existing explanatory text remains sufficient without those images or network access.

## Verification after corrections

- All 15 default behavior tests passed. The updated public-data reference ran independently and demonstrated the expected missing-value rejection.
- Ruff lint and format checks passed for all 19 Python files.
- All five notebooks and six references passed fresh-kernel shared verification with real Requests session calls blocked. Navigation, local links, 90/210-minute allocations, six exercise chains, clean outputs/counts/loaders, and the separate `%load` execution protocol passed.
- The Bash prompt accepted only harmless test input; no real credential was read and no AI request was made.
- Actual browser preview review and VS Code desktop interactions remain pending. Earlier localhost/public smoke-test evidence is retained in the instructor record; it was not represented as a new live check during this content review.

Review totals: **Standards 1 P3 finding, corrected; Spec 0 confirmed violations.** No unresolved content finding remains. Visual/editor and delivery checks remain separate.

[Class index](README.md) · [Instructor evidence](INSTRUCTOR.md) · [Diagram suggestions](IMAGE_SUGGESTIONS.md)

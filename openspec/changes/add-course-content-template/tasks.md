# Execution status — 19 November 2026

Implementation and automated/static checks are complete; VS Code desktop tasks 5.4–5.5 remain open. The template/specimen was published in `11dc49e`; shared class-discovery/environment updates were published in `04bd438`. See [project execution status](../../../PROJECT_STATUS.md) for the cross-course progress and legacy-content rule. Keep this change open until its pending desktop tasks pass.

## 1. Establish the authoring layout

- [x] 1.1 Add `templates/class-content/AUTHORING.md` with the notebook/Python/Markdown responsibilities and the six class-number/slug mappings.
- [x] 1.2 Add the copyable `NN-topic` directory and document placeholder replacement, optional supporting directories, and matching notebook filenames.
- [x] 1.3 Add the template README and matching VS Code workspace with navigation, prerequisites, kernel selection, extension recommendations, and the class-directory working convention.

## 2. Build the weekly notebook template

- [x] 2.1 Create a valid Python notebook with outcomes, preparation, six timed class intervals, independent work, completion checks, reflection, extensions, and references.
- [x] 2.2 Allocate exactly 90 class minutes and 210 independent minutes; mark project workload as separate and extensions as optional.
- [x] 2.3 Add three prominent interim exercise cards and at least one independent exercise card with the required fields, IDs, metadata, and answer cells.
- [x] 2.4 Keep reusable example logic in supporting Python files and use notebook cells only for explanation, small demonstrations, and practice.

## 3. Add file-backed solution loading

- [x] 3.1 Add a local `.py` reference solution for every template exercise and document the classroom/independent filename mapping.
- [x] 3.2 Add separate commented `%load` cells with matching IDs/tags, plus reveal/inspect/execute instructions that preserve student attempts.
- [x] 3.3 Include explanations and expected results in solution files; document comment-only solutions for terminal/prose exercises.
- [x] 3.4 Add the visible working-directory/path check and clear recovery instructions without changing directories or modifying `sys.path`.
- [x] 3.5 Document release cleanup of both cell source and outputs after testing `%load`.

## 4. Provide the short class-01 specimen

- [x] 4.1 Create the clearly labeled `example/01-oop-and-schemas` specimen with a resolved README and a small runnable class/schema example.
- [x] 4.2 Demonstrate one complete interim exercise chain and one independent exercise chain, including real solution files and expected results.
- [x] 4.3 Declare the specimen's minimal uv environment and verify that its week-01 launch instructions require no prior Git knowledge.
- [x] 4.4 Confirm that the specimen illustrates the format without being presented as the completed five-hour first class.

## 5. Verify and document the deliverable

- [x] 5.1 Validate nbformat, numbering, VS Code workspace configuration, exercise IDs/tags, timing totals, relative links, existing solution paths, and absence of unreplaced placeholders in the specimen.
- [x] 5.2 Inspect release cell source: loaders stay commented, outputs are empty, execution counts are null, and no loaded solutions, credentials, or machine-specific paths remain.
- [x] 5.3 Execute the untouched template and specimen from fresh kernels using the documented environment, without live services; confirm blank exercise cells do not break Run All.
- [ ] 5.4 On a temporary notebook copy, verify `%load` in VS Code's notebook editor: it reveals source separately from execution and preserves the student answer cell. Pending desktop UI access; kernel payload and installed extension handler checks are separate evidence.
- [ ] 5.5 Visually inspect exercise highlights and required/optional labels in VS Code's notebook editor and a static preview; verify their meaning remains clear without color. Static preview already reviewed; VS Code GUI check pending.
- [x] 5.6 Record the supported frontend, environment, commands, and results in the authoring guide; verify existing teaching materials are preserved.


## 6. Course-wide review follow-up — 20 November 2026

- [x] 6.1 Clarify template/specimen versus class-local environments and each README's exact dev/no-dev setup command; document offline PNG/Mermaid authoring and licensing.
- [x] 6.2 Recheck the template/specimen and all authored classes with the shared verifier and real HTTP blocked. Preserve the separate pending actual desktop/frontend tasks.

- [x] 6.3 Record publication of the revised guidance/verifier in `705efd3`, pushed to `origin/main` on 20 November 2026.

- [x] 6.4 Add a minimal root README linking to each of the six class guides; statically verify all six targets exist and appear once in course order. Published in `3b9173b`, pushed to `origin/main` on 20 November 2026 after the user's explicit request; no new execution or delivery check claimed.

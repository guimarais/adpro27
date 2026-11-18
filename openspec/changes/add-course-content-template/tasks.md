## 1. Establish the authoring layout

- [ ] 1.1 Add `templates/class-content/AUTHORING.md` with the notebook/Python/Markdown responsibilities and the six class-number/slug mappings.
- [ ] 1.2 Add the copyable `NN-topic` directory and document placeholder replacement, optional supporting directories, and matching notebook filenames.
- [ ] 1.3 Add the template README with navigation, prerequisites, dependency/run-instruction placeholders, and the class-directory launch convention.

## 2. Build the weekly notebook template

- [ ] 2.1 Create a valid Python notebook with outcomes, preparation, six timed class intervals, independent work, completion checks, reflection, extensions, and references.
- [ ] 2.2 Allocate exactly 90 class minutes and 210 independent minutes; mark project workload as separate and extensions as optional.
- [ ] 2.3 Add three prominent interim exercise cards and at least one independent exercise card with the required fields, IDs, metadata, and answer cells.
- [ ] 2.4 Keep reusable example logic in supporting Python files and use notebook cells only for explanation, small demonstrations, and practice.

## 3. Add file-backed solution loading

- [ ] 3.1 Add a local `.py` reference solution for every template exercise and document the classroom/independent filename mapping.
- [ ] 3.2 Add separate commented `%load` cells with matching IDs/tags, plus reveal/inspect/execute instructions that preserve student attempts.
- [ ] 3.3 Include explanations and expected results in solution files; document comment-only solutions for terminal/prose exercises.
- [ ] 3.4 Add the visible working-directory/path check and clear recovery instructions without changing directories or modifying `sys.path`.
- [ ] 3.5 Document release cleanup of both cell source and outputs after testing `%load`.

## 4. Provide the short class-01 specimen

- [ ] 4.1 Create the clearly labeled `example/01-oop-and-schemas` specimen with a resolved README and a small runnable class/schema example.
- [ ] 4.2 Demonstrate one complete interim exercise chain and one independent exercise chain, including real solution files and expected results.
- [ ] 4.3 Declare the specimen's minimal uv environment and verify that its week-01 launch instructions require no prior Git knowledge.
- [ ] 4.4 Confirm that the specimen illustrates the format without being presented as the completed five-hour first class.

## 5. Verify and document the deliverable

- [ ] 5.1 Validate nbformat, numbering, exercise IDs/tags, timing totals, relative links, existing solution paths, and absence of unreplaced placeholders in the specimen.
- [ ] 5.2 Inspect release cell source: loaders stay commented, outputs are empty, execution counts are null, and no loaded solutions, credentials, or machine-specific paths remain.
- [ ] 5.3 Execute the untouched template and specimen from fresh kernels using the documented environment, without live services; confirm blank exercise cells do not break Run All.
- [ ] 5.4 On a temporary notebook copy, verify `%load` in a supported Jupyter frontend: it reveals source separately from execution and preserves the student answer cell.
- [ ] 5.5 Visually inspect exercise highlights and required/optional labels in the live notebook and a static preview; verify their meaning remains clear without color.
- [ ] 5.6 Record the supported frontend, environment, commands, and results in the authoring guide; verify existing teaching materials are preserved.

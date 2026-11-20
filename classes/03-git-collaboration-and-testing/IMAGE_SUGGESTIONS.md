# Creative Commons images for class 03

This guide records four embedded local visuals below and three third-party source candidates. No remote image request is needed to execute a notebook. The suggestions link to the original file pages so students can inspect the creator, license, and accessible file variants. File-specific creator/license information was checked on **19 November 2026**; Wikimedia's general page-footer license is not the image license.

| Process and placement | Suggested image and creator | File license | Teaching purpose and caveat |
| --- | --- | --- | --- |
| 03.1, before the staging demo; revisit in 03.2 | [Git data flow simplified](https://commons.wikimedia.org/wiki/File:Git_data_flow_simplified.svg), **Cmglee** | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) | Connect working files, index, local repository, and remote. Trace only `add`, `commit`, `fetch`, and `push` initially. Some commands use older terminology; the class uses `switch` for branch switching. |
| 03.2, branch → review → merge discussion | [Basic git branching workflow (GitLab)](https://commons.wikimedia.org/wiki/File:Basic_git_branching_workflow_(GitLab).png), **TheresNoTime** | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Show work on a branch returning to a shared line. Explain that GitLab calls the review a merge request while this course uses GitHub pull requests; product interfaces differ. |
| 03.3, after observing the intentional failing test | [Test-driven development](https://commons.wikimedia.org/wiki/File:Test-driven_development.svg), **Excirial; vector derivative by Jarozwj** | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) | Discuss the cycle of seeing failure, making a small change, and checking again. This depicts the broader TDD approach; the class requires behavior-focused tests, not mastery of that whole methodology. |

## Suggested alternative text

1. “Git data moves from working files to the staging index, into local commits, and between local and remote repositories through explicit operations.” Follow with a plain-text explanation of the two diffs; arrows alone do not explain staged versus unstaged edits.
2. “A feature branch diverges from the shared branch; its change is reviewed and merged back.” Name the source and target branches in the surrounding text.
3. “A short development cycle links a failing test, a change that makes it pass, and improvement while keeping tests passing.” Explain that a collection error is different from an assertion exposing the intended bug.

## Ready-to-use credits for unchanged copies

- “[Git data flow simplified](https://commons.wikimedia.org/wiki/File:Git_data_flow_simplified.svg)” by Cmglee, via Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Unchanged.
- “[Basic git branching workflow (GitLab)](https://commons.wikimedia.org/wiki/File:Basic_git_branching_workflow_(GitLab).png)” by TheresNoTime, via Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Unchanged.
- “[Test-driven development](https://commons.wikimedia.org/wiki/File:Test-driven_development.svg)” by Excirial, vector derivative by Jarozwj, via Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Unchanged.

If a later author crops, translates, recolors, or redraws one of these works, replace “Unchanged” with an accurate change note and follow the linked license's attribution and ShareAlike terms for the adaptation. Keep the image credit next to the illustration or in a clearly linked credits section; the repository's software license does not replace these file licenses. A notebook can also use an original text/table explanation instead of an image.


## Local visual additions — 20 November 2026

These visuals explain existing material inside its allocated reading/demo time. They add no required task or minutes. Each notebook includes a caption, meaningful alternative text, and a nearby credit. Local PNGs display offline without Mermaid support; `.mmd` files preserve editable sources.

| Part | Local image | Teaching purpose | Source/license |
| --- | --- | --- | --- |
| 03.1 | [Locate the version being recorded](images/git-data-flow.png) | Read from the working directory upward: add stages a selected version, commit records the index locally, and push sends commits remotely. Trace those three arrows first. The picture also includes commands outside this lesson; its older checkout labels do not replace the course's switch commands. Editing after add leaves a newer unstaged version. | [Cmglee](https://commons.wikimedia.org/wiki/File:Git_data_flow_simplified.svg); [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); unchanged Commons rendering |
| 03.2 | [Separate a local branch from hosted review](images/branches-and-review.png) | A local branch names commits. Push sends its commits to a remote branch; opening a pull request is a separate action. Fetch refreshes local remote-tracking references and does not integrate your working branch. | Original; [Mermaid source](images/branches-and-review.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 03.3 | [Keep the requirement fixed while correcting code](images/behavior-test-cycle.png) | Arrange known inputs, call the function, then assert the required result. An assertion exposing the seeded bug is useful evidence; a collection error means setup must be repaired first. Rerunning the same expectation checks the correction. | Original; [Mermaid source](images/behavior-test-cycle.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 03.4 | [Replace the input; exercise the real behavior](images/replace-input-boundary.png) | The fixture replaces only read_payload at the name used by the loader. Validation and summarize stay real. Use fresh inputs so a change in one test cannot leak into another. | Original; [Mermaid source](images/replace-input-boundary.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

Original diagrams: ADPRO course contributors, 2026, released under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/), covering the Mermaid sources and their PNG renderings. They are newly authored diagrams of this course's code, not adaptations of the external illustrations. Keep this attribution and license link when reusing them, and identify later changes. External files retain their individual licenses; the repository's software license does not replace them.

External creator/license/source pages were rechecked on 20 November 2026; Wikimedia's page-footer license is not the image license. Download URLs:

- [Locate the version being recorded: selected PNG](https://thumb.wikimedia.org/wikipedia/commons/thumb/4/44/Git_data_flow_simplified.svg/960px-Git_data_flow_simplified.svg.png)

For future edits, render the corresponding `.mmd` with Mermaid CLI to the same PNG filename (white background, scale 2), then inspect the actual image and exported notebook before release. Rendering is author-only; students need no JavaScript packages. See the course authoring guide for the rendering command and verification distinctions.

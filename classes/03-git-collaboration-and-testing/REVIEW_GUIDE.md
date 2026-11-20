# A small review workflow

Work in a separate practice repository that you own or that the instructor supplies. Never point the exercise at the original course repository's remote. No notebook or reference file sends code to GitHub automatically.

## Online route: a real pull request

1. Prepare access to your own/classroom GitHub repository. For a new Git-starter repository, create an **empty** GitHub repository without a generated README/license, configure its actual URL as `origin`, and publish the initial baseline with `git push -u origin main`. The target branch must exist remotely before the PR. For an existing classroom repository, clone its supplied baseline and work from that history instead of attaching an unrelated local history. Account/authentication setup belongs to the 30-minute preparation allocation; never put credentials in tracked files.
2. Start a small branch from the agreed baseline, make one coherent change, and inspect/test it.
3. Push **that branch** to the intended remote. In GitHub, choose the correct base and comparison branches and open the pull request. A branch on your computer is not itself a published PR.
4. Describe the problem and resulting behavior, with a small before/after example where useful. State the checks run and any expected limitation.
5. Ask the assigned peer to read the diff, run the checks, and give specific feedback. Respond by explaining or improving the change; rerun the relevant tests.
6. Merge only through the course's agreed process once review is resolved. Fetch/integrate the resulting baseline deliberately.

GitHub documents the current [create-PR flow](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request). The button label is less important than selecting the right base and head and explaining the change.

## Offline route: a review packet

If access is unavailable during 03.2, include your branch diff (`git diff main...HEAD`) and commit summary (`git log --oneline main..HEAD`) in the written packet. For 03.5, use [the supplied patch](practice/review/change.patch). This is an **offline review packet**, not a published GitHub PR. Record the base behavior, proposed change, findings, test evidence, and recommendation. Exchange it with the assigned peer locally or through the normal course channel; if working alone, label the author response as simulated. This packet gives provisional completion only. Use the first 15 minutes of 03.5.H1's existing 45-minute allocation to publish/review the actual PR, or inspect/respond to its review if already published. If access remains unavailable, do the 30-minute regression-review portion now, reserve the remaining 15 minutes for an instructor-arranged later access session, and keep hosted completion pending. Record the PR URL, source/base branches, and actual peer feedback; a simulated author response does not establish hosted peer review.

## What to review

- Does the change preserve the documented input/empty-data contract?
- Do its tests expose the possible regression, rather than just repeat its calculation?
- Are unrelated files, generated environments, or credentials included?
- Are the names, function boundaries, and run instructions understandable?

Use one actionable paragraph per finding: identify the location, explain the consequence, and suggest a concrete correction/check. For example: “Returning 0 for an empty mean makes absence look like an observed average. Keep None and add a regression case for empty input.”

The example patch changes the empty mean to zero. Do not change an assertion merely to match the regression. The appropriate review asks for a correction and evidence that the original contract still works.

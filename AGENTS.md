# Course authoring

Read [PROJECT_STATUS.md](PROJECT_STATUS.md) before continuing implementation; it records completed blocks, evidence, and outstanding work. Use [COURSE_REDESIGN.md](COURSE_REDESIGN.md) for the agreed curriculum and [the authoring guide](templates/class-content/AUTHORING.md) when creating or editing lessons.

## Legacy content

Never track legacy content unless it is actually reused in this redesigned course. The root legacy directories are listed in the legacy section of [.gitignore](.gitignore). An inventory entry, reference link, or possible future use does not count as reuse.

When reusing material, prefer copying only the needed files into the relevant active class directory, adapting them to the lesson, and recording their source and any license/attribution requirements. Leave the remaining legacy files untracked and intact. Stage explicit active-project paths; review the staged file list before committing.

## Execution records

After implementation or verification, update PROJECT_STATUS.md and the relevant OpenSpec tasks with the actual result. Keep implementation, automated/static verification, desktop verification, and publication distinct. Leave unavailable checks pending; a static preview or kernel protocol check does not complete a VS Code desktop check.

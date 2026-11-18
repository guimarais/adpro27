## ADDED Requirements

### Requirement: Reusable weekly content artifacts

The implementation SHALL provide a reusable class-content template, an authoring guide, and a short filled class-01 specimen under `templates/class-content/`. The lesson narrative SHALL be a Jupyter notebook, reusable application code SHALL live in Python files, and a Markdown README SHALL provide navigation and launch/setup instructions.

#### Scenario: Author starts a new block
- **WHEN** an author follows the authoring guide
- **THEN** the author can copy a documented template, locate the lesson and supporting files, and identify which placeholders must be replaced
- **AND** the author is not required to install a custom notebook extension or generate the notebook from another source format

#### Scenario: Reader follows the entry point
- **WHEN** a reader opens the class README
- **THEN** the reader finds the lesson, its prerequisites, launch instructions, and links to supporting code without duplicated full lesson prose

### Requirement: Two-digit class numbering

An instantiated class directory SHALL begin with a two-digit class number from `01` through `06`, followed by the documented topic slug. A single-notebook class SHALL use the same stem for its main notebook. A multipart class SHALL retain that directory and use ordered notebook stems such as `01.1-topic`, `01.2-topic`, with an index defining reading order. The literal reusable template SHALL use explicit `NN` and `topic` placeholders. Lesson and exercise IDs SHALL remain distinguishable.

#### Scenario: First two classes are instantiated
- **WHEN** an author creates the OOP block and reproducible-projects block
- **THEN** their directories are `01-oop-and-schemas` and `02-reproducible-python-projects`
- **AND** their main notebooks are `01-oop-and-schemas.ipynb` and `02-reproducible-python-projects.ipynb`

### Requirement: VS Code notebook workflow

Each class SHALL provide a `.code-workspace` file with the same stem as its class directory. It SHALL open only the numbered class directory, recommend Microsoft's Python and Jupyter extensions, define that directory as the notebook working directory, and provide a portable default uv interpreter location. The README SHALL explain environment installation, opening the workspace in VS Code desktop, explicitly selecting the notebook kernel, and recovery when that environment is missing from the picker. Student runtime dependencies SHALL NOT require JupyterLab or another browser notebook server.

#### Scenario: Student opens a class in VS Code
- **WHEN** a student follows the class README and opens its workspace file
- **THEN** the numbered class directory is the workspace root
- **AND** the student can select the uv environment as the notebook kernel and confirm it using the setup cell's printed interpreter path
- **AND** local imports and solution paths resolve from that class directory

#### Scenario: VS Code remembers another interpreter
- **WHEN** the previously selected notebook kernel differs from the supplied uv environment
- **THEN** the instructions show how to obtain the intended interpreter path and select it explicitly
- **AND** they distinguish the terminal interpreter from the notebook kernel

### Requirement: Complete weekly learning structure

The template SHALL include the class purpose, learning outcomes, prerequisites, preparation, class agenda, teaching segments, interim exercises, guided independent work, completion checks, reflection, optional extensions, and references. It SHALL distinguish in-class, independent, and optional content in visible text. It SHALL follow the six-block order in `COURSE_REDESIGN.md`, with Git basics beginning week `03`.

#### Scenario: Student identifies what to do
- **WHEN** a student reads the block
- **THEN** the student can distinguish what happens in class, what is required independently, and what is optional
- **AND** the student can find an observable completion check for required activity

### Requirement: Explicit weekly time budgets

The generic template SHALL allocate exactly 90 class minutes as three 20-minute teaching segments followed by three ten-minute exercises. It SHALL include an independent-work table totaling 210 minutes, including preparation and independent exercise time. It SHALL identify project work as additional instructor-managed workload and exclude optional extensions from required totals.

#### Scenario: Author reviews the timetable
- **WHEN** the template's required activity durations are summed
- **THEN** the class intervals are `0–20`, `20–30`, `30–50`, `50–60`, `60–80`, and `80–90`
- **AND** independent work totals 210 minutes without counting setup or exercise time twice
- **AND** the separate project has no template-imposed assignments or rubric

### Requirement: Highlighted interim exercises

Every interim exercise SHALL have a prominent Markdown heading containing the word `Exercise`, its stable ID, and its title. A portable callout SHALL include its class/independent classification, duration, goal, starting point, task, observable completion criterion, and hint. The highlight SHALL remain understandable without color, custom CSS, or editor-specific admonitions.

#### Scenario: Exercise is viewed outside the live notebook
- **WHEN** a learner views the notebook in a static notebook preview
- **THEN** the exercise remains visually distinct from explanatory prose
- **AND** its identity, task, time estimate, and completion criterion remain readable

### Requirement: Stable exercise identities

For the original single-notebook template, the three interim exercise IDs SHALL be `<class>.1`, `<class>.2`, and `<class>.3`; independent IDs SHALL use `<class>.H1`, `<class>.H2`, and subsequent numbers. In multipart classes, IDs SHALL instead include the lesson and explicit exercise type, such as `01.2.E1` and `01.5.H1`; solution filenames SHALL replace dots with underscores and lowercase the exercise suffix. Exercise IDs SHALL be unique within a class and map consistently to local solution filenames. Prompt, answer, and loader cells SHALL carry the same `exercise_id` metadata value and the respective `exercise`, `exercise-answer`, and `solution-loader` tags.

#### Scenario: Class two contains classroom and independent work
- **WHEN** class `02` is instantiated
- **THEN** its interim exercise IDs are `02.1`, `02.2`, and `02.3`
- **AND** its first independent exercise is `02.H1`
- **AND** the corresponding solution paths follow `solutions/exercise_02_1.py` and `solutions/exercise_02_h1.py`

### Requirement: Separate attempts and file-backed solutions

Every exercise SHALL provide student answer space separately from its solution-loader cell. Each solution loader SHALL reference an existing local `.py` solution file. Reference solutions SHALL include explanatory comments and any relevant expected result, and SHALL work from documented setup without depending on unfinished student answers. Terminal-only or prose solutions SHALL use Python comments rather than automatically executing shell commands.

#### Scenario: Student reveals a solution after an attempt
- **WHEN** a student uses the solution loader
- **THEN** the student's answer cell remains unchanged
- **AND** the loaded reference includes an explanation of the result

#### Scenario: Student loads a Git exercise solution
- **WHEN** a Git exercise's solution file is loaded and then its comment-only cell is executed
- **THEN** the learner sees the command sequence and explanation
- **AND** no repository-modifying shell commands run automatically

### Requirement: Opt-in IPython solution loading

Distributed solution-loader cells SHALL contain a commented `%load solutions/<filename>.py` command plus concise reveal instructions. Instructions SHALL explain that students uncomment and run the loader to inspect source, then separately execute the populated cell when appropriate. The authoring guide SHALL document that `%load` can replace its invoking cell and that downloaded solution files are reference material rather than confidential content.

#### Scenario: Untouched notebook is run in full
- **WHEN** a student uses Run All on an unmodified distributed notebook
- **THEN** the solution-loader cells remain comments
- **AND** no reference solution is revealed or executed

#### Scenario: Student opts into a reference solution
- **WHEN** a student uncomments and runs the documented `%load` line in VS Code's notebook editor using the supplied IPython kernel
- **THEN** the referenced source becomes available in the loader cell for inspection
- **AND** loading alone does not execute that Python solution

### Requirement: Predictable solution path resolution

The README SHALL document opening the numbered class workspace in VS Code to establish the kernel's working directory. The notebook SHALL include a visible setup check for the required local solution path, print the active interpreter path, and give actionable workspace/kernel recovery instructions if the path is missing. The solution workflow SHALL NOT silently change the working directory, mutate `sys.path`, or download solution source from a remote URL.

#### Scenario: Notebook starts from the documented directory
- **WHEN** the student follows the launch instructions
- **THEN** the setup check succeeds and each relative solution path resolves

#### Scenario: Editor starts the kernel from another directory
- **WHEN** the required class-relative solution directory is absent
- **THEN** the setup check explains the expected launch directory and recovery steps
- **AND** it does not silently change global notebook state

### Requirement: Clean and valid notebook releases

Distributed notebooks SHALL be valid nbformat documents with Python kernel metadata, empty outputs, and null code-cell execution counts. Every tagged solution-loader cell SHALL contain only its documented commented loader/instructions, with no previously loaded solution body. The authoring guide SHALL explain that clearing outputs and restarting the kernel do not remove loaded source.

#### Scenario: Instructor prepares a notebook after testing a solution
- **WHEN** the instructor prepares the student release
- **THEN** the original commented loader source is restored as well as cleared outputs and execution counts
- **AND** no instructor machine paths or credentials appear in the released notebook

### Requirement: Offline execution and accessible practice

The unmodified generic template and worked specimen SHALL execute from a fresh kernel using their documented environment without purchased API access, a GPU, a running local model, or a live external API. Empty student answer cells SHALL NOT cause Run All to fail. Live-service and optional activities SHALL be clearly marked and disabled by default.

#### Scenario: Student has no model access
- **WHEN** the student runs the supplied default notebook
- **THEN** examples use local fixtures or replay data where external responses are needed
- **AND** the student can attempt the required exercise flow without model credentials

### Requirement: Demonstrated authoring and verification workflow

The authoring guide SHALL explain copying/renaming a block and its workspace, replacing placeholders, allocating time, creating exercise/solution pairs, and preparing a clean release. The short `01` specimen SHALL demonstrate a runnable example, an interim prompt/answer/loader/solution chain, and an independent exercise chain while identifying itself as a format demonstration. Verification SHALL cover notebook format, numbering, workspace configuration, timing, local links/paths, exercise metadata, clean solution source, offline Run All, visual presentation, and an actual `%load` reveal in VS Code's notebook editor on a temporary copy. Headless and source-inspection checks SHALL be distinguished from actual VS Code GUI verification.

#### Scenario: Author verifies the completed template
- **WHEN** the author follows the documented verification process
- **THEN** the structural and execution checks pass
- **AND** the exercise highlight and solution interaction are checked in VS Code's notebook editor
- **AND** the distributed copy still contains commented loaders and empty outputs

### Requirement: Additive introduction of the template

Implementation SHALL add the template and specimen alongside existing teaching materials. It SHALL preserve the current and historical notebooks and project briefs. Adopting the template for all six finished classes SHALL be separate from creating the template.

#### Scenario: Template change is implemented
- **WHEN** the new template and specimen are added
- **THEN** existing course materials remain available
- **AND** the new artifacts do not claim that all six redesigned lessons or the assessed project have been authored

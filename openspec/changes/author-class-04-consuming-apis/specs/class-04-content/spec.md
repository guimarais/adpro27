## ADDED Requirements

### Requirement: Ordered class-four distribution

The class SHALL provide five ordered 04.1–04.5 notebooks, a complete local package, six independent references, a VS Code workspace, and a class-local uv manifest/lockfile. Each notebook SHALL run fresh without earlier answers or external services.

#### Scenario: Student starts with the public-data notebook
- **WHEN** part 04.4 is run in the installed class workspace
- **THEN** its local imports and saved mapping work without running parts 04.1–04.3

### Requirement: Simple architecture and supplied backend

Part 04.1 SHALL explain frontend, backend, HTTP API, client/server, localhost, request/response components, and one query parameter. The class SHALL supply a tiny FastAPI observations endpoint and explicit two-terminal server/client instructions. Building a new server SHALL remain optional.

#### Scenario: Student changes the label parameter
- **WHEN** the supplied service is running and label=north is requested
- **THEN** the response contains only the north observation with value 2.5
- **AND** an unknown label returns a successful empty list

### Requirement: Validated synchronous consumption

The required client SHALL use Requests with an explicit timeout, status checking, JSON decoding, and full-list Pydantic validation. It SHALL preserve the existing Observation(label, value) contract and reject the complete load if any record is invalid. Network acquisition SHALL NOT happen in constructors or imports.

#### Scenario: One row is missing its value
- **WHEN** a successful JSON body containing that row is loaded
- **THEN** the client raises an explained schema failure and does not return partial results

### Requirement: Distinct and actionable failures

The client SHALL distinguish connection/timeout, HTTP status, invalid JSON, and invalid records, retaining original causes. The deterministic suite SHALL exercise normal and failure behavior while replacing only external acquisition. It SHALL NOT require a running server or external API.

#### Scenario: An HTTP error contains HTML
- **WHEN** the client receives HTTP 503 with an HTML body
- **THEN** status checking reports HTTP 503 before attempting successful-body JSON parsing

### Requirement: Small public-data mapping

The class SHALL integrate a key-free World Bank request for Portugal/Spain population in one fixed year, retain a real saved response with provenance/attribution, and map ISO/year to label and population in persons to value. Missing values and multi-page results SHALL NOT be silently accepted as zero or complete data.

#### Scenario: Public service access is unavailable
- **WHEN** the student uses the saved response
- **THEN** the mapping remains runnable and the result is labelled saved-response evidence rather than a live request

### Requirement: OpenAI and Ollama HTTP previews

The class SHALL show short instructor demonstrations of OpenAI Responses and local Ollama generate using explicit POST JSON bodies, timeouts, status checking, and relevant authentication/configuration. Both SHALL default to clearly labelled illustrative saved envelopes. Live calls SHALL require an explicit switch and environment configuration; required work SHALL NOT require credentials, model installation, downloads, SDKs, or GPU access.

#### Scenario: AI demos run without credentials
- **WHEN** their default commands run with outbound calls forbidden
- **THEN** both return saved envelopes without reading secrets or claiming live model results

### Requirement: Approved simple scope and complete workload

The class SHALL allocate 90 classroom minutes and 210 independent minutes including setup, exercises, checks, and reflection. Preparation SHALL be 30 independent minutes; parts 1–3 SHALL each allocate 30 classroom and 15 independent minutes; parts 4 and 5 SHALL allocate 60 and 75 independent minutes. Pagination, retry implementation, and new backend development SHALL be optional, within a separate 180-minute ceiling. Six exercise chains SHALL use highlighted prompts, separate attempts, and exact commented local loaders.

#### Scenario: Student totals required work
- **WHEN** the index allocations are summed
- **THEN** they total five hours without adding setup or completion checks a second time

### Requirement: Honest verification and release state

Verification SHALL cover clean notebooks, paths, timing, fresh kernels, independent references, offline failure tests, seeded regression detection, local/public smoke tests, static presentation, and earlier-class regressions. Actual VS Code desktop checks SHALL be recorded separately and remain pending when unavailable. Publication SHALL only be recorded after it occurs.

#### Scenario: Only kernel and static checks are available
- **WHEN** verification is recorded
- **THEN** those checks do not mark desktop reveal/rendering complete


### Requirement: Offline teaching illustrations

The approved course-wide review SHALL be reflected in local teaching illustrations
(4 in this class), captions, meaningful alternative text, and source/license
records. Reused images SHALL retain file-specific credits and licenses. Original
course-specific diagrams SHALL retain editable Mermaid sources and CC BY 4.0
credits, alongside local PNG renderings. Images SHALL explain existing concepts
within the unchanged workload; their display SHALL NOT require network access or
a student-installed renderer.

#### Scenario: Student opens the complete class folder offline
- **WHEN** a notebook displays a teaching illustration
- **THEN** it reads the bundled PNG and supplies a textual explanation and credit
- **AND** editable source and license information are available locally or through the source guide

# Illustrations for class 05

Local images explain the supplied application. Keep the complete `images/` folder with the notebooks.


## Local visual additions — 20 November 2026

These visuals explain existing material inside its allocated reading/demo time. They add no required task or minutes. Each notebook includes a caption, meaningful alternative text, and a nearby credit. Local PNGs display offline without Mermaid support; `.mmd` files preserve editable sources.

| Part | Local image | Teaching purpose | Source/license |
| --- | --- | --- | --- |
| 05.1 | [The model proposes; Python controls](images/model-and-application.png) | A proposed call is data. Python decides whether the name and arguments are allowed, executes a permitted function, and validates the final answer. A schema-valid answer string can still make a false numeric claim; compare it with actual tool results. | Original; [Mermaid source](images/model-and-application.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 05.2 | [Link the proposal and result](images/linked-tool-round-trip.png) | Use the same call_id for the proposed function call and its returned result. Arguments arrive as JSON text; Python validates them before execution. This sequence represents a successful replay or live flow, not a network action performed by the picture. | Original; [Mermaid source](images/linked-tool-round-trip.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 05.3 | [Count proposals separately from executions](images/requests-and-executions.png) | In the repeated-call replay, requests 1 and 2 each lead to an execution. Request 3 proposes another call, but Python stops before executing it. The final counters are three requests and two executions; there is no fourth request. | Original; [Mermaid source](images/requests-and-executions.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 05.4 | [Locate the first failed boundary](images/failure-layers.png) | An unknown name and invalid arguments stop before a tool runs. A valid missing-country lookup can return an empty list. A malformed final answer fails a later boundary. Diagnose the responsible layer rather than treating every case as a prompt problem. | Original; [Mermaid source](images/failure-layers.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 05.5 | [Match the claim to its evidence](images/evidence-types.png) | Replay exercises the real application with authored responses. Mocked SDK transport checks request/response integration. Only a live evaluation observes the selected model's behavior on that date; none of these alone proves broad answer quality. | Original; [Mermaid source](images/evidence-types.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

Original diagrams: ADPRO course contributors, 2026, released under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/), covering the Mermaid sources and their PNG renderings. They are newly authored diagrams of this course's code, not adaptations of the external illustrations. Keep this attribution and license link when reusing them, and identify later changes. External files retain their individual licenses; the repository's software license does not replace them.


For future edits, render the corresponding `.mmd` with Mermaid CLI to the same PNG filename (white background, scale 2), then inspect the actual image and exported notebook before release. Rendering is author-only; students need no JavaScript packages. See the course authoring guide for the rendering command and verification distinctions.

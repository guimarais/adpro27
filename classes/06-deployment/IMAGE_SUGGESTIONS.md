# Illustrations for class 06

Local images explain the supplied application. Keep the complete `images/` folder with the notebooks.


## Local visual additions — 20 November 2026

These visuals explain existing material inside its allocated reading/demo time. They add no required task or minutes. Each notebook includes a caption, meaningful alternative text, and a nearby credit. Local PNGs display offline without Mermaid support; `.mmd` files preserve editable sources.

| Part | Local image | Teaching purpose | Source/license |
| --- | --- | --- | --- |
| 06.1 | [Locate the Python process](images/thin-app-architecture.png) | The browser displays the interface; Streamlit runs Python on the server. The UI calls supplied modules over saved observations. A local browser URL is not a public deployment. AI remains disabled on the required public path. | Original; [Mermaid source](images/thin-app-architecture.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 06.2 | [Copy contents into the student repository root](images/student-repository-root.png) | The course keeps this class nested under classes/06-deployment. Your separate student repository puts the class contents at its root, including hidden workflow/configuration files. Exclude environments, caches, and real secrets. | Original; [Mermaid source](images/student-repository-root.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 06.3 | [One push, two independent paths](images/independent-ci-and-hosting.png) | Actions and Community Cloud observe the repository through separate mechanisms. A passing check does not establish the hosted version, and a red check does not itself block automatic hosting updates. Verify the commit/run and visible release independently. | Original; [Mermaid source](images/independent-ci-and-hosting.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 06.5 | [Keep secrets on the server](images/server-secret-boundary.png) | The required public app works with AI disabled. Optional private live AI reads server-side secrets; credentials stay out of Git, browser output, notebooks, and diagnostic messages. A per-session limit is not a global spend cap. | Original; [Mermaid source](images/server-secret-boundary.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 06.5 | [Localhost belongs to the machine running Python](images/local-and-remote-localhost.png) | A local Python client can reach laptop Ollama through laptop localhost. In a hosted Python process, localhost points to the hosting machine. The same string does not create a connection back to the laptop; required hosting needs no Ollama. | Original; [Mermaid source](images/local-and-remote-localhost.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

Original diagrams: ADPRO course contributors, 2026, released under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/), covering the Mermaid sources and their PNG renderings. They are newly authored diagrams of this course's code, not adaptations of the external illustrations. Keep this attribution and license link when reusing them, and identify later changes. External files retain their individual licenses; the repository's software license does not replace them.


For future edits, render the corresponding `.mmd` with Mermaid CLI to the same PNG filename (white background, scale 2), then inspect the actual image and exported notebook before release. Rendering is author-only; students need no JavaScript packages. See the course authoring guide for the rendering command and verification distinctions.

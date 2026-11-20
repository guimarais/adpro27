# Creative Commons image suggestions for class 04

**20 November update:** the client/server asset is now downloaded and embedded, together with three original Mermaid diagrams. The table below retains earlier candidates; the local inventory later in this file identifies the selected assets. Visual and automated results are recorded separately in INSTRUCTOR.md and OpenSpec task 4.5.

These optional diagrams follow the class-03 suggestion format: source links, teaching placements, alternative text, and ready-to-use credits. No remote images are embedded and no image request is needed for notebook execution. Discussion replaces part of the existing explanation time; it adds no required activity or topic.

Individual file pages, creators, and licenses were checked on **19 November 2026**. Wikimedia's general metadata/footer license is not the image's license. The candidates below have explicit Creative Commons licenses. The original candidates were suggestions: direct downloads returned HTTP 429 on 19 November. The selected client/server download succeeded on 20 November; the other two candidates remain unembedded. No claim is made about their appearance in VS Code. Visually check a selected copy before including it in a teaching release.

## Placement and purpose

| Process and placement | Suggested image and creator | File license | Teaching use and limits |
| --- | --- | --- | --- |
| 04.1, after the frontend/backend request-flow explanation | [Client-server model](https://commons.wikimedia.org/wiki/File:Client-server_model.svg), **Lubaochuan** | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Trace a client request and server response. Identify the notebook/Requests client and supplied FastAPI backend. Explain that these roles can run on the same laptop: the diagram does not require two physical machines or an internet connection. |
| 04.2, alongside request → status → JSON → validation | [HTTP response message format](https://commons.wikimedia.org/wiki/File:Prj5-responseHeader.png), **Satishgavali; response derivative by Frostyandy2k** | [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/) | Distinguish a response's status line, headers, and body before extracting JSON. This is an older HTTP/1-style message illustration, not a packet layout to implement or the wire representation of every HTTP version. Requests handles protocol framing; JSON is one possible body format and still needs schema validation. Prefer the notebook's own field table if the diagram's labels distract beginners. |
| 04.4, before comparing the local-service and World Bank adapters; briefly revisit for the AI previews | [API in context](https://commons.wikimedia.org/wiki/File:20261024_API.svg), **RCraig09** | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Connect a client application to capabilities exposed through an API. Locate the request/response boundary and then point to our external-to-internal mapping. Treat the API as an interface exposed by the service, not an extra physical machine every application needs. The provider's response contract still determines the mapping; the illustration does not imply that the World Bank and AI APIs share a JSON schema. |

## Suggested alternative text and captions

1. **Alternative text:** “A client initiates a request and receives a response from a server.” **Caption:** In this class, Requests is the client and FastAPI handles the request. Both can run locally; an API client does not have to be a browser.
2. **Alternative text:** “An HTTP response is divided into a status line, header fields, and an optional message body.” **Caption:** Check HTTP status before decoding the body. Successful JSON decoding does not establish that the records satisfy the Observation schema. Explain these parts in text even when the picture is shown.
3. **Alternative text:** “An application exchanges requests and results with a service through its API.” **Caption:** Keep the service's external representation at the adapter boundary. Our summary calculation continues to receive validated Observation objects.

These are proposed descriptions to check against the selected rendered copy before embedding it. The existing notebook text/tables explain each point without relying on color, tiny labels, or an available image host.

## Ready-to-use credits for unchanged copies

- “[Client-server model](https://commons.wikimedia.org/wiki/File:Client-server_model.svg)” by Lubaochuan, via Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Unchanged copy.
- “[HTTP response message format](https://commons.wikimedia.org/wiki/File:Prj5-responseHeader.png)” by Satishgavali, response derivative by Frostyandy2k, via Wikimedia Commons, [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/). Unchanged copy of the existing response derivative; the source page documents its alteration from the request-message illustration.
- “[API in context](https://commons.wikimedia.org/wiki/File:20261024_API.svg)” by RCraig09, via Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Unchanged copy.

If a later author crops, translates, recolors, or redraws a candidate, replace the unchanged-copy note with the actual changes and follow its attribution/ShareAlike terms. Keep the creator, original file-page link, and license beside the reused image or in clearly linked credits. The repository's software license does not replace these file licenses. Keep any downloaded transparent diagrams readable on a white display background, without silently changing their source artwork.

## Selection notes

Start with the client/server diagram. Add the API-context diagram only if students need help transferring that idea to another provider. The response-format illustration is optional support; the class does not teach raw HTTP framing. No stock image is needed for an authentication header, timeout, or validation error: the small real code and saved failure cases are more precise.

MCP belongs after ordinary tool calling in class 05, as discussed in the course planning conversation. An MCP architecture diagram would introduce additional roles at the wrong point in class 04, so it is not included here.

[Class index](README.md) · [Instructor notes](INSTRUCTOR.md)


## Local visual additions — 20 November 2026

These visuals explain existing material inside its allocated reading/demo time. They add no required task or minutes. Each notebook includes a caption, meaningful alternative text, and a nearby credit. Local PNGs display offline without Mermaid support; `.mmd` files preserve editable sources.

| Part | Local image | Teaching purpose | Source/license |
| --- | --- | --- | --- |
| 04.1 | [Identify roles before machines](images/client-server.png) | Requests is our client; FastAPI is the supplied server. They can run on the same laptop. The client initiates a request and receives a response; it need not be a browser. Keep the server terminal running while using the client terminal. | [Lubaochuan](https://commons.wikimedia.org/wiki/File:Client-server_model.svg); [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); unchanged Commons rendering |
| 04.2 | [A successful status is only one boundary](images/client-failure-boundaries.png) | First the request must return within its timeout; then check status, decode JSON, and validate records. Success at one stage does not imply success at the next. Keep failures distinct from a valid empty result. | Original; [Mermaid source](images/client-failure-boundaries.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 04.4 | [Keep provider details at the adapter](images/world-bank-mapping.png) | Map countryiso3code and date into the label and population into value, in persons. The summary still consumes Observation objects. Check expected identities separately: a shape-valid row does not establish completeness or truth. | Original; [Mermaid source](images/world-bank-mapping.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 04.5 | [Separate deterministic checks from service evidence](images/offline-and-live-evidence.png) | Known saved/fake responses test application behavior repeatably. A separate explicit smoke check tests service reachability and today's contract. Neither result silently substitutes for the other. | Original; [Mermaid source](images/offline-and-live-evidence.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

Original diagrams: ADPRO course contributors, 2026, released under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/), covering the Mermaid sources and their PNG renderings. They are newly authored diagrams of this course's code, not adaptations of the external illustrations. Keep this attribution and license link when reusing them, and identify later changes. External files retain their individual licenses; the repository's software license does not replace them.

External creator/license/source pages were rechecked on 20 November 2026; Wikimedia's page-footer license is not the image license. Download URLs:

- [Identify roles before machines: selected PNG](https://thumb.wikimedia.org/wikipedia/commons/thumb/6/69/Client-server_model.svg/1280px-Client-server_model.svg.png)

For future edits, render the corresponding `.mmd` with Mermaid CLI to the same PNG filename (white background, scale 2), then inspect the actual image and exported notebook before release. Rendering is author-only; students need no JavaScript packages. See the course authoring guide for the rendering command and verification distinctions.

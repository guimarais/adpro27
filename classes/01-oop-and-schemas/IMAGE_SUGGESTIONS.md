# Creative Commons illustrations for class 01

Six illustrations are included as local PNGs (three reused illustrations and three original Mermaid diagrams) in the lesson notebooks, with alternative text, short teaching captions, and nearby credits. Download the complete class folder, including `images/`, to keep them available offline. No network request or extra code cell is needed to display them. Their discussion fits inside the existing reading/demo time; the workload and exercises are unchanged.

Creators and individual licenses were checked against the linked sources on **19 November 2026**. Wikimedia's general metadata/footer license is not the image license. Where a work offers several licenses, the CC option below is the one used for this copy. CC0 is a public-domain dedication, distinguished from attribution licenses.

## Placement and purpose

| Placement | Local image | Creator | License or dedication |
| --- | --- | --- | --- |
| 01.1, before constructing and changing two reports | [CPT-OOP-objects and classes](images/objects-and-classes.png) | Pluke | [CC0 1.0 Universal dedication](https://creativecommons.org/publicdomain/zero/1.0/) |
| 01.2, before discussing methods that read or change state | [ProgrammingObject](images/object-state-and-methods.png) | chris (Wikimedia user Chrkl) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| 01.4, immediately before the JSON round-trip example | [Serialization](images/serialization.png) | Trustable | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |

## Sources, captions, and credits

### CPT-OOP-objects and classes

The class defines a common structure; each constructed object has its own identity and state. Treat the cars as a simple analogy, then return to two Report instances and compare their separate records lists. The picture does not establish how Python stores those lists.

**Alternative text:** One car class is shown beside three named example objects: polo, mini, and beetle.

**Credit:** “[CPT-OOP-objects and classes](https://commons.wikimedia.org/wiki/File:CPT-OOP-objects_and_classes.svg)” by Pluke, [CC0 1.0 Universal dedication](https://creativecommons.org/publicdomain/zero/1.0/). Commons-rendered PNG; no content changes.

### ProgrammingObject

Attributes describe current state; methods provide operations on an object. In this lesson, Report.add changes collected state while total and summary read it; the exercise adds a mean. The device is an analogy: a Python method need not change state, and this picture does not enforce private access.

**Alternative text:** An object is drawn as a device with attribute displays and three method controls.

**Credit:** “[ProgrammingObject](https://commons.wikimedia.org/wiki/File:ProgrammingObject.svg)” by chris (Wikimedia user Chrkl), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Commons-rendered PNG; no content changes.

### Serialization

Serialization represents data for storage or transfer; deserialization reconstructs data. Here model_dump_json returns JSON text, not bytes; encoding is a separate step when bytes are required. The round trip creates a new validated Observation, rather than preserving the original object identity. The database and memory branches are context, not extra tasks.

**Alternative text:** Serialization turns an object into a byte stream for storage or transfer; deserialization reconstructs an object from a stream.

**Credit:** “[Serialization](https://commons.wikimedia.org/wiki/File:Serialization.png)” by Trustable, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Commons-rendered PNG; no content changes.

## Reuse and presentation

Keep the source, creator, and license links with reused illustrations. If you crop, translate, recolor, or otherwise adapt an image, describe the changes and follow its linked license, including ShareAlike where applicable. CC0 does not require attribution; this course retains a provenance credit. These image terms are separate from the repository's software license.

Transparent diagrams are displayed on a white background so their black text/arrows remain readable across editor themes; the image files themselves are unchanged. The adjacent text explains the teaching point without relying on color or on reading every label in the picture. The numbered notebook sequence, exercise IDs, and commented `%load` solution cells are preserved.

[Class index](README.md) · [Instructor notes](INSTRUCTOR.md)


## Local visual additions — 20 November 2026

These visuals explain existing material inside its allocated reading/demo time. They add no required task or minutes. Each notebook includes a caption, meaningful alternative text, and a nearby credit. Local PNGs display offline without Mermaid support; `.mmd` files preserve editable sources.

| Part | Local image | Teaching purpose | Source/license |
| --- | --- | --- | --- |
| 01.1 | [Trace state ownership](images/independent-state.png) | Each constructor creates a separate records list. An alias to left still refers to left; adding through that alias cannot change right. | Original; [Mermaid source](images/independent-state.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 01.3 | [Accept, convert, or reject](images/validation-outcomes.png) | The same Observation contract accepts a number, converts a numeric string by default, and rejects invalid text. The later strict-field example changes conversion policy; type hints alone perform none of these checks. | Original; [Mermaid source](images/validation-outcomes.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 01.4 | [Follow one record through its representations](images/record-representations.png) | An instance stores one validated observation. A dictionary and JSON text represent that observation. JSON Schema describes allowed records and is generated from the model class, rather than from the north record. | Original; [Mermaid source](images/record-representations.mmd); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

Original diagrams: ADPRO course contributors, 2026, released under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/), covering the Mermaid sources and their PNG renderings. They are newly authored diagrams of this course's code, not adaptations of the external illustrations. Keep this attribution and license link when reusing them, and identify later changes. External files retain their individual licenses; the repository's software license does not replace them.


For future edits, render the corresponding `.mmd` with Mermaid CLI to the same PNG filename (white background, scale 2), then inspect the actual image and exported notebook before release. Rendering is author-only; students need no JavaScript packages. See the course authoring guide for the rendering command and verification distinctions.

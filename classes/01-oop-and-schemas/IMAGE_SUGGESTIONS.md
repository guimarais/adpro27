# Creative Commons illustrations for class 01

Three illustrations are included as local PNGs in the lesson notebooks, with alternative text, short teaching captions, and nearby credits. Download the complete class folder, including `images/`, to keep them available offline. No network request or extra code cell is needed to display them. Their discussion fits inside the existing reading/demo time; the workload and exercises are unchanged.

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

Attributes describe current state; methods provide operations on an object. In this lesson, Report.add changes collected state while total and mean read it. The device is an analogy: a Python method need not change state, and this picture does not enforce private access.

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

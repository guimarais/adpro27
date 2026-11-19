# Creative Commons illustrations for class 02

Three illustrations are included as local PNGs in the lesson notebooks, with alternative text, short teaching captions, and nearby credits. Download the complete class folder, including `images/`, to keep them available offline. No network request or extra code cell is needed to display them. Their discussion fits inside the existing reading/demo time; the workload and exercises are unchanged.

Creators and individual licenses were checked against the linked sources on **19 November 2026**. Wikimedia's general metadata/footer license is not the image license. Where a work offers several licenses, the CC option below is the one used for this copy. CC0 is a public-domain dedication, distinguished from attribution licenses.

## Placement and purpose

| Placement | Local image | Creator | License or dedication |
| --- | --- | --- | --- |
| 02.1, between the package demonstration and dotted-import explanation | [Modular approach code reuse](images/module-reuse.png) | Kayau | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| 02.2, after inspecting interpreter/package paths; revisit during 02.3 lockfile discussion | [Virtual environments diagram, Building Better Research Software](images/virtual-environments.png) | Building Better Research Software lesson authors (Carpentries Incubator) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| 02.5, before the refactoring task and preservation-of-behavior discussion | [Modular approach path](images/problem-decomposition.png) | Kayau | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) |

## Sources, captions, and credits

### Modular approach code reuse

Several operations can reuse one clearly named calculation. The mathematical labels are examples; no trigonometry is required here. In our package, Report uses the summary calculation from analysis.py through an ordinary import. Reuse does not require splitting every function into its own file.

**Alternative text:** Three mathematical operations reuse a shared helper for finding a hypotenuse.

**Credit:** “[Modular approach code reuse](https://commons.wikimedia.org/wiki/File:Modular_approach_code_reuse.svg)” by Kayau, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Commons-rendered PNG; no content changes.

### Virtual environments diagram, Building Better Research Software

Each project can use its own interpreter context and installed packages. The versions pictured are examples, not this class's required versions. Creating a venv uses a selected base Python; it does not by itself install another Python version. Compare this separation with the interpreter and package paths printed above.

**Alternative text:** One machine contains three virtual environments, each with its own Python version and a different collection of third-party package versions.

**Credit:** “[Virtual environments diagram, Building Better Research Software](https://carpentries-incubator.github.io/better-research-software/instructor/aio.html)” by Building Better Research Software lesson authors (Carpentries Incubator), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original PNG; unchanged.

The source lesson identifies its materials as CC BY 4.0 by the authors. [Original image](https://carpentries-incubator.github.io/better-research-software/fig/virtual-env.png); [lesson license](https://carpentries-incubator.github.io/better-research-software/instructor/LICENSE.html). This credit applies to the lesson illustration, not to an independent relicensing of any logos shown.

### Modular approach path

Break a larger task into understandable responsibilities. The gardening example supplies the analogy; the class refactor separates validation, calculation, state, and input/output. A box is a responsibility, not an instruction to create another file. Preserve intended behavior while changing the organization.

**Alternative text:** A path-cost problem is decomposed into calculating an area, multiplying by a unit cost, and smaller area calculations.

**Credit:** “[Modular approach path](https://commons.wikimedia.org/wiki/File:Modular_approach_path.svg)” by Kayau, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Commons-rendered PNG; no content changes.

## Reuse and presentation

Keep the source, creator, and license links with reused illustrations. If you crop, translate, recolor, or otherwise adapt an image, describe the changes and follow its linked license, including ShareAlike where applicable. CC0 does not require attribution; this course retains a provenance credit. These image terms are separate from the repository's software license.

Transparent diagrams are displayed on a white background so their black text/arrows remain readable across editor themes; the image files themselves are unchanged. The adjacent text explains the teaching point without relying on color or on reading every label in the picture. The numbered notebook sequence, exercise IDs, and commented `%load` solution cells are preserved.

[Class index](README.md) · [Instructor notes](INSTRUCTOR.md)

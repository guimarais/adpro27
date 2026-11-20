# Optional extension — local Podman packaging

Budget **135 minutes maximum**, including installation, image download, build,
testing, and explanation. Combined with optional AI (45), this stays within
180 minutes. Stop when the budget is exhausted. Packaging is enrichment;
Streamlit Community Cloud deployment does not require a container.

1. **35 minutes:** follow [Podman installation](https://podman.io/docs/installation)
   for your actual operating system. Linux can use the native engine; macOS and
   Windows need a Linux virtual machine through Podman machine/Desktop. Where
   required, run `podman machine init` and `podman machine start` before building.
   Installation may require administrator/institutional support. Check
   `podman info`; do not claim another platform was tested from a Linux result.
2. **45 minutes:** from the class/student repository root, inspect the supplied
   [Containerfile](Containerfile) and [.containerignore](.containerignore), then run:

   ```sh
   podman build -t adpro-explorer -f Containerfile .
   ```

   The image copies the selected Python/locked metadata, installs runtime
   dependencies without the dev group, and copies only app/package/fixture files.
   The source context excludes local secrets and `.venv`; the Containerfile does
   not copy `.streamlit`. No secret is needed at build or runtime.
3. **30 minutes:** run locally:

   ```sh
   podman run --rm -p 127.0.0.1:8501:8501 adpro-explorer
   ```

   Open `http://localhost:8501`, inspect the two-country total, and try missing
   France plus a saved AI example. Stop with Ctrl+C. The application binds inside
   the container on `0.0.0.0`; the host port is restricted to loopback. If 8501 is
   busy, use `127.0.0.1:8502:8501` and open host port 8502. This publishes a local
   port, not a public service. Port numbers are not authentication.
4. **25 minutes:** explain what the image contains, what the running container is,
   why your local `.venv` is excluded, and how local packaging differs from the
   public Community Cloud URL. Record actual build/run/platform results or leave
   them pending. Container-to-host Ollama networking is outside this extension.

Sources checked 20 November 2026:
[build](https://docs.podman.io/en/latest/markdown/podman-build.1.html),
[run](https://docs.podman.io/en/latest/markdown/podman-run.1.html),
[uv image integration](https://docs.astral.sh/uv/guides/integration/docker/).

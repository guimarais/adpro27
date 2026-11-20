# Deploy the supplied explorer

These steps use the approved **standalone student repository**. The author checked
the linked official documentation on **20 November 2026**; this is documentation
evidence, not a completed hosted deployment. Account screens can change. Work
within the README's allocated preparation/deployment/CI time and record actual
results. The instructor should rehearse the whole hosted route before teaching.

## 1. Prepare accounts and the repository

Sign in to GitHub with your own account and prepare Streamlit Community Cloud's
GitHub connection. Follow its authorization screen for the intended repository;
organization restrictions or unavailable access require instructor/account-owner
help. Browser-based or VS Code GitHub sign-in avoids placing tokens in commands.
Never write a token/key/password in a notebook, Git URL, README, or screenshot.
[Account connection](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account).

Create an **empty** GitHub repository using your account, without an automatically
created README/license/gitignore. Use a public repository for the simple public
data app, subject to institutional policy. Copy the class contents to a separate
local folder outside the course checkout. Include hidden files; exclude `.venv`,
caches, `.git`, `.env`, and real `.streamlit/secrets.toml`. This is your repository
root. Its relevant layout is:

```text
streamlit_app.py
pyproject.toml
uv.lock
.python-version
.gitignore
.github/workflows/checks.yml
.streamlit/secrets.example.toml
report_app/
fixtures/
tests/
solutions/
README.md
```

Run the following **manually in that new folder**, not in the course checkout or
a notebook. Replace the URL token with your repository's HTTPS URL:

```sh
git init -b main
git status --short
git add .gitignore .python-version pyproject.toml uv.lock streamlit_app.py report_app fixtures tests solutions .github .streamlit/secrets.example.toml README.md DEPLOYMENT.md PODMAN.md INSTRUCTOR.md LICENSE Containerfile .containerignore *.ipynb *.code-workspace
git diff --cached --name-only
git diff --cached
git commit -m "Add supplied data explorer"
git remote add origin <your-student-repository-https-url>
git push -u origin main
```

`git init` creates a new repository only in your copied folder. Git may first ask
for your author name/email; use your course-approved identity. Inspect the staged
paths/content before committing. Real secrets and `.venv` must not appear. The
class `.gitignore` works independently of the course's ignore file. If you have
unrelated files, stage only the class paths. Do not force-push to solve sign-in
or remote-history problems; inspect the error and ask for help.

## 2. Create the hosted app

At [Streamlit Community Cloud](https://share.streamlit.io), choose **Create app**,
then the existing-app option. Select your student repository, branch `main`, and
entrypoint **`streamlit_app.py`**. All these files are at the student repository
root. Open **Advanced settings** and explicitly select **Python 3.13**, matching
`.python-version` and `requires-python` in the manifest. Leave secrets empty for
the required saved-data/replay app, then deploy.
[Official deployment steps](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).

The hosting dependency detector recognizes `uv.lock`. Keep it and
`pyproject.toml` beside the entrypoint. Do not introduce `requirements.txt`,
`Pipfile`, or another competing dependency route. When changing a dependency,
use `uv add ...`, review both manifest and lockfile, and commit both. Confirm the
actual installer/Python version in the build log; documentation support does not
establish that a particular deployment succeeded.
[Dependency detection](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies).

Cloud execution starts from the repository root. Our fixture paths are resolved
from the Python package file, so they do not depend on notebook state. Opening
`http://localhost:8501` on your laptop runs only your local app; it is not a URL
your peer can use. GitHub stores code and runs automation; Streamlit hosts the
Python process. GitHub Pages cannot run it.
[File organization](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization),
[GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## 3. Inspect logs and diagnose a failure

Open the hosting logs with your repository write access. Identify the failing
stage: entrypoint, dependency installation, interpreter, or application run.
Read the first useful error, state a cause, apply one small fix, and inspect the
next build. [Saved failure cases](fixtures/deployment-failures.json) are invented
teaching examples with proposed checks; they are available while an actual build
or account setup is pending. Do not submit a saved log as a successful deployment.

The app emits `view release=06.0 rows=2` at INFO level and safe event names on
failure. For example, `data_load_failed kind=ValueError` leads to checking the
fixture/schema while the UI offers a recovery instruction. Logs contain no
credential values, access codes, user input, or raw provider exception bodies.
Share only the necessary redacted lines when asking for help.

## 4. Inspect CI, then verify a later update

GitHub discovers workflows only in the repository-root `.github/workflows`.
Open **Actions → Checks** for your exact pushed commit. The supplied single job
checks out that commit, installs uv and the selected Python, recreates the locked
environment, then runs pytest and Ruff lint/format checks. Package/action
installation needs network access; test execution uses saved data, replay, and
mocked SDK transport, without API/model access or secrets. The AppTest checks
exercise the real Streamlit script headlessly; they do not prove browser layout.
[uv integration](https://docs.astral.sh/uv/guides/integration/github/),
[Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart).

In part 06.4, adapt the workflow's test command to:

```sh
uv run --locked python -m pytest tests -q --maxfail=1
```

This keeps all supplied tests and stops after the first failure. Run it locally,
then inspect its hosted job after pushing. You are adapting one command, not
writing YAML from memory. No notebook execution or author-only repository checker
is required by the student workflow. Commits to the course repository do not
activate this nested student workflow.

For the release exercise, change only `RELEASE = "06.0"` to `RELEASE = "06.1"` in
`streamlit_app.py`, run the supplied local checks, review/stage that file, commit,
and push. Record `git rev-parse HEAD`, the Actions run URL/result for that commit,
and the public app URL showing **Release 06.1**. If necessary inspect hosting logs
and refresh after the update; do not assume a new push means a completed rebuild.
Community Cloud follows the configured branch independently of Actions. A red
check alone does not gate hosting; branch protection or a different release
pipeline would be additional work, outside this lesson.

## 5. Server-side configuration and optional private AI

Required completion uses no secrets. Missing configuration leaves the data app
and labelled illustrative replay usable. For harmless configuration practice,
copy [the disabled example](.streamlit/secrets.example.toml) to
`.streamlit/secrets.toml` in your student folder, keeping `[ai] enabled = false`.
The real filename is ignored. Check with
`git check-ignore .streamlit/secrets.toml`; never add it to the repository.

Optional live use requires **your own suitable access**, or an instructor-managed
private demonstration. First restrict hosting access to invited viewers using
the platform's sharing settings; keep the public handover app AI-disabled. Set
these values through the hosting **Secrets** settings, or an ignored local file:

```toml
[ai]
enabled = true
model = "your-verified-model-id"
api_key = "your-private-key"
access_code = "your-private-code-at-least-16-characters-long"
```

These strings are placeholders. Supply actual values privately, never by editing
the tracked example. No key field exists in the public UI. The live button also
requires the instructor access code and allows one run per browser session;
each run retains class 05's two-tool/three-request limits, no SDK retries, and
1024 output tokens per response. An incomplete setup leaves data/replay available.

The code gate is a classroom precaution, not user identity, a durable rate limit,
or a global cost cap. New sessions can run again. Use the hosting access controls
and provider-side restrictions appropriate to the demonstration, then disable or
remove live configuration afterwards. Do not publish an unrestricted shared key
behind an anonymous button. A public URL with AI disabled is sufficient for all
required completion. Live model/feature/access/cost/latency verification remains
separate from the deterministic tests. The selected model must be rehearsed by
the instructor; no unverified model is hard-coded.
[Hosted secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management),
[Local secrets](https://docs.streamlit.io/develop/concepts/connections/secrets-management),
[App sharing](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app).

The remote server's `localhost` means that server. It does not reach a laptop's
Ollama. No local-model download, container networking, or model hosting is required.

## 6. Peer handover

Use the allocated 15 minutes. A peer follows your local run instructions and
opens the public URL without a model key. Record date, URL, release, what they
tried, the observed result, and one improvement. Record an unavailable peer,
failed build, or missing URL honestly as pending; a static preview, saved trace,
or headless AppTest cannot establish this evidence.

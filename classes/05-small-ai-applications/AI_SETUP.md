# Explicit live OpenAI and optional local exploration

Default notebooks, references, CLI commands, and tests use local replay and never
need a credential or model download. Replays are illustrative scripts, not measured
model behavior. The installed SDK is locked in `uv.lock`; model access and feature
compatibility must be checked separately before delivery.

## Instructor live demonstration

Prepare a live demonstration or a recording before teaching. If access is unavailable,
walk through the labelled replay and record the live-demo delivery task as pending.
Do not claim a synthetic script is a recording. API access can incur charges;
students are not required to purchase it. A ChatGPT subscription does not supply
this application with an API key. Use institution-funded access if available.

Choose **one account-accessible model** whose official model page confirms both
function calling and structured outputs. Record its exact ID/date and test the
combination used by [provider.py](report_app/provider.py). No default model or live
capability is claimed by this distribution. Recheck [model documentation](https://developers.openai.com/api/docs/models),
[function calling](https://developers.openai.com/api/docs/guides/function-calling),
and [structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses).

Configure `OPENAI_MODEL` and `OPENAI_API_KEY` in the terminal session that will run
the command. Do not put keys in a notebook, output, source file, screenshot, or Git.
For example, enter the key without echoing it or adding it to shell history:

**Bash** (Linux/macOS; uses Bash `read`, not a portable POSIX-shell command):

```bash
export OPENAI_MODEL='replace-with-your-verified-model-id'
read -rsp 'OpenAI API key: ' OPENAI_API_KEY
export OPENAI_API_KEY
```

**PowerShell** (Windows; clear the temporary value after use):

```powershell
$env:OPENAI_MODEL = 'replace-with-your-verified-model-id'
$class05Key = Read-Host 'OpenAI API key' -AsSecureString
$env:OPENAI_API_KEY = [System.Net.NetworkCredential]::new('', $class05Key).Password
Remove-Variable class05Key
```

Then, from this class directory, explicitly opt in:

```sh
uv run --locked python -m report_app --structured --live
uv run --locked python -m report_app --case portugal --live
uv run --locked python -m report_app --case compare --live
uv run --locked python -m report_app --evaluate --live
```

The five-prompt evaluation makes at most **15 model requests total**, up to three
per prompt; it is not one single run. Never run it automatically from notebooks.
Remove `--live` to recover the free replay path. Clear the environment variables
when finished (`unset OPENAI_API_KEY OPENAI_MODEL` in Bash;
`Remove-Item Env:OPENAI_API_KEY, Env:OPENAI_MODEL` in PowerShell).

## What the supplied SDK code does

The first standalone example calls `client.responses.parse(..., text_format=Answer)`
to show the Pydantic convenience API. The complete supplied harness calls
`client.responses.create` with the same one-field JSON Schema and validates the
final text through `Answer.model_validate_json`. This keeps malformed saved and
live output on the same application validation path. Students need not implement
either SDK branch.

Tool proposals are returned as `function_call` items. Python validates their JSON
arguments and dispatches only a permitted name; the next request includes the
matching `function_call_output`. Full provider output is retained in conversation
history, including reasoning items when present. The public trace records only
observable application events. It does not expose private model reasoning.

`parallel_tool_calls=False` requests one proposal at a time; the harness also
rejects multiple proposals. Python enforces two executions/three model requests.
The API's `max_tool_calls` field applies to built-in tools and does not replace
our custom-function counter. Output is limited to 1,024 tokens per response;
reasoning tokens count where applicable. Incomplete responses stop without
parsing partial output. Model token needs may require instructor tuning.

The SDK client sets `max_retries=0` and `timeout=20.0`. Its normal retry defaults
would obscure the relationship between model-request counters and HTTP attempts.
The timeout controls socket operations, not a strict whole-run deadline. A valid
final answer, refusal, incomplete response, invalid call/output, API error, or limit
ends the run. Inspect the trace and retry manually after correcting the cause.
See the [Python SDK reference](https://developers.openai.com/api/reference/python)
and [Responses reference](https://developers.openai.com/api/reference/python/resources/responses/methods/create).
Official guidance was checked on 19 November 2026; mocked SDK checks are separate
from live model/access/cost/latency evidence.

## Optional Ollama — up to 120 minutes including setup/download

This is an instructor-supervised exploration, not a second required provider
implementation. The required OpenAI/replay harness remains unchanged.

1. Install the separate [Ollama application/server](https://docs.ollama.com/quickstart)
   for your OS; a Python package alone does not install the server or model.
2. Have the instructor select a small model only after testing **both tool calling
   and structured output** on representative CPU-only hardware. Record exact model
   tag, download size, RAM/CPU, latency, and results. No specific model has passed
   that delivery check here, so no untested model is recommended. Stop here if none
   is available; required replay work is already complete.
3. Download that verified model explicitly with `ollama pull <verified-model-tag>`.
   Start/confirm the local server according to the OS instructions; it commonly
   serves `http://localhost:11434`. Confirm availability with `ollama list`.
4. In a **temporary copy** of the class folder, install the separate Python client
   using `uv add ollama`. Follow the official [Python prerequisites](https://github.com/ollama/ollama-python),
   [tool-calling examples](https://docs.ollama.com/capabilities/tool-calling), and
   [structured-output examples](https://docs.ollama.com/capabilities/structured-outputs).
   Keep provider-specific calls visible. If necessary, test tool selection and
   final schema generation as separate stages. The same allowlist, validation,
   and limits must still be enforced by Python.
5. Compare one supplied prompt and record local results separately. A successful
   model installation or plain-text answer does not verify tool/schema support.

The optional instructions identify prerequisites, not verified CPU performance.
They introduce no required package, download, GPU, framework, or provider abstraction.

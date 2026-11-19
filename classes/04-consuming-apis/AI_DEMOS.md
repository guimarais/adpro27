# Instructor preview: OpenAI and Ollama over HTTP

These are two short demonstrations of method/URL/body/header/response, within the last teaching block of the 90-minute class. Students inspect the supplied source and saved envelopes; they do not need live credentials or local models. Class 05 teaches the OpenAI SDK, validation, bounded tool execution, and evaluation.

## Default: illustrative saved envelopes

From this class directory:

```sh
uv run --locked python -m examples.ai_http openai
uv run --locked python -m examples.ai_http ollama
```

Both work offline and read no credential environment variables. The envelopes are hand-authored representative subsets, clearly marked in [fixture provenance](fixtures/README.md); they are not live captures or claims about model quality. Use them if live access is unavailable.

## OpenAI: explicit live instructor call

Read [ai_http.py](examples/ai_http.py). Its live branch posts to the [official OpenAI Responses endpoint](https://developers.openai.com/api/reference/resources/responses/methods/create) using Requests. The body supplies model/input and a small output-token limit; the bearer key is a header. The instructor selects a currently accessible model and checks account access/cost before teaching; no model is hard-coded here. A live call can incur charges. Recheck the official documentation before delivery.

In a private instructor terminal, set `OPENAI_API_KEY` through your existing credential mechanism and `OPENAI_MODEL` to the selected accessible model. Do not paste the key into a notebook, a frontend, a shared terminal capture, or a committed file. This course does not load a .env file automatically. The following non-echoing prompt uses **Bash**. If your terminal uses zsh or another shell, start `bash` first and run the whole block there:

```bash
read -r -s -p "OpenAI key: " OPENAI_API_KEY
printf '\n'
export OPENAI_API_KEY
export OPENAI_MODEL="your-accessible-model"
uv run --locked python -m examples.ai_http openai --live
unset OPENAI_API_KEY
```

On PowerShell, use your approved private environment/credential mechanism to set those same two environment variables before the live command; no shell-specific credential prompt is required student work. Run only when you intend to call the service. The program never prints request headers. A missing setting, HTTP failure, invalid JSON, or timeout ends the demo with an error rather than silently substituting a fixture. Retry with the saved command when access is unavailable.

Inspect status, errors/incomplete details, and output item types. A completed response can contain different content types, including refusal content. Do not assume output[0] is always an assistant message. This preview prints the raw envelope so those differences stay visible; an output-token bound may yield incomplete output, which should be discussed rather than disguised as a successful final answer. No automatic retries are used for potentially charged POST requests.

## Ollama: explicit already-prepared local call

The [official generate endpoint](https://docs.ollama.com/api/generate) accepts model/prompt; `stream: false` returns a single JSON response for simple inspection. The example addresses only `http://127.0.0.1:11434`, reads `OLLAMA_MODEL`, and does not install Ollama or download a model.

On a machine with Ollama already running and a model already installed, select its exact installed name (`ollama list` helps identify it), then:

```sh
export OLLAMA_MODEL="your-installed-model"
uv run --locked python -m examples.ai_http ollama --live
```

PowerShell uses `$env:OLLAMA_MODEL="your-installed-model"` before the same Python command. The response text is under `response`; check `done`. The longer timeout allows for local generation but does not promise suitability on a student's CPU. No particular model/hardware combination was tested for this class. Keep installation, downloads, and local performance trials in optional work; use replay when the service/model is unavailable.

## Teaching comparison

Both examples demonstrate POST + JSON + explicit timeout + status check. OpenAI adds hosted-service authentication; local Ollama needs a running local service. The schemas and access requirements differ. Neither HTTP success nor JSON validity establishes factual correctness. A later deployed app's localhost refers to the hosting machine, not a student's laptop. The dedicated AI lesson will build the application around these boundaries.

Official endpoint documentation checked on **19 November 2026**. Provider access, current models, cost, live output, and CPU performance remain delivery-time checks. The required notebook path stays replay-based.

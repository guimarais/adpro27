"""Short instructor HTTP previews. Default to illustrative saved responses."""

import argparse
import json
import os

import requests

from report_app.source import read_fixture

PROMPT = "Explain an HTTP API in one sentence."


def openai_response(live: bool = False) -> dict:
    """POST a JSON body with a bearer header; no SDK is needed for this preview."""
    if not live:
        return read_fixture("openai-response.json")
    key = os.environ.get("OPENAI_API_KEY")
    model = os.environ.get("OPENAI_MODEL")
    if not key or not model:
        raise ValueError(
            "Set OPENAI_API_KEY and OPENAI_MODEL for the instructor demo, or omit --live."
        )
    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": model,
            "input": PROMPT,
            "max_output_tokens": 128,
            "store": False,
        },
        timeout=60,
    )
    response.raise_for_status()
    return response.json()


def ollama_response(live: bool = False) -> dict:
    """Ask an already-running local model for one complete JSON response."""
    if not live:
        return read_fixture("ollama-response.json")
    model = os.environ.get("OLLAMA_MODEL")
    if not model:
        raise ValueError("Set OLLAMA_MODEL to an installed model, or omit --live.")
    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={"model": model, "prompt": PROMPT, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("provider", choices=["openai", "ollama"])
    parser.add_argument(
        "--live", action="store_true", help="explicitly contact the selected service"
    )
    args = parser.parse_args()
    try:
        payload = (
            openai_response(args.live)
            if args.provider == "openai"
            else ollama_response(args.live)
        )
    except (ValueError, requests.RequestException) as exc:
        # Do not print request headers or credentials. The cause remains inspectable in code.
        parser.exit(
            1,
            f"Demo failed ({type(exc).__name__}); check configuration/service/status or omit --live.\n",
        )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()

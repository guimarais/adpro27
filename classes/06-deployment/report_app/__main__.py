"""Explicit replay/live entry points; the default command is offline."""

import argparse
import json

from openai import APIError

from .evaluation import evaluate
from .harness import run
from .provider import make_live_request, make_replay, structured_demo
from .source import read_fixture


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Explicitly contact OpenAI")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--case",
        default="portugal",
        choices=[
            "portugal",
            "total",
            "compare",
            "missing",
            "modify",
            "unknown-tool",
            "invalid-arguments",
            "malformed",
            "refused",
            "incomplete",
            "repeated",
        ],
    )
    group.add_argument("--evaluate", action="store_true")
    group.add_argument("--structured", action="store_true")
    args = parser.parse_args()
    try:
        if args.structured:
            result = {
                "mode": "live" if args.live else "replay",
                "answer": structured_demo(live=args.live).answer,
            }
        elif args.evaluate:
            result = evaluate(live=args.live)
        else:
            if args.live and args.case not in {
                "portugal",
                "total",
                "compare",
                "missing",
                "modify",
            }:
                parser.error(
                    "Failure cases are saved scripts; choose a five-prompt case for live mode."
                )
            script = read_fixture(f"replays/{args.case}.json")
            request = make_live_request() if args.live else make_replay(args.case)
            result = run(
                script["prompt"], request, mode="live" if args.live else "replay"
            )
    except APIError as exc:
        parser.exit(
            1,
            f"Live API error: {type(exc).__name__}. Inspect configuration or use replay.\n",
        )
    except ValueError as exc:
        parser.exit(1, f"{exc}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

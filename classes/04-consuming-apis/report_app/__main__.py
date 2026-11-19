"""Offline default; explicitly choose --local or --public for real HTTP."""

import argparse
import json

from .analysis import summarize
from .api import fetch_observations
from .public_data import fetch_population
from .source import load_observations


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--local",
        action="store_true",
        help="contact the running supplied FastAPI service",
    )
    mode.add_argument(
        "--public", action="store_true", help="contact the World Bank API"
    )
    args = parser.parse_args()
    try:
        if args.local:
            records = fetch_observations()
        elif args.public:
            records = fetch_population()
        else:
            records = load_observations()
    except (RuntimeError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")
    print(json.dumps(summarize(records), sort_keys=True))


if __name__ == "__main__":
    main()

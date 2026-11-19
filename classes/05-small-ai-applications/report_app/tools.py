"""Two supplied read-only operations and their small allowlist dispatcher."""

from pydantic import BaseModel, ConfigDict, Field

from .analysis import summarize
from .source import load_observations


class NoArguments(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class FindArguments(NoArguments):
    label: str = Field(min_length=1)


def get_summary() -> dict:
    """Count, total population, and mean population for the saved two countries."""
    return summarize(load_observations())


def find_observations(label: str) -> list[dict]:
    """Exact match only; a missing label is a valid empty result."""
    return [
        record.model_dump() for record in load_observations() if record.label == label
    ]


PERMITTED = {
    "get_summary": (NoArguments, get_summary),
    "find_observations": (FindArguments, find_observations),
}

TOOL_DEFINITIONS = [
    {
        "type": "function",
        "name": name,
        "description": function.__doc__,
        "parameters": {
            **arguments.model_json_schema(),
            "required": list(arguments.model_json_schema()["properties"]),
        },
        "strict": True,
    }
    for name, (arguments, function) in PERMITTED.items()
]


def dispatch(name: str, arguments: str):
    """A name selects supplied code; model-proposed code is never executed."""
    argument_model, function = PERMITTED[name]  # Unknown name raises KeyError.
    validated = argument_model.model_validate_json(arguments)
    return function(**validated.model_dump())

"""Supplied backend: run explicitly with uvicorn; no server starts on import."""

from fastapi import FastAPI

from .models import Observation
from .source import load_observations

app = FastAPI(title="Class 04 observations")


@app.get("/observations")
def observations(label: str | None = None) -> list[Observation]:
    """Return all observations, or those whose label matches exactly."""
    records = load_observations()
    return [record for record in records if label is None or record.label == label]

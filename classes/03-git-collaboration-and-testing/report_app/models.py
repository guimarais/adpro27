"""Contracts for the example's nonnegative quantities."""

from pydantic import BaseModel, Field


class Observation(BaseModel):
    label: str = Field(min_length=1)
    value: float = Field(ge=0, allow_inf_nan=False)

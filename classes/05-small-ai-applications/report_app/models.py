"""Keep the earlier Observation contract; add one small final-answer contract."""

from pydantic import BaseModel, ConfigDict, Field


class Observation(BaseModel):
    label: str = Field(min_length=1)
    value: float = Field(ge=0, allow_inf_nan=False)


class Answer(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    answer: str

"""A deliberately small World Bank example: two countries, one year, one page."""

from pydantic import BaseModel, Field, TypeAdapter, ValidationError

from .api import get_json
from .models import Observation

POPULATION_URL = "https://api.worldbank.org/v2/country/PRT;ESP/indicator/SP.POP.TOTL"
POPULATION_PARAMS = {"format": "json", "date": "2023", "per_page": 2}


class PopulationRow(BaseModel):
    countryiso3code: str = Field(min_length=3, max_length=3)
    date: str = Field(pattern=r"^\d{4}$")
    value: float = Field(ge=0, allow_inf_nan=False)


def parse_population(payload) -> list[Observation]:
    """Map ISO country/year into label and population/persons into value."""
    if (
        not isinstance(payload, list)
        or len(payload) != 2
        or not isinstance(payload[0], dict)
        or payload[0].get("pages") != 1
    ):
        raise ValueError(
            "Expected one complete World Bank page; check the country/year query."
        )
    try:
        rows = TypeAdapter(list[PopulationRow]).validate_python(payload[1])
    except ValidationError as exc:
        raise ValueError(
            "Invalid population record; check country/year and missing values. Missing is not zero."
        ) from exc
    return [
        Observation(label=f"{row.countryiso3code}:{row.date}", value=row.value)
        for row in rows
    ]


def fetch_population() -> list[Observation]:
    """Contact the public service only when explicitly called."""
    return parse_population(get_json(POPULATION_URL, params=POPULATION_PARAMS))

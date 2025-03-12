from pydantic import BaseModel, Field


class MushroomCreationForm(BaseModel):
    name: str
    is_edible: bool
    weight: int
    freshness: int = Field(None, ge=0, le=100)


class Mushroom(BaseModel):
    id: int
    name: str
    is_edible: bool
    weight: int
    freshness: int = Field(None, ge=0, le=100)
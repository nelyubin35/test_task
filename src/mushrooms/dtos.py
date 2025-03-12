from pydantic import BaseModel, Field


class CreateMushtoomDTO(BaseModel):
    name: str
    is_edible: bool
    weight: int
    freshness: int = Field(None, ge=0, le=100)
    
    
class UpdateMushroomDTO(BaseModel):
    name: str
    is_edible: bool
    weight: int
    freshness: int = Field(None, ge=0, le=100)
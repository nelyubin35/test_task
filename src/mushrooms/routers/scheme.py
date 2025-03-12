from pydantic import BaseModel, Field
from src.mushrooms.models import Mushroom


class MushroomBaseSc(BaseModel):
    name: str
    is_edible: bool
    weight: int
    freshness: int = Field(None, ge=0, le=100)
    
    
class MushroomCreationSc(MushroomBaseSc):
    pass


class MushroomGettingSc(MushroomBaseSc):
    id: int
    
    @classmethod
    def from_model(cls, mushroom: Mushroom) -> 'MushroomGettingSc':
        return cls(
            id=mushroom.id,
            name=mushroom.name,
            is_edible=mushroom.is_edible,
            weight=mushroom.weight,
            freshness=mushroom.freshness
        )
        
    
class MushroomUpdateSc(MushroomBaseSc):
    pass
    
    
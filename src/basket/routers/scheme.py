from pydantic import BaseModel

from src.basket.models import Basket
from src.mushrooms.routers.scheme import MushroomGettingSc


class BasketBaseSc(BaseModel):
    owner: str
    capacity: int 


class BasketCreationSc(BasketBaseSc):
    pass


class BasketGettingSc(BasketBaseSc):
    id: int
    mushrooms: list[MushroomGettingSc] = []
    
    @classmethod
    def from_model(cls, basket: Basket) -> 'BasketGettingSc':
        return cls(
            id=basket.id,
            owner=basket.owner,
            capacity=basket.capacity,
            mushrooms=[MushroomGettingSc.from_model(mushroom) for mushroom in basket.mushrooms]
        )
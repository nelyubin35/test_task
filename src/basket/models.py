from pydantic import BaseModel
from src.mushrooms.models import Mushroom
from .exceptions import MushroomInBasketAllreadyExists, MushroomWontFitInBasket, MushroomIsNotInBasket


class BasketCreationForm(BaseModel):
    owner: str
    capacity: int 


class Basket(BaseModel):
    id: int
    owner: str
    capacity: int
    mushrooms: list[Mushroom] = []
    
    def add_mushroom(self, mushroom: Mushroom):
        mushrooms_weight = 0
        for existed_mushroom in self.mushrooms:
            mushrooms_weight += existed_mushroom.weight
            if existed_mushroom.id == mushroom.id:
                raise MushroomInBasketAllreadyExists()
        if mushrooms_weight + mushroom.weight > self.capacity:
            raise MushroomWontFitInBasket()
        self.mushrooms.append(mushroom)
        
    def remove_mushroom(self, mushroom: Mushroom):
        try:
            self.mushrooms.remove(mushroom)
        except ValueError:
            raise MushroomIsNotInBasket()
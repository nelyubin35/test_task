from src.mushrooms.models import Mushroom, MushroomCreationForm


class MushroomIdGenerator:
    _last_id: int = 0
    
    @classmethod
    def get_id(cls) -> int:
        cls._last_id += 1
        return cls._last_id
    
    
class MushroomStorage:
    _storage: dict[int, Mushroom] = {}
    
    @classmethod 
    async def add(cls, basket_form: MushroomCreationForm) -> Mushroom:
        mushroom = Mushroom(
            id=MushroomIdGenerator.get_id(),
            name=basket_form.name,
            is_edible=basket_form.is_edible,
            weight=basket_form.weight,
            freshness=basket_form.freshness
        )
        cls._storage[mushroom.id] = mushroom
        return mushroom
    
    @classmethod 
    async def get_by_id(cls, mushroom_id: int) -> Mushroom | None:
        return cls._storage.get(mushroom_id, None)
    
    @classmethod 
    async def update(cls, mushroom: Mushroom) -> None:
        cls._storage[mushroom.id] = mushroom
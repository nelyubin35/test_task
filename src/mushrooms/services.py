from .exceptions import MushroomDoesntExists
from .models import Mushroom, MushroomCreationForm
from .db import MushroomStorage
from .dtos import CreateMushtoomDTO, UpdateMushroomDTO


async def create_mushroom(create_mushroom_dto: CreateMushtoomDTO) -> Mushroom:
    form = MushroomCreationForm(
        name=create_mushroom_dto.name,
        is_edible=create_mushroom_dto.is_edible,
        weight=create_mushroom_dto.weight,
        freshness=create_mushroom_dto.freshness
    )
    return await MushroomStorage.add(form) 


async def update_mushroom(mushroom_id: int, update_mushroom_dto: UpdateMushroomDTO) -> Mushroom:
    mushroom: Mushroom | None = await MushroomStorage.get_by_id(mushroom_id)
    if not mushroom:
        raise MushroomDoesntExists()
    dto = update_mushroom_dto
    mushroom.name = dto.name
    mushroom.is_edible = dto.is_edible
    mushroom.weight = dto.weight
    mushroom.freshness = dto.freshness
    await MushroomStorage.update(mushroom)
    return mushroom
    
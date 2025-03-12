from fastapi import APIRouter, Response, HTTPException

from src.mushrooms.exceptions import MushroomDoesntExists
from src.mushrooms.services import create_mushroom, update_mushroom
from .scheme import MushroomCreationSc, MushroomGettingSc, MushroomUpdateSc
from src.mushrooms.dtos import CreateMushtoomDTO, UpdateMushroomDTO
from src.mushrooms.models import Mushroom
from src.mushrooms.db import MushroomStorage

router = APIRouter(prefix='/mushrooms')


@router.post(path='/', response_model=MushroomGettingSc)
async def create_mushroom_api(
    body: MushroomCreationSc,
) -> MushroomGettingSc:
    mushroom: Mushroom = await create_mushroom(CreateMushtoomDTO(
        name=body.name,
        is_edible=body.is_edible,
        weight=body.weight,
        freshness=body.freshness
    ))
    return MushroomGettingSc.from_model(mushroom)


@router.get('/{mushroom_id}', response_model=MushroomGettingSc)
async def get_bushroom_api(
    mushroom_id: int,
    response: Response
) -> MushroomGettingSc:
    mushroom: Mushroom | None = await MushroomStorage.get_by_id(mushroom_id)
    if mushroom:
        return MushroomGettingSc.from_model(mushroom)
    response.status_code = 404
    raise HTTPException(404, detail='Гриб не существует')


@router.put('/{mushroom_id}', response_model=MushroomGettingSc)
async def update_mushroom_api(
    mushroom_id: int,
    body: MushroomUpdateSc,
) -> MushroomGettingSc:
    try:
        updated_mushroom = await update_mushroom(
            mushroom_id=mushroom_id,
            update_mushroom_dto=UpdateMushroomDTO(
                name=body.name,
                is_edible=body.is_edible,
                weight=body.weight,
                freshness=body.freshness
            )
        )
    except MushroomDoesntExists:
        raise HTTPException(404, detail='Гриб не существует')
    return MushroomGettingSc.from_model(updated_mushroom)
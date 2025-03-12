from src.mushrooms.models import Mushroom
from .dtos import CreateBasketDTO
from .models import BasketCreationForm, Basket
from .db import BasketStorage
from src.mushrooms.db import MushroomStorage
from src.mushrooms.exceptions import MushroomDoesntExists
from .exceptions import BasketDoesntExists, MushroomInBasketAllreadyExists, MushroomWontFitInBasket, MushroomIsNotInBasket


async def create_basket(create_basket_dto: CreateBasketDTO) -> Basket:
    dto = create_basket_dto
    form = BasketCreationForm(
        owner=dto.owner,
        capacity=dto.capacity,
    )
    return await BasketStorage.add(form)


async def add_mushroom_to_basket(mushroom_id: int, basket_id: int) -> Basket:
    mushroom: Mushroom | None = await MushroomStorage.get_by_id(mushroom_id)
    if mushroom is None:
        raise MushroomDoesntExists()
    basket: Basket | None = await BasketStorage.get_by_id(basket_id)
    if basket is None:
        raise BasketDoesntExists()
    try:
        basket.add_mushroom(mushroom)
    except MushroomInBasketAllreadyExists:
        raise
    except MushroomWontFitInBasket:
        raise
    
    await BasketStorage.update(basket)
    return basket
    
    
async def remove_mushroom_from_basket(mushroom_id: int, basket_id: int) -> Basket:
    mushroom: Mushroom | None = await MushroomStorage.get_by_id(mushroom_id)
    if mushroom is None:
        raise MushroomDoesntExists()
    basket: Basket | None = await BasketStorage.get_by_id(basket_id)
    if basket is None:
        raise BasketDoesntExists()
    try:
        basket.remove_mushroom(mushroom)
    except MushroomIsNotInBasket:
        raise
    return basket
    
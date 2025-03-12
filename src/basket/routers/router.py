from fastapi import APIRouter, HTTPException

from src.basket.dtos import CreateBasketDTO
from src.basket.services import add_mushroom_to_basket, create_basket, remove_mushroom_from_basket
from .scheme import BasketGettingSc, BasketCreationSc
from src.basket.models import Basket
from src.basket.exceptions import BasketDoesntExists, MushroomInBasketAllreadyExists, MushroomWontFitInBasket, MushroomIsNotInBasket
from src.mushrooms.exceptions import MushroomDoesntExists
from src.basket.db import BasketStorage


router = APIRouter(prefix='/baskets', tags=['baskets'])


@router.post(path='/', response_model=BasketGettingSc)
async def create_basket_api(
    body: BasketCreationSc
) -> BasketGettingSc:
    basket = await create_basket(CreateBasketDTO(
        owner=body.owner,
        capacity=body.capacity 
    ))
    return BasketGettingSc.from_model(basket)


@router.post(path='{basket_id}/add-mushroom/{mushroom_id}')
async def add_mushroom_to_basket_api(
    basket_id: int,
    mushroom_id: int,
) -> BasketGettingSc:
    try: 
        basket: Basket = await add_mushroom_to_basket(mushroom_id=mushroom_id, basket_id=basket_id)
    except BasketDoesntExists:
        raise HTTPException(404, detail='Корзины не существует')
    except MushroomDoesntExists:
        raise HTTPException(404, detail='Гриб не существует')
    except MushroomInBasketAllreadyExists:
        raise HTTPException(409, detail='Гриб уже в карзине')
    except MushroomWontFitInBasket:
        raise HTTPException(409, detail='Гриб не влезит в корзину')
    return BasketGettingSc.from_model(basket)


@router.get('/{basket_id}', response_model=BasketGettingSc)
async def get_basket_api(
    basket_id: int,
) -> BasketGettingSc:
    basket: Basket | None = await BasketStorage.get_by_id(basket_id)
    if basket is None:
        raise HTTPException(404, detail='Корзины не существует')
    return BasketGettingSc.from_model(basket)


@router.delete('/{basket_id}/remove-mushroom/{mushroom_id}', response_model=BasketGettingSc)
async def remove_mushroom_from_basket_api(
    basket_id: int,
    mushroom_id: int,
) -> BasketGettingSc:
    try: 
        basket: Basket = await remove_mushroom_from_basket(mushroom_id=mushroom_id, basket_id=basket_id)
    except BasketDoesntExists:
        raise HTTPException(404, detail='Корзины не существует')
    except MushroomDoesntExists:
        raise HTTPException(404, detail='Гриб не существует')
    except MushroomIsNotInBasket:
        raise HTTPException(404, detail='Гриб не в корзине')
    return BasketGettingSc.from_model(basket)
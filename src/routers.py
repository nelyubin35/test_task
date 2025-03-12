from fastapi import APIRouter

from src.mushrooms.routers import mushrooms_router
from src.basket.routers import baskets_router


main_router = APIRouter()
main_router.include_router(mushrooms_router)
main_router.include_router(baskets_router)


@main_router.get('/')
async def hello():
    return {'message': 'Hello World'}
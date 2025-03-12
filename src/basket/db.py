from src.basket.models import Basket, BasketCreationForm


class BasketIdGenerator:
    _last_id: int = 0
    
    @classmethod
    def get_id(cls) -> int:
        cls._last_id += 1
        return cls._last_id


class BasketStorage:
    _storage: dict[int, Basket] = {}
    
    @classmethod 
    async def add(cls, basket_form: BasketCreationForm) -> Basket:
        basket = Basket(
            id=BasketIdGenerator.get_id(),
            owner=basket_form.owner,
            capacity=basket_form.capacity
        )
        cls._storage[basket.id] = basket
        return basket
        
    @classmethod 
    async def get_by_id(cls, basket_id: int) -> Basket | None:
        return cls._storage.get(basket_id, None)
    
    @classmethod 
    async def update(cls, basket: Basket) -> None:
        cls._storage[basket.id] = basket
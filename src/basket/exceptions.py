
class BasketDoesntExists(Exception):
    message = 'Горзины не существует'
    
    
class MushroomInBasketAllreadyExists(Exception):
    message = 'Гриб уже есть в корзине'
    
    
class MushroomWontFitInBasket(Exception):
    message = 'Гриб не влезит в карзину'
    

class MushroomIsNotInBasket(Exception):
    message = 'Гриб не в корзине'
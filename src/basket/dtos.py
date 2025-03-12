from pydantic import BaseModel


class CreateBasketDTO(BaseModel):
    owner: str
    capacity: int 
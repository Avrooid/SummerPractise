from pydantic import BaseModel
from typing import Union, List


class PriceCreate(BaseModel):
    name: str
    price: int


class PriceRead(PriceCreate):
    id: int


class PriceUpdate(BaseModel):
    price: int

from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):#garante que os dados estejam certos
    name: str
    price: float


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
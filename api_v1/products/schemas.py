



from pydantic import BaseModel
from sqlalchemy.orm import Mapped

class Product(BaseModel):
    

    name: str
    price: int
    description: str




from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Mapped

class ProductBase(BaseModel):
    name: str
    price: int
    description: str

class ProductCreate(BaseModel):
    pass



class Product(ProductBase):
    model_config = ConfigDict(from_attributes= True )
    id: int
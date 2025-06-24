from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    price: int
    sale_price: int
    rating: float
    feedbacks: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True

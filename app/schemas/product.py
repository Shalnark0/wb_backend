from pydantic import BaseModel

class ProductCreate(BaseModel):
    title: str
    price: int
    sale_price: int
    rating: float
    feedbacks: int

class ProductOut(ProductCreate):
    id: int

    class Config:
        orm_mode = True

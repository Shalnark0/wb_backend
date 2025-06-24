from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.schemas.product import ProductOut, ProductCreate
from app.crud.products import get_products_filtered, create_product
from typing import List
from app.parser.parser import fetch_products_by_query

router = APIRouter()

@router.get("/products/", response_model=List[ProductOut])
async def read_products(
    min_price: int = 0,
    min_rating: float = 0,
    min_feedbacks: int = 0,
    db: AsyncSession = Depends(get_db)
):
    return await get_products_filtered(db, min_price, min_rating, min_feedbacks)

@router.post("/parse/")
async def parse_products(query: str):
    products: List[ProductCreate] = await fetch_products_by_query(query)
    
    for product in products:
        print("Продукт:", product)

    return {"parsed": len(products), "products": products}



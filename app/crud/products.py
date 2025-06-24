from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.schemas.product import ProductOut

async def create_product(db: AsyncSession, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_products_filtered(
    db: AsyncSession,
    min_price: int = 0,
    max_price: int = 100_000,
    min_rating: float = 0,
    min_feedbacks: int = 0,
):
    query = select(Product).where(
        Product.price >= min_price,
        Product.price <= max_price,
        Product.rating >= min_rating,
        Product.feedbacks >= min_feedbacks
    )
    result = await db.execute(query)
    return result.scalars().all()

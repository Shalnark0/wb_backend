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


FAKE_PRODUCTS = [
    ProductOut(id=1, title="Кроссовки Adidas", price=7000, sale_price=5000, rating=4.7, feedbacks=1340),
    ProductOut(id=2, title="Футболка Nike", price=3000, sale_price=2700, rating=4.5, feedbacks=420),
    ProductOut(id=3, title="Куртка Puma", price=15000, sale_price=12000, rating=4.8, feedbacks=620),
]

async def get_products_filtered(
    db,
    min_price: int = 0,
    min_rating: float = 0,
    min_feedbacks: int = 0,
):
    return [
        product for product in FAKE_PRODUCTS
        if product.price >= min_price and
           product.rating >= min_rating and
           product.feedbacks >= min_feedbacks
    ]


import httpx
from typing import List
from app.schemas.product import ProductCreate

async def fetch_products_by_query(query: str, page: int = 1) -> List[ProductCreate]:
    url = "https://search.wb.ru/exactmatch/ru/common/v4/search"
    params = {
        "query": query,
        "page": page,
        "resultset": "catalog",
        "dest": "-1257786",
        "sort": "popular",
        "spp": "30"
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

    result = []
    for item in data.get("data", {}).get("products", []):
        try:
            result.append(ProductCreate(
                title=item.get("name", "Нет названия"),
                price=item.get("priceU", 0) // 100,
                sale_price=item.get("salePriceU", 0) // 100,
                rating=item.get("reviewRating", 0),
                feedbacks=item.get("feedbacks", 0)
            ))
        except Exception as e:
            print(f"Ошибка при обработке товара: {e}")

    return result

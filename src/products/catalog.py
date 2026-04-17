import httpx
from src.config import API_BASE_URL

async def list_products(page=1, limit=20, category=None, sort=None):
    params = {"page": page, "limit": limit}
    if category:
        params["category"] = category
    if sort:
        params["sort"] = sort
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/products", params=params)
        response.raise_for_status()
        return response.json()

async def get_product(product_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/products/{product_id}")
        response.raise_for_status()
        return response.json()

async def create_product(token, data):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/products", json=data, headers=headers)
        response.raise_for_status()
        return response.json()

async def update_product(product_id, token, data):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/products/{product_id}", json=data, headers=headers)
        response.raise_for_status()
        return response.json()

async def delete_product(product_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/products/{product_id}", headers=headers)
        response.raise_for_status()
        return response.status_code

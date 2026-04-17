import httpx
from src.config import API_BASE_URL

async def get_stock(product_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/products/{product_id}/inventory", headers=headers)
        response.raise_for_status()
        return response.json()

async def update_stock(product_id, token, quantity, warehouse=None):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"quantity": quantity}
    if warehouse:
        data["warehouse"] = warehouse
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/products/{product_id}/inventory",
                                  json=data, headers=headers)
        response.raise_for_status()
        return response.json()

async def reserve_stock(product_id, token, quantity, order_id):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/products/{product_id}/inventory/reserve",
                                 json={"quantity": quantity, "order_id": order_id}, headers=headers)
        response.raise_for_status()
        return response.json()

async def release_stock(product_id, token, order_id):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/products/{product_id}/inventory/reserve/{order_id}",
                                   headers=headers)
        response.raise_for_status()
        return response.status_code

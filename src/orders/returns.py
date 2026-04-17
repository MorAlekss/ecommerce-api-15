import httpx
from src.config import API_BASE_URL

async def create_return(order_id, token, items, reason):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/orders/{order_id}/returns",
                                     json={"items": items, "reason": reason}, headers=headers)
        response.raise_for_status()
        return response.json()

async def get_return(return_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/returns/{return_id}", headers=headers)
        response.raise_for_status()
        return response.json()

async def list_returns(token, page=1, limit=20):
    headers = {"Authorization": f"Bearer {token}"}
    params = {"page": page, "limit": limit}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/returns", params=params, headers=headers)
        response.raise_for_status()
        return response.json()

async def approve_return(return_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/returns/{return_id}",
                                      json={"status": "approved"}, headers=headers)
        response.raise_for_status()
        return response.json()

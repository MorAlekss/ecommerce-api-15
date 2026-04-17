import httpx
from src.config import API_BASE_URL

async def list_users(token, page=1, limit=20, filters=None):
    headers = {"Authorization": f"Bearer {token}"}
    params = {"page": page, "limit": limit, **(filters or {})}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/admin/users", params=params, headers=headers)
    response.raise_for_status()
    return response.json()

async def get_user(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/admin/users/{user_id}", headers=headers)
    response.raise_for_status()
    return response.json()

async def suspend_user(user_id, token, reason):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/admin/users/{user_id}/suspend",
                                     json={"reason": reason}, headers=headers)
    response.raise_for_status()
    return response.json()

async def reinstate_user(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/admin/users/{user_id}/suspend", headers=headers)
    response.raise_for_status()
    return response.status_code

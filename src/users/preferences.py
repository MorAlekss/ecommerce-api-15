import httpx
from src.config import API_BASE_URL

async def get_preferences(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}/preferences", headers=headers)
    response.raise_for_status()
    return response.json()

async def update_preferences(user_id, token, preferences):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/users/{user_id}/preferences",
                                json=preferences, headers=headers)
    response.raise_for_status()
    return response.json()

async def reset_preferences(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/users/{user_id}/preferences", headers=headers)
    response.raise_for_status()
    return response.status_code

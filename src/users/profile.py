import httpx
from src.config import API_BASE_URL

async def get_profile(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}", headers=headers)
    response.raise_for_status()
    return response.json()

async def update_profile(user_id, token, data):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/users/{user_id}", json=data, headers=headers)
    response.raise_for_status()
    return response.json()

async def update_avatar(user_id, token, avatar_url):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/users/{user_id}/avatar",
                                     json={"avatar_url": avatar_url}, headers=headers)
    response.raise_for_status()
    return response.json()

async def delete_account(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/users/{user_id}", headers=headers)
    response.raise_for_status()
    return response.status_code

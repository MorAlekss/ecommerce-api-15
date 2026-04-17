import httpx
from src.config import API_BASE_URL

async def get_api_tokens(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}/tokens", headers=headers)
        response.raise_for_status()
        return response.json()

async def create_api_token(user_id, token, name, scopes):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/users/{user_id}/tokens",
                                     json={"name": name, "scopes": scopes}, headers=headers)
        response.raise_for_status()
        return response.json()

async def revoke_api_token(user_id, token_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/users/{user_id}/tokens/{token_id}", headers=headers)
        response.raise_for_status()
        return response.status_code

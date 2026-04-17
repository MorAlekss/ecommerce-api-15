import httpx
from src.config import API_BASE_URL

async def get_oauth_url(provider, redirect_uri):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/auth/oauth/{provider}", params={"redirect_uri": redirect_uri})
        response.raise_for_status()
        return response.json()

async def exchange_oauth_code(provider, code, redirect_uri):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/auth/oauth/{provider}/callback",
                                     json={"code": code, "redirect_uri": redirect_uri})
        response.raise_for_status()
        return response.json()

async def revoke_oauth_token(provider, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/auth/oauth/{provider}/revoke", headers=headers)
        response.raise_for_status()
        return response.status_code

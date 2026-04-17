import httpx
from src.config import API_BASE_URL

async def login(email, password):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/auth/login", json={"email": email, "password": password})
        response.raise_for_status()
        return response.json()

async def logout(token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/auth/logout", headers=headers)
        response.raise_for_status()
        return response.status_code

async def refresh_token(refresh_token):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/auth/refresh", json={"refresh_token": refresh_token})
        response.raise_for_status()
        return response.json()

async def verify_email(token):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/auth/verify", params={"token": token})
        response.raise_for_status()
        return response.json()

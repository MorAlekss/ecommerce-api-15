import httpx
from src.config import API_BASE_URL, API_KEY

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY,
}

async def get(url, params=None, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=merged_headers)
    response.raise_for_status()
    return response.json()

async def post(url, data=None, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=merged_headers)
    response.raise_for_status()
    return response.json()

async def put(url, data=None, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    async with httpx.AsyncClient() as client:
        response = await client.put(url, json=data, headers=merged_headers)
    response.raise_for_status()
    return response.json()

async def patch(url, data=None, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    async with httpx.AsyncClient() as client:
        response = await client.patch(url, json=data, headers=merged_headers)
    response.raise_for_status()
    return response.json()

async def delete(url, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=merged_headers)
    response.raise_for_status()
    return response.status_code

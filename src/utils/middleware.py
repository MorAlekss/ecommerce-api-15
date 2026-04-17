import httpx
import logging

logger = logging.getLogger(__name__)

async def log_request(method, url, **kwargs):
    """Log and execute an HTTP request."""
    logger.info(f"{method.upper()} {url}")
    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, **kwargs)
    logger.info(f"Response: {response.status_code}")
    return response

async def authenticated_get(url, token, params=None):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

async def authenticated_post(url, token, data=None):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

async def authenticated_put(url, token, data=None):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.put(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

async def authenticated_delete(url, token):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code

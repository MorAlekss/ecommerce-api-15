import time
import httpx

async def retry_request(func, max_retries=3, backoff=1.0):
    """Retry a request function on failure with exponential backoff."""
    last_error = None
    for attempt in range(max_retries):
        try:
            return await func()
        except httpx.HTTPError as e:
            last_error = e
            if attempt < max_retries - 1:
                time.sleep(backoff * (2 ** attempt))
    raise last_error

async def get_with_retry(url, params=None, headers=None, max_retries=3):
    async def _request():
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
    return await retry_request(_request, max_retries=max_retries)

async def post_with_retry(url, data=None, headers=None, max_retries=3):
    async def _request():
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
    return await retry_request(_request, max_retries=max_retries)

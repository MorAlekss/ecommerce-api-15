import time
import requests

def retry_request(func, max_retries=3, backoff=1.0):
    """Retry a request function on failure with exponential backoff."""
    last_error = None
    for attempt in range(max_retries):
        try:
            return func()
        except requests.exceptions.RequestException as e:
            last_error = e
            if attempt < max_retries - 1:
                time.sleep(backoff * (2 ** attempt))
    raise last_error

def get_with_retry(url, params=None, headers=None, max_retries=3):
    def _request():
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    return retry_request(_request, max_retries=max_retries)

def post_with_retry(url, data=None, headers=None, max_retries=3):
    def _request():
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    return retry_request(_request, max_retries=max_retries)

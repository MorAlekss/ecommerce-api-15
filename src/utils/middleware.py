import requests
import logging

logger = logging.getLogger(__name__)

def log_request(method, url, **kwargs):
    """Log and execute an HTTP request."""
    logger.info(f"{method.upper()} {url}")
    response = requests.request(method, url, **kwargs)
    logger.info(f"Response: {response.status_code}")
    return response

def authenticated_get(url, token, params=None):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def authenticated_post(url, token, data=None):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

def authenticated_put(url, token, data=None):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

def authenticated_delete(url, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code

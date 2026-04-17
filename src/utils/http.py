import requests
from src.config import API_BASE_URL, API_KEY

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY,
}

def get(url, params=None, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    response = requests.get(url, params=params, headers=merged_headers)
    response.raise_for_status()
    return response.json()

def post(url, data=None, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    response = requests.post(url, json=data, headers=merged_headers)
    response.raise_for_status()
    return response.json()

def put(url, data=None, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    response = requests.put(url, json=data, headers=merged_headers)
    response.raise_for_status()
    return response.json()

def patch(url, data=None, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    response = requests.patch(url, json=data, headers=merged_headers)
    response.raise_for_status()
    return response.json()

def delete(url, headers=None):
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}
    response = requests.delete(url, headers=merged_headers)
    response.raise_for_status()
    return response.status_code

import requests
from src.config import API_BASE_URL

def get_profile(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_BASE_URL}/users/{user_id}", headers=headers)
    response.raise_for_status()
    return response.json()

def update_profile(user_id, token, data):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{API_BASE_URL}/users/{user_id}", json=data, headers=headers)
    response.raise_for_status()
    return response.json()

def update_avatar(user_id, token, avatar_url):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.patch(f"{API_BASE_URL}/users/{user_id}/avatar",
                              json={"avatar_url": avatar_url}, headers=headers)
    response.raise_for_status()
    return response.json()

def delete_account(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{API_BASE_URL}/users/{user_id}", headers=headers)
    response.raise_for_status()
    return response.status_code

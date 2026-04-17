import requests
from src.config import API_BASE_URL

def get_preferences(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/preferences", headers=headers)
    response.raise_for_status()
    return response.json()

def update_preferences(user_id, token, preferences):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{API_BASE_URL}/users/{user_id}/preferences",
                            json=preferences, headers=headers)
    response.raise_for_status()
    return response.json()

def reset_preferences(user_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{API_BASE_URL}/users/{user_id}/preferences", headers=headers)
    response.raise_for_status()
    return response.status_code

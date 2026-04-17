import requests
from src.config import API_BASE_URL, SMTP_HOST

def send_email(token, to, subject, body, template=None):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"to": to, "subject": subject, "body": body}
    if template:
        data["template"] = template
    response = requests.post(f"{API_BASE_URL}/notifications/email", json=data, headers=headers)
    response.raise_for_status()
    return response.json()

def send_bulk_email(token, recipients, subject, body, template=None):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"recipients": recipients, "subject": subject, "body": body}
    if template:
        data["template"] = template
    response = requests.post(f"{API_BASE_URL}/notifications/email/bulk", json=data, headers=headers)
    response.raise_for_status()
    return response.json()

def get_email_status(email_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_BASE_URL}/notifications/email/{email_id}", headers=headers)
    response.raise_for_status()
    return response.json()

def unsubscribe_email(email, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{API_BASE_URL}/notifications/email/unsubscribe",
                               json={"email": email}, headers=headers)
    response.raise_for_status()
    return response.status_code

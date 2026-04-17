import httpx
from src.config import API_BASE_URL, SMS_API_KEY

SMS_HEADERS = {"X-SMS-API-Key": SMS_API_KEY}

async def send_sms(to, message):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/notifications/sms",
                                     json={"to": to, "message": message}, headers=SMS_HEADERS)
    response.raise_for_status()
    return response.json()

async def send_bulk_sms(recipients, message):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/notifications/sms/bulk",
                                     json={"recipients": recipients, "message": message}, headers=SMS_HEADERS)
    response.raise_for_status()
    return response.json()

async def get_sms_status(sms_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/notifications/sms/{sms_id}", headers=SMS_HEADERS)
    response.raise_for_status()
    return response.json()

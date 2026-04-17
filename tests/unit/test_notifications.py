import sys
sys.path.insert(0, '.')
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
import src.notifications.email as email_module
import httpx as _httpx
from src.notifications.email import send_email, send_bulk_email, get_email_status
from src.notifications.sms import send_sms, send_bulk_sms

# Inject httpx into email module namespace so patch.object can find it
email_module.httpx = _httpx


@pytest.mark.asyncio
async def test_send_email():
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "msg_123", "status": "queued"}
    mock_response.raise_for_status.return_value = None
    with patch.object(email_module, 'httpx') as mock_httpx:
        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        mock_httpx.AsyncClient.return_value = mock_client
        result = await send_email("token123", "user@example.com", "Hello", "Test body")
        assert result["status"] == "queued"

@pytest.mark.asyncio
async def test_send_bulk_email():
    mock_response = MagicMock()
    mock_response.json.return_value = {"batch_id": "batch_123", "count": 3}
    mock_response.raise_for_status.return_value = None
    with patch.object(email_module, 'httpx') as mock_httpx:
        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        mock_httpx.AsyncClient.return_value = mock_client
        result = await send_bulk_email("token123", ["a@example.com", "b@example.com"], "Subject", "Body")
        assert result["count"] == 3

@pytest.mark.asyncio
async def test_send_sms():
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "sms_123", "status": "sent"}
    mock_response.raise_for_status.return_value = None
    with patch('src.notifications.sms.httpx.AsyncClient') as MockClient:
        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await send_sms("+123****7890", "Your order is ready!")
        assert result["status"] == "sent"

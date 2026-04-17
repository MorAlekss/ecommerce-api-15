import sys
sys.path.insert(0, '.')
import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from src.payments.stripe import create_payment_intent, refund_payment
from src.payments.webhook import register_webhook


@pytest.mark.asyncio
async def test_create_payment_intent():
    with patch('src.payments.stripe.httpx.AsyncClient') as mock_cls:
        mock_client = AsyncMock()
        mock_cls.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "pi_123", "status": "requires_payment_method"}
        mock_response.raise_for_status.return_value = None
        mock_client.post.return_value = mock_response
        result = await create_payment_intent(1000, "usd")
        assert result["id"] == "pi_123"

@pytest.mark.asyncio
async def test_refund_payment():
    with patch('src.payments.stripe.httpx.AsyncClient') as mock_cls:
        mock_client = AsyncMock()
        mock_cls.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "re_123", "status": "succeeded"}
        mock_response.raise_for_status.return_value = None
        mock_client.post.return_value = mock_response
        result = await refund_payment("pi_123")
        assert result["status"] == "succeeded"

@pytest.mark.asyncio
async def test_register_webhook():
    with patch('src.payments.webhook.httpx.AsyncClient') as mock_cls:
        mock_client = AsyncMock()
        mock_cls.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "wh_123", "url": "https://example.com/webhook"}
        mock_response.raise_for_status.return_value = None
        mock_client.post.return_value = mock_response
        result = await register_webhook("token123", "https://example.com/webhook", ["payment.success"])
        assert result["id"] == "wh_123"

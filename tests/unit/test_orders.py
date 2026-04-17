import sys
sys.path.insert(0, '.')
from unittest.mock import patch, AsyncMock, MagicMock
from src.orders.checkout import create_cart, add_to_cart, checkout
from src.orders.history import list_orders, get_order, cancel_order
from src.orders.returns import create_return, get_return
import pytest


@pytest.mark.asyncio
async def test_create_cart():
    with patch('src.orders.checkout.httpx.AsyncClient') as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "cart1", "items": []}
        mock_response.raise_for_status.return_value = None
        mock_client.post.return_value = mock_response
        result = await create_cart("token123")
        assert result["id"] == "cart1"

@pytest.mark.asyncio
async def test_add_to_cart():
    with patch('src.orders.checkout.httpx.AsyncClient') as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "cart1", "items": [{"product_id": "p1", "quantity": 2}]}
        mock_response.raise_for_status.return_value = None
        mock_client.post.return_value = mock_response
        result = await add_to_cart("cart1", "token123", "p1", 2)
        assert len(result["items"]) == 1

@pytest.mark.asyncio
async def test_list_orders():
    with patch('src.orders.history.httpx.AsyncClient') as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"orders": [{"id": "o1"}], "total": 1}
        mock_response.raise_for_status.return_value = None
        mock_client.get.return_value = mock_response
        result = await list_orders("token123")
        assert result["total"] == 1

@pytest.mark.asyncio
async def test_create_return():
    with patch('src.orders.returns.httpx.AsyncClient') as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "r1", "status": "pending"}
        mock_response.raise_for_status.return_value = None
        mock_client.post.return_value = mock_response
        result = await create_return("o1", "token123", [{"product_id": "p1", "quantity": 1}], "defective")
        assert result["status"] == "pending"

import sys
sys.path.insert(0, '.')
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from src.products.catalog import list_products, get_product, create_product, update_product
from src.products.search import search_products, get_suggestions
from src.products.inventory import get_stock, update_stock, reserve_stock


@pytest.mark.asyncio
async def test_list_products():
    with patch('src.products.catalog.httpx.AsyncClient') as mock_client_cls:
        mock_client = AsyncMock()
        mock_client_cls.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"products": [{"id": "p1"}, {"id": "p2"}], "total": 2}
        mock_response.raise_for_status.return_value = None
        mock_client.get.return_value = mock_response
        result = await list_products()
        assert result["total"] == 2

@pytest.mark.asyncio
async def test_get_product():
    with patch('src.products.catalog.httpx.AsyncClient') as mock_client_cls:
        mock_client = AsyncMock()
        mock_client_cls.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "p1", "name": "Widget", "price": 9.99}
        mock_response.raise_for_status.return_value = None
        mock_client.get.return_value = mock_response
        result = await get_product("p1")
        assert result["name"] == "Widget"

@pytest.mark.asyncio
async def test_search_products():
    with patch('src.products.search.httpx.AsyncClient') as mock_client_cls:
        mock_client = AsyncMock()
        mock_client_cls.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": [{"id": "p1", "name": "Widget"}], "total": 1}
        mock_response.raise_for_status.return_value = None
        mock_client.get.return_value = mock_response
        result = await search_products("widget")
        assert result["total"] == 1

@pytest.mark.asyncio
async def test_get_stock():
    with patch('src.products.inventory.httpx.AsyncClient') as mock_client_cls:
        mock_client = AsyncMock()
        mock_client_cls.return_value.__aenter__.return_value = mock_client
        mock_response = MagicMock()
        mock_response.json.return_value = {"product_id": "p1", "quantity": 50}
        mock_response.raise_for_status.return_value = None
        mock_client.get.return_value = mock_response
        result = await get_stock("p1", "token123")
        assert result["quantity"] == 50

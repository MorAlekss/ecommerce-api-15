import sys
sys.path.insert(0, '.')
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from src.auth.login import login, logout, refresh_token, verify_email
from src.auth.oauth import get_oauth_url, exchange_oauth_code
from src.auth.tokens import get_api_tokens, create_api_token, revoke_api_token


@pytest.mark.asyncio
async def test_login():
    with patch('src.auth.login.httpx.AsyncClient') as mock_client:
        mock_client_instance = AsyncMock()
        mock_client.return_value.__aenter__.return_value = mock_client_instance
        mock_response = MagicMock()
        mock_response.json.return_value = {"access_token": "token123", "refresh_token": "***"}
        mock_response.raise_for_status.return_value = None
        mock_client_instance.post.return_value = mock_response
        result = await login("user@example.com", "password")
        assert result["access_token"] == "token123"

@pytest.mark.asyncio
async def test_logout():
    with patch('src.auth.login.httpx.AsyncClient') as mock_client:
        mock_client_instance = AsyncMock()
        mock_client.return_value.__aenter__.return_value = mock_client_instance
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None
        mock_client_instance.post.return_value = mock_response
        result = await logout("token123")
        assert result == 200

@pytest.mark.asyncio
async def test_refresh_token():
    with patch('src.auth.login.httpx.AsyncClient') as mock_client:
        mock_client_instance = AsyncMock()
        mock_client.return_value.__aenter__.return_value = mock_client_instance
        mock_response = MagicMock()
        mock_response.json.return_value = {"access_token": "new_token"}
        mock_response.raise_for_status.return_value = None
        mock_client_instance.post.return_value = mock_response
        result = await refresh_token("refresh123")
        assert result["access_token"] == "new_token"

@pytest.mark.asyncio
async def test_get_oauth_url():
    with patch('src.auth.oauth.httpx.AsyncClient') as mock_client:
        mock_client_instance = AsyncMock()
        mock_client.return_value.__aenter__.return_value = mock_client_instance
        mock_response = MagicMock()
        mock_response.json.return_value = {"url": "https://oauth.example.com/auth"}
        mock_response.raise_for_status.return_value = None
        mock_client_instance.get.return_value = mock_response
        result = await get_oauth_url("google", "https://app.example.com/callback")
        assert "url" in result

@pytest.mark.asyncio
async def test_create_api_token():
    with patch('src.auth.tokens.httpx.AsyncClient') as mock_client:
        mock_client_instance = AsyncMock()
        mock_client.return_value.__aenter__.return_value = mock_client_instance
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "tok_123", "name": "My Token"}
        mock_response.raise_for_status.return_value = None
        mock_client_instance.post.return_value = mock_response
        result = await create_api_token("user1", "token123", "My Token", ["read"])
        assert result["id"] == "tok_123"

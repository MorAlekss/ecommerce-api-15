import sys
sys.path.insert(0, '.')
from unittest.mock import patch, MagicMock
from src.utils.http import get, post, put, patch as http_patch, delete
from src.utils.middleware import authenticated_get, authenticated_post


def test_get():
    with patch('src.utils.http.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": "value"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        result = get("https://api.example.com/test")
        assert result["data"] == "value"

def test_post():
    with patch('src.utils.http.requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "123"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        result = post("https://api.example.com/test", {"key": "value"})
        assert result["id"] == "123"

def test_authenticated_get():
    with patch('src.utils.middleware.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": "secure"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        result = authenticated_get("https://api.example.com/secure", "token123")
        assert result["data"] == "secure"

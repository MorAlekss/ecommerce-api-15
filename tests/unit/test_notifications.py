import sys
sys.path.insert(0, '.')
from unittest.mock import patch, MagicMock
from src.notifications.email import send_email, send_bulk_email, get_email_status
from src.notifications.sms import send_sms, send_bulk_sms


def test_send_email():
    with patch('src.notifications.email.requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "msg_123", "status": "queued"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        result = send_email("token123", "user@example.com", "Hello", "Test body")
        assert result["status"] == "queued"

def test_send_bulk_email():
    with patch('src.notifications.email.requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = {"batch_id": "batch_123", "count": 3}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        result = send_bulk_email("token123", ["a@example.com", "b@example.com"], "Subject", "Body")
        assert result["count"] == 3

def test_send_sms():
    with patch('src.notifications.sms.requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "sms_123", "status": "sent"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        result = send_sms("+1234567890", "Your order is ready!")
        assert result["status"] == "sent"

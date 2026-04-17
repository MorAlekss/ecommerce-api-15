import sys
sys.path.insert(0, '.')
from unittest.mock import patch, MagicMock, call


def make_mock_response(data):
    m = MagicMock()
    m.json.return_value = data
    m.raise_for_status = MagicMock(return_value=None)
    m.status_code = 200
    return m


def test_full_purchase_flow():
    """Integration test: login → get product → add to cart → checkout → payment"""
    login_resp = make_mock_response({"access_token": "tok123"})
    product_resp = make_mock_response({"id": "p1", "name": "Widget", "price": 999})
    cart_resp = make_mock_response({"id": "cart1", "total": 999})
    payment_resp = make_mock_response({"id": "pi_123", "status": "requires_confirmation"})

    with patch('src.auth.login.requests') as mock_requests_login, \
         patch('src.products.catalog.requests') as mock_requests_catalog, \
         patch('src.orders.checkout.requests') as mock_requests_checkout, \
         patch('src.payments.stripe.requests') as mock_requests_stripe:

        mock_requests_login.post.return_value = login_resp
        mock_requests_catalog.get.return_value = product_resp
        mock_requests_checkout.post.return_value = cart_resp
        mock_requests_stripe.post.return_value = payment_resp

        from src.auth.login import login
        from src.products.catalog import get_product
        from src.orders.checkout import create_cart
        from src.payments.stripe import create_payment_intent

        auth = login("user@example.com", "password")
        token = auth["access_token"]
        assert token == "tok123"

        product = get_product("p1")
        assert product["name"] == "Widget"

        cart = create_cart(token)
        assert cart["id"] == "cart1"

        payment = create_payment_intent(product["price"], "usd")
        assert payment["id"] == "pi_123"

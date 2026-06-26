from helpers import create_order_payload
from api_client import OrdersApi as api
import pytest
import allure

class TestListOrderApi:

    def test_get_order_list_data_200(self):
        response = api.get_order_list(payload=None)
        assert response.status_code == 200
        assert "orders" in response.json() #в тело ответа возвращается список заказов.
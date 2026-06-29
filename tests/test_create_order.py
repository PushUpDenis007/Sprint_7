from helpers import create_order_payload
from api_client import OrdersApi as api
import pytest
import allure

@allure.feature("Проверка создания заказа")
class TestOrderApi:

    @pytest.mark.parametrize("color",[
        ['BLACK', 'GREY'],#можно указать оба цвета;
        ['GREY'],
        ['BLACK'],
        None #можно совсем не указывать цвет;
    ]
    )
    @allure.title("Создание заказа с цветом: {color}")
    def test_create_order_valid_data_201(self,color):
        payload=create_order_payload(color)
        response = api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json() #тело ответа содержит track.
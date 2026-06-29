from api_client import OrdersApi as api
import allure

@allure.feature("Просмотр списка заказов")
class TestListOrderApi:
    @allure.title("Получить список заказов")
    def test_get_order_list_data_200(self):
        response = api.get_order_list(payload=None)
        assert response.status_code == 200
        assert "orders" in response.json() #в тело ответа возвращается список заказов.
from helpers import create_user_payload, delete_courier_from_db
from api_client import CourierApi as api
import pytest
import allure

class TestOrderApi:
    
    def test_login_user_valid_data_200(self,courier_setup): #курьер может авторизоваться;
        payload=courier_setup
        response = api.login_courier(payload)
        assert response.status_code == 200
        assert "id" in response.json() #успешный запрос возвращает id.
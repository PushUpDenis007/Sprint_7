from helpers import create_user_payload, delete_courier_from_db
from api_client import CourierApi as api
import pytest
import allure

class TestCreateApi:
    
    def test_create_user_valid_data_201(self): #курьера можно создать;
        payload=create_user_payload()
        try:
            response = api.create_courier(payload)
            assert response.status_code == 201
            assert response.json() == {"ok": True} #успешный запрос возвращает {"ok":true};
        finally:
            delete_courier_from_db(payload)

    def test_create_user_duplicate_data_409(self, courier_setup): #нельзя создать двух одинаковых курьеров;
        payload=courier_setup
        try:
            response = api.create_courier(payload)
            assert response.status_code == 409 #запрос возвращает правильный код ответа;
            assert "Этот логин уже используется" in response.json().get("message")
        finally:
            if response.status_code == 201:
                delete_courier_from_db(payload) 

    @pytest.mark.parametrize(
        "test_id, modify_payload", [
            ("missing_login", lambda d: d.pop("login")),
            ("missing_password", lambda d: d.pop("password"))
        ]
    )
    def test_create_user_invalid_data_400(self,test_id, modify_payload): #чтобы создать курьера, нужно передать в ручку все обязательные поля;
        allure.dynamic.title(f"Тест создания курьера с ошибкой: {test_id}")
        payload=create_user_payload()
        modify_payload(payload)
        response = api.create_courier(payload)
        assert response.status_code == 400 #запрос возвращает правильный код ответа;
        assert "Недостаточно данных для создания учетной записи" in response.json().get("message") #если одного из полей нет, запрос возвращает ошибку;

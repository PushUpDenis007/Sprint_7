from api_client import CourierApi as api
import pytest
import allure

@allure.feature("Проверка логина юзера")
class TestLoginApi:

    @allure.title("Позитивный логин пользователя")
    def test_login_user_valid_data_200(self,courier_setup): #курьер может авторизоваться;
        payload=courier_setup
        response = api.login_courier(payload)
        assert response.status_code == 200
        assert "id" in response.json() #успешный запрос возвращает id.

    @pytest.mark.parametrize(
        "test_id, modify_payload", [
            ("missing_login", lambda d: d.pop("login")),
            ("missing_password", lambda d: d.pop("password"))
        ]
    )
    @allure.title("Авторизация с пропущенными данными: {test_id}")
    def test_login_user_empty_data_400(self,courier_setup,modify_payload,test_id): #для авторизации нужно передать все обязательные поля;
        payload=courier_setup.copy()
        modify_payload(payload)
        response = api.login_courier(payload)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message") #если какого-то поля нет, запрос возвращает ошибку;

    @pytest.mark.parametrize(
        "test_id, modify_payload", [
            ("wrong_login", lambda d: d.update({"login":"wrong_login"})),
            ("wrong_password", lambda d: d.update({"password":"wrong_password"}))
        ]
    )
    @allure.title("Авторизация с неправильными данными: {test_id}")
    def test_login_user_invalid_data_404(self,courier_setup,modify_payload,test_id):
        payload=courier_setup.copy()
        modify_payload(payload)
        response = api.login_courier(payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message") #система вернёт ошибку, если неправильно указать логин или пароль;



    
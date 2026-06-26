import random
import string
from api_client import CourierApi

# Вспомогательная функция для генерации случайных уникальных логинов
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

#функция упаковки данных в словарь
def create_user_payload():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

def delete_courier_from_db(payload):
    login_resp = CourierApi.login_courier({
        "login": payload["login"],
        "password": payload["password"]
    })
    if login_resp.status_code == 200:
        courier_id = login_resp.json().get("id")
        CourierApi.delete_courier(courier_id)
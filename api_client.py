import requests
from urls import Urls

class CourierApi:

    @staticmethod
    def create_courier(payload): #Метод для отправки запроса на создание курьера
        url = f'{Urls.BASE_URL}/api/v1/courier'
        response = requests.post(url, data=payload)
        return response
    
    @staticmethod 
    def login_courier(payload): #Метод для отправки запроса на login курьера
        url = f'{Urls.BASE_URL}/api/v1/courier/login'
        response = requests.post(url, data=payload)
        return response
    
    @staticmethod
    def delete_courier(id): #Метод для отправки запроса на delete курьера
        url = f'{Urls.BASE_URL}/api/v1/courier/{id}'
        response = requests.delete(url)
        return response
import allure
import requests
from data import Data
from helpers import create_email_user_random, create_user_pass_random, create_user_name_random


class TestGetListOrder:
    @allure.title('Проверка получения списка заказов c авторизованным конкретным пользователем')
    @allure.description(
        'Проверяем получение списка заказов, получаем статус 200 и проверяем, что список не пустой')
    def test_get_list_order(self):
        user = {
            'email': create_email_user_random(),
            'password': create_user_pass_random(),
            'name': create_user_name_random()
        }
        requests.post(Data.Url_create_user, data=user)
        login = requests.post(Data.Url_login_user, data=user)
        token = login.json()['accessToken']
        response = requests.get(Data.Url_orders_from_user, headers={'Authorization': token}, data=user)
        assert response.status_code == 200

    @allure.title('Проверка получения списка заказов c неавторизованным конкретным пользователем')
    @allure.description(
        'Проверяем получение списка заказов, получаем статус 401 и проверяем, что список не пустой')
    def test_get_list_order(self):
        user = {
            'email': create_email_user_random(),
            'password': create_user_pass_random(),
            'name': create_user_name_random()
        }
        requests.post(Data.Url_create_user, data=user)
        response = requests.get(Data.Url_orders_from_user, data=user)
        assert response.status_code == 401

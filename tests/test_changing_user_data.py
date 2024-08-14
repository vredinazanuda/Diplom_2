import allure
import requests
from data import Data
from helpers import create_email_user_random, create_user_pass_random, create_user_name_random


class TestChangingUserData:
    @allure.title('Проверка изменения данных пользователя с авторизацией')
    @allure.description('Создаем аккаунт пользователя, логинимся на него и изменяем данные')
    def test_changing_user_data_from_authorization(self):
        user_1 = {'email': create_email_user_random(),
                  'password': create_user_pass_random(),
                  'name': create_user_name_random()
                  }
        user_2 = {'email': create_email_user_random(),
                  'password': create_user_pass_random(),
                  'name': create_user_name_random()
                  }
        requests.post(Data.Url_create_user, data=user_1)
        user_data = requests.post(Data.Url_login_user, data=user_1)
        token = user_data.json()['accessToken']
        response = requests.get(Data.Url_changing_user_data, headers={'Authorization': token}, data=user_2)
        assert response.status_code == 200

    @allure.title('Проверка изменения данных пользователя без авторизации')
    @allure.description('Попытка изменить данные пользователя без авторизации, ожидаем получение ошибки')
    def test_changing_user_data_without_authorization(self):
        user_1 = {'email': create_email_user_random(),
                  'password': create_user_pass_random(),
                  'name': create_user_name_random()
                  }
        user_2 = {'email': create_email_user_random(),
                  'password': create_user_pass_random(),
                  'name': create_user_name_random()
                  }
        requests.post(Data.Url_create_user, data=user_1)
        response = requests.get(Data.Url_changing_user_data, data=user_2)
        assert response.status_code == 401

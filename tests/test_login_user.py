import allure
import requests
from data import Data, DataMy
from helpers import create_email_user_random, create_user_pass_random, create_user_name_random


class TestLoginUser:
    @allure.title('Проверка успешного логина пользователя')
    @allure.description(
        'Создаём аккаунт пользователя и логинимся на него, получаем статус 200')
    def test_user_login_passed(self):
        payload = {'email': DataMy.email,
                   'password': DataMy.password,
                   'name': DataMy.name
                   }
        response = requests.post(Data.Url_login_user, data=payload)
        del payload["password"]
        assert (response.status_code == 200
                and response.json()["success"] == True
                and response.json()["user"] == payload)

    @allure.title('Проверка логина c неправильным логином')
    @allure.description(
        'Пытаемся залогиниться в аккаунт пользователя, получаем ошибку 401 и соотвествующее сообщение')
    def test_no_such_login(self):
        payload = {'email': DataMy.incorrect_login,
                   'password': create_user_pass_random(),
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.Url_login_user, data=payload)
        assert (response.status_code == 401
                and response.json()["success"] == False
                and response.json()["message"] == "email or password are incorrect")

    @allure.title('Проверка логина c неправильным паролем')
    @allure.description(
        'Пытаемся залогиниться в аккаунт пользователя, получаем ошибку 401 и соотвествующее сообщение')
    def test_no_such_password(self):
        payload = {'email': create_email_user_random(),
                   'password': DataMy.incorrect_password,
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.Url_login_user, data=payload)
        assert (response.status_code == 401
                and response.json()["success"] == False
                and response.json()["message"] == "email or password are incorrect")

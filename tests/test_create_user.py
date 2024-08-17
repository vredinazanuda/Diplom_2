import allure
import requests
from data import Data, DataMy
from helpers import create_email_user_random, create_user_pass_random, create_user_name_random


class TestNewUserCreate:
    @allure.title('Проверка создания пользователя')
    @allure.description('Создаём пользователя и проверяем, что код ответа равен 200 и тело ответа соотвествует '
                        'документации')
    def test_create_user(self):
        payload = {'email': create_email_user_random(),
                   'password': create_user_pass_random(),
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.Url_create_user, data=payload)
        del payload["password"]
        assert (response.status_code == 200
                and response.json()["success"] == True
                and response.json()["user"] == payload)

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    @allure.description('Создаём пользователя и проверяем, что код ответа равен 403 и тело ответа соотвествует '
                        'документации')
    def test_duplicate_create_user(self):
        payload = {'email': DataMy.email,
                   'password': create_user_pass_random(),
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.Url_create_user, data=payload)
        print(response.text)
        assert (response.status_code == 403
                and response.json()["success"] == False
                and response.json()["message"] == "User already exists")


    @allure.title('Проверка невозможности создания пользователя без одного обязательного поля')
    @allure.description('Посылаем запрос без поля "Пароль" и пытаемся создать аккаунт, получаем ошибку 403 и её текст')
    def test_not_once_required_field(self):
        payload = {'email': create_email_user_random(),
                   'name': create_user_name_random()
                   }
        response = requests.post(Data.Url_create_user, data=payload)
        assert (response.status_code == 403
                and response.json()["success"] == False
                and response.json()["message"] == "Email, password and name are required fields")
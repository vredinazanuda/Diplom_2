import allure
import requests
from data import Data, BurgerIngredients
from helpers import create_email_user_random, create_user_pass_random, create_user_name_random


class TestCreateOrder:
    @allure.title('Проверка создания заказа с ингредиентами авторизованным пользователем')
    @allure.description(
        'При создании заказа передаются существующие ингредиенты авторизованным созданным пользователем')
    def test_create_order_ingredients_authorized_user(self):
        user = {'email': create_email_user_random(),
                'password': create_user_pass_random(),
                'name': create_user_name_random()
                }
        requests.post(Data.Url_login_user, data=user)
        requests.get(Data.Url_login_user, data=user)
        response = requests.post(Data.Url_create_order, data=BurgerIngredients.burger_existing)
        assert response.status_code == 200

    @allure.title('Проверка создания заказа с ингредиентами  неавторизованным пользователем')
    @allure.description('При создании заказа передаются существующие ингредиенты неавторизованным пользователем')
    def test_create_order_ingredients_unauthorized_user(self):
        user = {'email': create_email_user_random(),
                'password': create_user_pass_random(),
                'name': create_user_name_random()
                }
        requests.post(Data.Url_login_user, data=user)
        response = requests.post(Data.Url_create_order, data=BurgerIngredients.burger_existing)
        assert response.status_code == 200

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('При создании заказа не передаются ингредиенты ')
    def test_create_order_authorized_user_no_ingredients(self):
        user = {'email': create_email_user_random(),
                'password': create_user_pass_random(),
                'name': create_user_name_random()
                }
        requests.post(Data.Url_login_user, data=user)
        response = requests.post(Data.Url_create_order, data=BurgerIngredients.burger_empty)
        assert response.status_code == 400

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов авторизованным пользователем')
    @allure.description('При создании заказа авторизованным  пользователем не передаются ингредиенты с неверным хешем')
    def test_create_order_authorized_user_bad_ingredients_hash_error(self):
        user = {'email': create_email_user_random(),
                'password': create_user_pass_random(),
                'name': create_user_name_random()
                }
        requests.post(Data.Url_login_user, data=user)
        response = requests.post(Data.Url_create_order, data=BurgerIngredients.non_existent_burger)
        assert response.status_code == 500

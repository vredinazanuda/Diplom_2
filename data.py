class Data:
    Url_main_page = 'https://stellarburgers.nomoreparties.site/'
    Url_create_user = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    Url_login_user = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    Url_changing_user_data = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    Url_create_order = 'https://stellarburgers.nomoreparties.site/api/orders'
    Url_orders_from_user = 'https://stellarburgers.nomoreparties.site/api/orders'


class DataMy:

    name = 'Ксения'
    email = "zavalishina--kseniia@ya.ru"
    password = 'meow1meoW2'
    incorrect_password = 'regsgq3F4t'
    incorrect_login = 'ehshariktikakiyabilnatsepi@ya.ru'


class BurgerIngredients:
    burger_existing = {'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    non_existent_burger = {'ingredients': ['35c0c5d1fр82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    burger_empty = {'ingredients': ''}

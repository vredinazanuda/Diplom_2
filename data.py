class Data:
    base_Url = "stellarburgers.nomoreparties.site"
    Url_main_page = f'https://{base_Url}/'
    Url_create_user = f'https://{base_Url}/api/auth/register'
    Url_login_user = f'https://{base_Url}/api/auth/login'
    Url_changing_user_data = f'https://{base_Url}/api/auth/user'
    Url_create_order = f'https://{base_Url}/api/orders'
    Url_orders_from_user = f'https://{base_Url}/api/orders'


class DataMy:

    name = 'Ксения'
    email = "zavalishina--kseniia1@ya.ru"
    password = 'meow1meoW2'
    incorrect_password = 'regsgq3F4t'
    incorrect_login = 'ehshariktikakiyabilnatsepi@ya.ru'


class BurgerIngredients:
    burger_existing = {'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    burger_existing_check = "Бессмертный флюоресцентный бургер"
    non_existent_burger = {'ingredients': ['35c0c5d1fр82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    burger_empty = {'ingredients': ''}

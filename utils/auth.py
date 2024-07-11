import allure
import requests
from data.all_data import Links

@allure.step("Регистрация пользователя(рандом)")
def register_user(user_data):
    response = requests.post(f"{Links.BASE_URL}{Links.register_handler}", json=user_data)
    return response.json()

@allure.step("Регистрация пользователя известного")
def register_concrete_user(user_data):
    response = requests.post(f"{Links.BASE_URL}{Links.register_handler}", json=user_data)
    return response.json()

@allure.step("Логин юзера")
def login_user(user_data):
    response = requests.post(f"{Links.BASE_URL}{Links.login_handler}", json=user_data)
    return response.json()

@allure.step("Логаут юзера")
def logout_user(refresh_token):
    response = requests.post(f"{Links.BASE_URL}{Links.logout_handler}", json={"token": refresh_token})
    return response.json()

@allure.step("Обновить токен")
def refresh_token(refresh_token):
    response = requests.post(f"{Links.BASE_URL}{Links.token_handler}", json={"token": refresh_token})
    return response.json()


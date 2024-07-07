import allure
import requests
import random

BASE_URL = "https://stellarburgers.nomoreparties.site/api"
new_email = f"denis_pcheliakov_8{random.randint(100, 999)}@yandex.ru"

@allure.step("Регистрация пользователя(рандом)")
def register_user(user_data):
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    return response.json()

@allure.step("Регистрация пользователя известного")
def register_concrete_user(user_data):
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    return response.json()

@allure.step("Логин юзера")
def login_user(user_data):
    response = requests.post(f"{BASE_URL}/auth/login", json=user_data)
    return response.json()

@allure.step("Логаут юзера")
def logout_user(refresh_token):
    response = requests.post(f"{BASE_URL}/auth/logout", json={"token": refresh_token})
    return response.json()

@allure.step("Обновить токен")
def refresh_token(refresh_token):
    response = requests.post(f"{BASE_URL}/auth/token", json={"token": refresh_token})
    return response.json()


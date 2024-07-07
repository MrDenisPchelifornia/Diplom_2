import allure
import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

@allure.step("Создание заказа")
def create_order(ingredients, access_token=None):
    headers = {"Authorization": access_token} if access_token else {}
    response = requests.post(f"{BASE_URL}/orders", json={"ingredients": ingredients}, headers=headers)
    return response.json()

@allure.step("Получить информацию о заказе юзера")
def get_user_orders(access_token):
    headers = {"Authorization": access_token} if access_token else {}
    response = requests.get(f"{BASE_URL}/orders", headers=headers)
    return response.json()



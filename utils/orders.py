import allure
import requests
from data.all_data import Links

@allure.step("Создание заказа")
def create_order(ingredients, access_token=None):
    headers = {"Authorization": access_token} if access_token else {}
    response = requests.post(f"{Links.BASE_URL}{Links.order_handler}", json={"ingredients": ingredients}, headers=headers)
    return response.status_code, response.json()

@allure.step("Получить информацию о заказе юзера")
def get_user_orders(access_token):
    headers = {"Authorization": access_token} if access_token else {}
    response = requests.get(f"{Links.BASE_URL}{Links.order_handler}", headers=headers)
    return response.status_code, response.json()

import allure
import requests
from data.all_data import Links

@allure.step("Получить информацию о юзере")
def get_user_info(access_token):
    headers = {"Authorization": access_token}
    response = requests.get(f"{Links.BASE_URL}{Links.auth_handler}", headers=headers)
    return response.json()

@allure.step("Обновить данные о пользователе")
def update_user_info(access_token, update_data):
    headers = {"Authorization": access_token}
    response = requests.patch(f"{Links.BASE_URL}{Links.auth_handler}", json=update_data, headers=headers)
    return response.json()

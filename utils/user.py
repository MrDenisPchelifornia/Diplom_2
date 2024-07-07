import allure
import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

@allure.step("Получить информацию о юзере")
def get_user_info(access_token):
    headers = {"Authorization": access_token}
    response = requests.get(f"{BASE_URL}/auth/user", headers=headers)
    return response.json()

@allure.step("Обновить данные о пользователе")
def update_user_info(access_token, update_data):
    headers = {"Authorization": access_token}
    response = requests.patch(f"{BASE_URL}/auth/user", json=update_data, headers=headers)
    return response.json()

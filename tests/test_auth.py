import allure
import pytest
from utils.auth import login_user, logout_user

@allure.title('ПРоверка логина')
def test_login_user():
    user_data = {"email": "denis_pcheliakov@yandex.ru", "password": "password123"}
    response = login_user(user_data)
    assert response["success"] is True
    assert "accessToken" in response

@allure.title('Попытка логина с некорректными данными')
def test_login_user_wrong_credentials():
    user_data = {"email": "wrong@yandex.ru", "password": "wrongpassword"}
    response = login_user(user_data)
    assert response["success"] is False
    assert response["message"] == "email or password are incorrect"

@allure.title('Проверка на разлогин')
def test_logout_user(user_auth):
    refresh_token = user_auth["refreshToken"]
    response = logout_user(refresh_token)
    assert response["success"] is True
    assert response["message"] == "Successful logout"


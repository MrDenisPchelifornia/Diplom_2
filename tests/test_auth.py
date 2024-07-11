import allure
import pytest
from utils.auth import login_user, logout_user
from data.all_data import Users, Asserts


@allure.title('Проверка логина')
def test_login_user():
    user_data = Users.valid_user
    response = login_user(user_data)
    assert response["success"] is True
    assert "accessToken" in response

@allure.title('Попытка логина с некорректными данными')
def test_login_user_wrong_credentials():
    user_data = Users.invalid_user
    response = login_user(user_data)
    assert response["success"] is False
    assert response["message"] == Asserts.login_failure_message

@allure.title('Проверка на разлогин')
def test_logout_user(user_auth):
    refresh_token = user_auth["refreshToken"]
    response = logout_user(refresh_token)
    assert response["success"] is True
    assert response["message"] == Asserts.successful_logout






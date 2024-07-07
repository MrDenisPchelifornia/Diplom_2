import allure
import pytest
from utils.user import get_user_info, update_user_info
from utils.auth import register_concrete_user, register_user, new_email

@allure.title('Проверка создания уникального пользователя')
def test_create_unique_user():
    user_data = {"email": new_email, "password": "password123", "name": "Unique User"}
    response = register_user(user_data)
    assert response["success"] is True

@allure.title('Проверка создания существующего пользователя')
def test_create_existing_user():
    user_data = {"email": "test@yandex.ru", "password": "password123", "name": "Test User"}
    register_concrete_user(user_data)
    response = register_user(user_data)
    assert response["success"] is False
    assert response["message"] == "User already exists"

@allure.title('Проверка создания пользователя с пропущенными данными')
def test_create_user_missing_field():
    user_data = {"email": new_email, "password": "password123"}
    response = register_user(user_data)
    assert response["success"] is False
    assert response["message"] == "Email, password and name are required fields"

@allure.title('Проверка получения данных о юзере')
def test_get_user_info(user_auth):
    access_token = user_auth["accessToken"]
    response = get_user_info(access_token)
    assert response["success"] is True
    assert response["user"]["email"] == "denis_pcheliakov@yandex.ru"
    assert response["user"]["name"] == "Unique User"

@allure.title('Проверка обновления информации юзера')
def test_update_user_info(user_auth):
    access_token = user_auth["accessToken"]
    update_data = {"name": "Name2.0"}
    response = update_user_info(access_token, update_data)
    assert response["success"] is True
    assert response["user"]["name"] == "Name2.0"
    update_data = {"name": "Unique User"}
    update_user_info(access_token, update_data)

@allure.title('Попытка обновить информацию неавторизованному юзеру')
def test_update_user_info_not_authorized():
    update_data = {"name": "Name2.0"}
    response = update_user_info(None, update_data)
    assert response["success"] is False
    assert response["message"] == "You should be authorised"

import allure
import pytest
from utils.user import get_user_info, update_user_info
from utils.auth import register_concrete_user, register_user
from data.all_data import Users, Asserts

@allure.title('Проверка создания уникального пользователя')
def test_create_unique_user():
    user_data = Users.new_user
    response = register_user(user_data)
    assert response['success'] is True

@allure.title('Проверка создания существующего пользователя')
def test_create_existing_user():
    user_data = Users.test_user
    register_concrete_user(user_data)
    response = register_user(user_data)
    assert response["success"] is False
    assert response["message"] == Asserts.expect_message_for_exists_user

@allure.title('Проверка создания пользователя с пропущенными данными')
def test_create_user_missing_field():
    user_data = Users.user_with_required_fields
    response = register_user(user_data)
    assert response["success"] is False
    assert response["message"] == Asserts.expect_message_for_required_fields

@allure.title('Проверка получения данных о юзере')
def test_get_user_info(user_auth):
    access_token = user_auth["accessToken"]
    response = get_user_info(access_token)
    assert response["success"] is True
    assert response["user"]["email"] == Asserts.expect_email_for_user
    assert response["user"]["name"] == Asserts.expect_name1_for_user

@allure.title('Проверка обновления информации юзера')
def test_update_user_info(user_auth):
    access_token = user_auth["accessToken"]
    update_data = Users.update_data_1
    response = update_user_info(access_token, update_data)
    assert response["success"] is True
    assert response["user"]["name"] == Asserts.expect_name2_for_user
    update_data = Users.update_data_2
    update_user_info(access_token, update_data)

@allure.title('Попытка обновить информацию неавторизованному юзеру')
def test_update_user_info_not_authorized():
    update_data = Users.update_data_1
    response = update_user_info(None, update_data)
    assert response["success"] is False
    assert response["message"] == Asserts.expect_text_for_not_authorized_user

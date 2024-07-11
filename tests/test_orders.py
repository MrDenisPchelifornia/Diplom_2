import allure
import pytest
from utils.orders import create_order, get_user_orders
from utils.auth import login_user, refresh_token
from conftest import user_auth
from data.all_data import Asserts, Correct_Ingradients, Uncorrect_Ingradients

@allure.title('Проверка создания заказа авторизованным пользователем')
def test_create_order_with_authorization(user_auth):
    access_token = user_auth["accessToken"]
    ingredients = [Correct_Ingradients.ingradients_c_1, Correct_Ingradients.ingradients_c_2]
    status_code, response = create_order(ingredients, access_token)
    assert status_code == 200
    assert response["success"] is True

@allure.title('Проверка создания заказа НЕ авторизованным пользователем')
def test_create_order_without_authorization(user_auth):
    ingredients = [Correct_Ingradients.ingradients_c_3, Correct_Ingradients.ingradients_c_4]
    status_code, response = create_order(ingredients)
    assert status_code == 200
    assert response["success"] is True

@allure.title('Проверка создания заказа с некорретными номерами инградиентов')
def test_create_order_with_invalid_hash(user_auth):
    access_token = user_auth["accessToken"]
    ingredients = [Uncorrect_Ingradients.ingradients_uc_1, Uncorrect_Ingradients.ingradients_uc_2]
    status_code, response = create_order(ingredients, access_token)
    assert status_code == 400
    assert response["success"] is False
    assert response["message"] == Asserts.make_order_with_uncorrect_ingradients

@allure.title('Проверка получения детлей заказа авторизованным юзером')
def test_get_user_orders_with_authorization(user_auth):
    access_token = user_auth["accessToken"]
    status_code, response = get_user_orders(access_token)
    assert status_code == 200
    assert response["success"] is True

@allure.title('Проверка получения детлей заказа НЕ авторизованным юзером')
def test_get_user_orders_without_authorization():
    status_code, response = get_user_orders(None)
    assert status_code == 401
    assert response["success"] is False
    assert response["message"] == Asserts.get_order_without_authorization

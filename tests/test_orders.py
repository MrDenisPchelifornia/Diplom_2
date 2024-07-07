import allure
import pytest
from utils.orders import create_order, get_user_orders
from utils.auth import login_user, refresh_token
from conftest import user_auth

@allure.title('Проверка создания заказа авторизованным пользователем')
def test_create_order_with_authorization(user_auth):
    access_token = user_auth["accessToken"]
    ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    response = create_order(ingredients, access_token)
    assert response["success"] is True

@allure.title('Проверка создания заказа НЕ авторизованным пользователем')
def test_create_order_without_authorization(user_auth):
    ingredients = ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]
    response = create_order(ingredients)
    assert response["success"] is True

@allure.title('Проверка создания заказа с некорретными номерами инградиентов')
def test_create_order_with_invalid_hash(user_auth):
    access_token = user_auth["accessToken"]
    ingredients = ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]
    response = create_order(ingredients, access_token)
    assert response["success"] is False
    assert response["message"] == "One or more ids provided are incorrect"

@allure.title('Проверка получения детлей заказа авторизованным юзером')
def test_get_user_orders_with_authorization(user_auth):
    access_token = user_auth["accessToken"]
    response = get_user_orders(access_token)
    assert response["success"] is True

@allure.title('Проверка получения детлей заказа НЕ авторизованным юзером')
def test_get_user_orders_without_authorization():
    response = get_user_orders(None)
    assert response["success"] is False
    assert response["message"] == "You should be authorised"


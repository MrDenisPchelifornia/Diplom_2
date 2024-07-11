import random

class Users:
    valid_user = {
        "email": "denis_pcheliakov@yandex.ru",
        "password": "password123"
    }

    invalid_user = {
        "email": "wrong@yandex.ru",
        "password": "wrongpassword"
    }

    standart_user = {
        "email": "denis_pcheliakov@yandex.ru",
        "password": "password123",
        "name": "Unique User"
    }

    new_email = f"denis_pcheliakov_8{random.randint(100, 999)}@yandex.ru"

    new_user = {
        "email": new_email,
        "password": "password123",
        "name": "Unique User"
    }

    test_user = {
        "email": "test@yandex.ru",
        "password": "password123",
        "name": "Test User"
    }

    user_with_required_fields = {
        "email": new_email,
        "password": "password123"
    }

    update_data_1 = {
        "name": "Name2.0"
    }

    update_data_2 = {
        "name": "Unique User"
    }

class Asserts:
    login_failure_message = "email or password are incorrect"
    successful_logout = "Successful logout"
    get_order_without_authorization = "You should be authorised"
    make_order_with_uncorrect_ingradients = "One or more ids provided are incorrect"
    expect_message_for_required_fields = "Email, password and name are required fields"
    expect_message_for_exists_user = "User already exists"
    expect_email_for_user = "denis_pcheliakov@yandex.ru"
    expect_name1_for_user = "Unique User"
    expect_name2_for_user = "Name2.0"
    expect_text_for_not_authorized_user = "You should be authorised"

class Links:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    register_handler = "/auth/register"
    login_handler = "/auth/login"
    logout_handler = "/auth/logout"
    token_handler = "/auth/token"
    order_handler = "/orders"
    auth_handler = "/auth/user"

class Correct_Ingradients:
    ingradients_c_1 = "61c0c5a71d1f82001bdaaa6d"
    ingradients_c_2 = "61c0c5a71d1f82001bdaaa6f"
    ingradients_c_3 = "61c0c5a71d1f82001bdaaa70"
    ingradients_c_4 = "61c0c5a71d1f82001bdaaa71"


class Uncorrect_Ingradients:
    ingradients_uc_1 = "60d3b41abdacab0026a733c6"
    ingradients_uc_2 = "609646e4dc916e00276b2870"
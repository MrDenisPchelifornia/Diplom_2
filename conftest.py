import pytest
from utils.auth import login_user, register_user

@pytest.fixture(scope='session')
def user_auth():
    user_data = {"email": "denis_pcheliakov@yandex.ru", "password": "password123", "name": "Unique User"}
    register_user(user_data)
    tokens = login_user(user_data)
    return tokens



import pytest
from utils.auth import login_user, register_user
from data.all_data import Users

@pytest.fixture(scope='session')
def user_auth():
    user_data = Users.standart_user
    register_user(user_data)
    tokens = login_user(user_data)
    return tokens


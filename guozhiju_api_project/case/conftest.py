import requests
import pytest
from case.common_api.api_login import login


@pytest.fixture(scope="session")
def login_fixture():
    s = requests.session()
    login(s, username="18896586050", password="eyJrZXkiOiJwYXQjc25hcCRpcyVnb29kIiwicHdkIjoiYTEyMzQ1NiIsInRva2VuIjoiNDVkMzJkYzliZDU5OGRlOGRmOWY0OTgwYzY2MjZmYjUifQ==")
    print("已登录")
    return s


@pytest.fixture(scope="function")
def unlogin_fixture():
    s = requests.session()
    yield s
    print("未登录")

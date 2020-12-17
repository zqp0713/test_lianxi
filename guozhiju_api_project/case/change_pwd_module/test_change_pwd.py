from case.common_api.api_login import change_pwd
import pytest
from setting import base_path
from common.read_yaml import read_yaml
import os
import allure

yaml_path = os.path.join(base_path, "testdata", "test_psw.yml")

# 测试数据
testdata_orgpwd = read_yaml(yaml_path)["orginpwd"]


@allure.feature("修改密码模块")
class Test_change_pwd():
    """修改密码-原始密码"""

    @allure.story("输入旧密码，失败")
    @pytest.mark.parametrize("test_input,expected", testdata_orgpwd)
    def test_change_psw_orgin_fail(self, login_fixture, test_input, expected):
        """修改密码-输入旧密码-失败"""
        s = login_fixture
        r = change_pwd(s, orgpwd=test_input["orgpwd"], newpwd="a123456", confpwd="a123456")
        assert r.json()["data"]["code"] == expected["code"]
        assert r.json()["data"]["msg"] == expected["msg"]

    @allure.story("输入旧密码，成功")
    def test_change_psw_orgin_success(self, login_fixture):
        """修改密码-输入旧密码-成功"""
        s = login_fixture
        r = change_pwd(s, orgpwd="eyJrZXkiOiJwYXQjc25hcCRpcyVnb29kIiwicHdkIjoiYTEyMzQ1NiIsInRva2VuIjoiNDVkMzJkYzliZDU5OGRlOGRmOWY0OTgwYzY2MjZmYjUifQ==",
                       newpwd="eyJrZXkiOiJwYXQjc25hcCRpcyVnb29kIiwicHdkIjoiYTEyMzQ1NiIsInRva2VuIjoiNDVkMzJkYzliZDU5OGRlOGRmOWY0OTgwYzY2MjZmYjUifQ==",
                       confpwd="eyJrZXkiOiJwYXQjc25hcCRpcyVnb29kIiwicHdkIjoiYTEyMzQ1NiIsInRva2VuIjoiNDVkMzJkYzliZDU5OGRlOGRmOWY0OTgwYzY2MjZmYjUifQ==")
        assert r.json()["data"]["code"] == 200
        assert r.json()["data"]["msg"] == "修改密码成功"




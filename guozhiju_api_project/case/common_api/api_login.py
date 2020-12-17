# coding:utf-8
import requests
import json
import os
from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager(logger_name="api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                   log_filename="api.log",
                                                                   log_path=LOG_PATH)


def login(s, username, password):
    """
    登录
    :param s:
    :param username:
    :param password:
    :return: 返回token
    """
    url = os.environ["host"]+"/1.0/users/users/loginsubmit"
    body = {"username": username,
            "password": password
            }

    r = s.post(url, json=body, verify=False)
    logger.debug("\n登录返回的结果：%s" % r.text)
    res = r.json()
    token = res["data"]["sid"]
    h = {"Authorization": token}
    s.headers.update(h)
    return token


def userinfo(s):
    """个人设置"""
    url = os.environ["host"]+"/1.0/users/users/latest_userinfo"
    r = s.get(url)
    logger.debug("\n个人设置get返回的结果：%s" % r.text)
    r = r.json()   # 响应结果转为json，再去格式化响应内容
    return json.dumps(r, indent=4, ensure_ascii=False)   # ensure_ascii解码显示中文  indent=4 每行字数


def change_userinfo(s,mobile, identify, sex, province, city, county):
    """修改个人设置"""
    url = os.environ["host"]+"/1.0/users/users/change_userinfo"
    body = {"User":
                {
                    "name": "吴昕然",
                    "mobile": mobile,
                    "slide_code": "",
                    "verify": "",
                    "identify_type": "1",
                    "identify": identify,
                    "identify_effective_date": "",
                    "country": "",
                    "sex": sex,
                    "birthday": "",
                    "province": province,
                    "city": city,
                    "county": county,
                    "company": "原生科技——qa",
                    "company_position": "122",
                    "email": "",
                    "address": "苏州",
                    "register_type": "E-1"
                }
            }
    r = s.post(url, json=body)
    logger.debug("\n修改个人设置返回的结果：%s" % r.text)
    return r


def change_pwd(s,orgpwd, newpwd, confpwd):
    url = os.environ["host"]+"/1.0/users/users/change_pwd"
    body = {
        "User":
            {
                "origin_pwd": orgpwd,
                "new_pwd": newpwd,
                "new_pwd_confirm": confpwd
            }
    }
    r = s.post(url, json=body,verify=False)
    logger.debug("\n修改密码返回的结果：%s" % r.text)
    return r


def logout(s):
    """登出"""
    url = os.environ["host"]+"/1.0/users/users/logout"
    r = s.post(url)
    logger.debug("\n退出登录返回的结果：%s" % r.text)
    return r







if __name__ == '__main__':
    s = requests.session()
    os.environ["host"] = "https://qa-cnipa-webapi.zhihuiya.com"
    token = login(s, "18896586050", "eyJrZXkiOiJwYXQjc25hcCRpcyVnb29kIiwicHdkIjoiYTEyMzQ1NiIsInRva2VuIjoiNDVkMzJkYzliZDU5OGRlOGRmOWY0OTgwYzY2MjZmYjUifQ==")
    # print(token)
    # r = userinfo(s)
    res = change_pwd(s, orgpwd="eyJrZXkiOiJwYXQjc25hcCRpcyVnb29kIiwicHdkIjoiYTEyMzQ1NiIsInRva2VuIjoiNDVkMzJkYzliZDU5OGRlOGRmOWY0OTgwYzY2MjZmYjUifQ==",
                     newpwd="eyJrZXkiOiJwYXQjc25hcCRpcyVnb29kIiwicHdkIjoiYTEyMzQ1NiIsInRva2VuIjoiNDVkMzJkYzliZDU5OGRlOGRmOWY0OTgwYzY2MjZmYjUifQ==",
                     confpwd="eyJrZXkiOiJwYXQjc25hcCRpcyVnb29kIiwicHdkIjoiYTEyMzQ1NiIsInRva2VuIjoiNDVkMzJkYzliZDU5OGRlOGRmOWY0OTgwYzY2MjZmYjUifQ==")
    # r = logout(s)
    # print(r.text)
    print(res.text)

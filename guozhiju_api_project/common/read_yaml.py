import yaml
import os


def read_yaml(yml_path):
    """读取yaml文件数据"""
    f = open(yml_path, "r", encoding="utf-8")
    rf = f.read()
    # print(rf)
    r = yaml.load(rf)   # yaml 转 python dict
    return r


if __name__ == "__main__":
    cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # print(cur_path)
    yml_path = os.path.join(cur_path, "testdata", "test_psw.yml")
    r = read_yaml(yml_path)["orginpwd"]
    print(r)

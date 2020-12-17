import os
import pytest

# 配置全局host地址
# 添加命令行参数.parser是内置 fixture
# 只需要切换host地址，不用打开代码时，直接在命令行执行用例时使用

def pytest_addoption(parser):
    """配置全局默认test地址"""
    parser.addoption(
        "--cmdhost", action="store",default="https://qa-cnipa-webapi.zhihuiya.com",
        help="my option:test or pre"
    )


@pytest.fixture(scope="session",autouse=True)
def host(request):
    """读取设置的host地址"""
    os.environ["host"] = request.config.getoption("--cmdhost")

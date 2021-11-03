import pytest
from common.db_link import *
# import requests
import pymysql
@pytest.fixture(scope="session")
def method():
    print("测试前")
    link_mysql("DELETE FROM users WHERE user_name='wjz';", "database.ini", "dev")
    yield
    print("测试后")
    link_mysql("DELETE FROM users WHERE user_name='wjz';","database.ini","dev")

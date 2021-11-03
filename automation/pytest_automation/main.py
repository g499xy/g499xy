#coding:utf-8
import pytest
import allure
import requests
import os
import yaml
import scapy
from testCases.test_01 import Test_Cases

# path=os.path.split(os.path.realpath(__file__))[0]
# with open(path + "/case.yaml", 'r', encoding="utf-8") as load_f:
#     project_dict = yaml.load(load_f)
# # print(project_dict)
if __name__ == '__main__':
    pytest.main([
                 '-s',
                 '-m api or smoking',
                 '--alluredir=report',
                 ])
    os.popen("allure generate report -o result/ --clean")
    # os.popen("allure open -h 0.0.0.0 -p 8083 report/")
    # os.popen("allure serve ./report/index")

# url='http://localhost:9527/user/regist'
# body={"username":"root",
# "password":"123456"}
# result=requests.post(url=url,json=body)
# print(result.text)

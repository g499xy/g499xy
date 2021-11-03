'''
author:zjw
'''
#coding:utf-8
import pytest
import allure
import os
import requests
import json
from common.get_data import *
from testCases.testData import *

@allure.feature("测试商品")
class Test_Cases():
    @pytest.mark.process
    @pytest.mark.parametrize("data,expect_result", [(1, 2), (3, 4)])
    def test_one(self,method,data,expect_result):
        print(data)
        print(expect_result)
        # assert data == expect_result

    @pytest.mark.smoking
    @pytest.mark.parametrize("time", [1, 4])
    def test_two(self,method,time):
        print(time)

    @pytest.mark.smoking
    def test_three(self,method):
        print("a")

    def test_four(self,method):
        print("b")

    path = os.path.split(os.path.realpath(__file__))[0]
    print(path)

    @allure.story("测试功能")
    @pytest.mark.api
    @pytest.mark.parametrize("body,expect",combBodyResult(replace_keyword(get_data(path,"\\testData\\case.yaml"),bodyDemo.regist_api_body),get_result(path,"\\testData\\case.yaml","check")))
    def test_api(self,body,expect,method):
        self.url="http://localhost:9527/user/regist"
        result=requests.post(url=self.url,json=body)
        assert expect['code']==result.status_code
        print(expect['returnBody'] )
        assert set(expect['returnBody']).issubset(set(json.loads(result.text)))

@allure.feature("测试原料")
class Test_otherClass():
    @pytest.mark.smoking
    @pytest.mark.parametrize("time", [1, 4])
    def test_five(self, method, time):
        print(time)






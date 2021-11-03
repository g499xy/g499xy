import os
import yaml
import jsonpath
import copy
from testCases.testData import  bodyDemo
def get_data(filePath,filename):
    with open(filePath + filename, 'r', encoding="utf-8") as load_f:
        project_dict = yaml.load(load_f)
        # print(project_dict)
        dict=jsonpath.jsonpath(project_dict,"$..parameter")
        # print(dict)
    return dict

def get_result(filePath,filename,keyword):
    with open(filePath + filename, 'r', encoding="utf-8") as load_f:
        project_dict = yaml.load(load_f)
        # print(project_dict)
        dict = jsonpath.jsonpath(project_dict, "$..%s"%keyword)
        # print(dict)
    return dict

def replace_keyword(replaceBody,body):
    lstBody=[]
    for i in range(0,len(replaceBody)):
        newBody = copy.copy(body)
        for key in replaceBody[i].keys():
            newBody[key]=replaceBody[i][key]
        lstBody.append(newBody)
    return lstBody

def combBodyResult(body,expect):
    lstComb=list(zip(body,expect))
    return lstComb
if __name__ == '__main__':
    path = os.path.split(os.path.realpath(__file__))[0]
    a=get_data("D:\\PycharmProjects\\pytest_automation\\testCases\\testData","\case.yaml")
    print(a)
    b=replace_keyword(a,bodyDemo.regist_api_body)
    print(b)
    expect_code=[400,200,400]
    print(combBodyResult(b,expect_code))
    print(get_result("D:\\PycharmProjects\\pytest_automation\\testCases\\testData","\case.yaml","code"))

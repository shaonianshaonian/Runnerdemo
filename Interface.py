# python3
#构造性能测试基类
import re
import time
import requests
import test
#初始化url、method（默认get）、header（默认为空字典）等参数,
#这里Performance类重写父类threading.Thread的__init__方法,会覆盖父类的__init__方法，
#用super()函数可以解决了子类就算重写父类方法或属性仍然可以继续使用父类的方法和属性。
class Performance(test.Thread):
    def __init__(self,url="", method="get",header={},body="",body_type="json"):
        #threading.Thread.__init__(self)
        super().__init__()
        self.url = url
        self.method = method
        self.header = header
        self.body = body
        self.body_type = body_type
    #构造请求函数
    def send_request(self):
        if re.search(self.method,'get',re.I):
            #get请求参数请求参数直接跟在url后面
            response =  requests.get(self.url,headers=self.header)
        else:
            if self.body_type == "json":
                response = requests.post(self.url,headers=self.header,json = self.body)
            elif self.body_type == "file":
                response = requests.post(self.url,headers=self.header,files = self.body)
            elif self.body == "data":
                response = requests.post(self.url,headers=self.header,data = self.body)
        #print(response.text)
        return response
    #构造接口请求状态、时间函数
    def test_performance(self):
        start_time = time.time()
        try:
            #运行请求函数
            response = self.send_request()
            #判断http状态码
            if response.status_code == 200:
                status = "success"
            else:
                status = "fail"
        except Exception as e:
            print(e)
            status = "except"
        end_time = time.time()
        spend_time = end_time - start_time
        return status,spend_time
    #构造运行函数
    def run(self):
        self.test_performance()
# coding=utf-8
import requests
from locust import HttpUser, TaskSet, task

from locust import HttpUser, TaskSet, task, between

headers = {
    "Content-Type": "application/json",
    "Country-Code": "MY",
    "Language-Code": "cn",
    "User-ID": "28",
    "User-Country-Code": "MY"
}

datas = {
    "serverName": "market-center",
    "interfaceName": "IActivityService.GetCurrent"
}


# 访问IActivityService.GetCurrent接口
class shakeActivity(TaskSet):

    @task
    def GetCurrent(self):
        # 定义请求头
        header = headers
        req = self.client.post("/api/proxyjson/", headers=header, data=datas)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")


class WebsiteUser(HttpUser):
    tasks = [shakeActivity]
    host = "https://shg-test.fingo.shop"
    wait_time = between(1, 1)


if __name__ == "__main__":
    import os

    os.system("locust -f test_002.py --headless -u 100 -r 50 -t 30")

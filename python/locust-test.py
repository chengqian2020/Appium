import json

from locust import TaskSet, HttpUser, between

def shake_get_current(l):
    headers = {
        "Content-Type": "application/json",
        "Country-Code": "MY",
        "Language-Code": "cn",
        "User-ID": "28",
        "User-Country-Code": "MY"
    }
    body = {
        "serverName": "market-center",
        "interfaceName": "IActivityService.GetCurrent"
    }
    with l.client.post("/api/proxyboss/", headers=headers, data=json.dumps(body), catch_response=True) as res_current:
        if res_current.status_code != 200:
            res_current.failure('Failed!')
        else:
            res_current.success()


class UserBehavior(TaskSet):
    tasks = [shake_get_current]


class WebSiteUser(HttpUser):
    host = "https://shg-test.fingo.shop"
    wait_time = between(3, 5)
    tasks = [UserBehavior]
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Testwait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(3)  # 隐式等待

    def teardown(self):
        print("等待两秒关闭浏览器")
        time.sleep(2)  # 直接等待
        self.driver.quit()

    def xianzhi_wait(self):
        self.driver.find_element_by_id("kw").send_keys("程潜")
        self.driver.find_element_by_id("su").click()
        WebDriverWait(self.driver, 10).until()

# -*- coding: UTF-8 -*-
import time
from selenium import webdriver


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 全屏展示
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get('http://www.baidu.com')


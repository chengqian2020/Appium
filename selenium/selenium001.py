#-*- coding: UTF-8 -*-

from selenium import webdriver

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get('http://testerhome.com/hogwarts')





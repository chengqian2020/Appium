# -*- coding: utf-8 -*-
from selenium import webdriver

class Base():
    def setup(self):
        self.driver = webdriver.chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearduwn(self):
        self.driver.quit()

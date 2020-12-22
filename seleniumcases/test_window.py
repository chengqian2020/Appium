from selenium import  webdriver
from selenium_event.base import Base


class Testwindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.


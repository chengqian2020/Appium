import time
import pytest
from selenium import webdriver
from seleniumcases.base import Base


class Testwindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        el = self.driver.window_handles
        print(el)
        self.driver.switch_to_window(el[-1])
        time.sleep(3)
        self.driver.switch_to_window(el[0])
        time.sleep(3)





if __name__ == '__main__':
    pytest.main(["-v", "-s", "Testwindows"])

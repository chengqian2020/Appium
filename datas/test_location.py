import time
import pytest
from selenium import webdriver


class TestDemo:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(3)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element_by_id("kw").send_keys("程潜")
        self.driver.find_element_by_id("su").click()



if __name__ == '__main__':
    pytest.main("-v -x TestDeom")

#-*- coding: UTF-8 -*-
import time
from selenium import webdriver
def Test_selenium():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('一只老母猪')
    driver.find_element_by_id('su').click()
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    Test_selenium()


# -*- coding: utf-8 -*-

from appium import webdriver
import time,traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'test'
desired_caps['app'] ='/Users/cq/Desktop/app@name_3.1.30@code_2498@debug.apk'
desired_caps['appPackage'] = 'com.fingogroup.fingo'
desired_caps['appActivity'] = 'com.fingogroup.fingo.vp.login.WelcomeActivity'
desired_caps['unicodekeyboard'] = True
desired_caps['reseKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000







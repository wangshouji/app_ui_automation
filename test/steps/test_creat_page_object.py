#coding=utf-8
import sys
import os
import yaml
sys.path.append("./behave")
from behave.start import *
from uiautomator2_up.u2_module import MyUiautomatorDriver
import importlib
from time import sleep
importlib.reload(sys)

paths = os.path.dirname(__file__).split('test')[0] + os.sep.join(["UIfeature\\android\\bwm.yml"])
f = open(paths, 'r', encoding='utf-8')
cfg = f.read()
dat = yaml.load(cfg)

driver = MyUiautomatorDriver('emulator-5554')

driver.reset_install_app()

# def setup_module(module):
#     pass
#
# def teardown_module(module):
#     pass

class TestCreatPageObject(object):

    # def setup_method(self):
    #     self.driver = driver
    #
    # def teardown_method(self):
    #     self.driver.browser.quit()
    #login
    def test_01(self):
        sleep(1)
        print('进入启动页面')
        print('点击单选框')
        driver.browser.find_element_by_id(dat['agree'][4]['id']).click()
        # sleep(1)
        # driver.browser.get_screenshot_as_file(dat['agree'][4]['alias'] + '.png')
        sleep(1)
        print('点击同意')
        driver.browser.find_element_by_id(dat['agree'][5]['id']).click()
        print('判断是否进入轮播页面')
        assert driver.browser.find_element_by_id(dat['connect'][1]['id']) is not None
        print('进入轮播页面')
        # sleep(1)
        # driver.browser.get_screenshot_as_file(dat['agree'][5]['alias'] + '.png')
    #
    def test_02(self):
        sleep(1)
        print('当前页面为轮播页面')
        print('点击下一步')
        driver.browser.find_element_by_id(dat['connect'][1]['id']).click()
        sleep(1)
        print('点击下一步')
        driver.browser.find_element_by_id(dat['connect'][1]['id']).click()
        sleep(1)
        print('点击下一步')
        driver.browser.find_element_by_id(dat['connect'][1]['id']).click()
        sleep(1)
        print('点击完成')
        driver.browser.find_element_by_id(dat['connect'][5]['id']).click()
        print('判断是否进入登陆页面')
        assert driver.browser.find_element_by_id(dat['login'][0]['id']) is not None
        print('进入登陆页面')

    def test_03(self):
        sleep(1)
        print('当前页面为登陆页面')
        print('点击权限框')
        driver.browser.find_element_by_id(dat['login'][0]['id']).click()
        sleep(1)
        print('输入账号')
        driver.browser.find_element_by_id(dat['login'][2]['id']).send_keys('18621263786')
        sleep(1)
        print('输入密码')
        driver.browser.find_element_by_id(dat['login'][3]['id']).send_keys('1qaz2wsx')
        sleep(1)
        print('点击登陆')
        driver.browser.find_element_by_id(dat['login'][4]['id']).click()
        print('判断是否登陆成功')
        assert driver.browser.find_element_by_xpath(dat['createpin'][0]['xpath']) is not None
        print('登陆成功')

    def test_04(self):
        sleep(10)
        print('当前页面为设置pin页面')
        print('点击1')
        driver.browser.find_element_by_xpath(dat['createpin'][0]['xpath']).click()
        sleep(1)
        print('点击2')
        driver.browser.find_element_by_xpath(dat['createpin'][1]['xpath']).click()
        sleep(1)
        print('点击3')
        driver.browser.find_element_by_xpath(dat['createpin'][2]['xpath']).click()
        sleep(1)
        print('点击4')
        driver.browser.find_element_by_xpath(dat['createpin'][3]['xpath']).click()

        sleep(2)
        print('点击1')
        driver.browser.find_element_by_xpath(dat['createpin'][0]['xpath']).click()
        sleep(1)
        print('点击2')
        driver.browser.find_element_by_xpath(dat['createpin'][1]['xpath']).click()
        sleep(1)
        print('点击3')
        driver.browser.find_element_by_xpath(dat['createpin'][2]['xpath']).click()
        sleep(1)
        print('点击4')
        driver.browser.find_element_by_xpath(dat['createpin'][3]['xpath']).click()
        print('判断是否设置成功')
        assert driver.browser.find_element_by_id(dat['permissions'][0]['id']) is not None
        print('permissions页面')

    def test_05(self):
        sleep(1)
        print('当前页面为设置pin页面')
        print('点击跳过')
        driver.browser.find_element_by_id(dat['permissions'][0]['id']).click()
        sleep(1)
        print('点击允许')
        driver.browser.find_element_by_id(dat['permissions'][1]['id']).click()
        sleep(1)
        print('点击允许')
        driver.browser.find_element_by_id(dat['permissions'][1]['id']).click()
        sleep(1)
        print('点击允许')
        driver.browser.find_element_by_id(dat['permissions'][1]['id']).click()
        sleep(1)
        print('点击确定')
        driver.browser.find_element_by_id(dat['permissions'][2]['id']).click()
        print('进入登陆页面')
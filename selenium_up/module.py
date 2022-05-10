#!/user/bin/env python
#coding=utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver import ActionChains
#url = "http://fota-web-test.nioint.com/desktop/"


class MyWebDriver(object):
    def __init__(self , url):
        chromedriver = "D:/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.set_page_load_timeout(60)
        self.browser.get(url)
        self.browser.fullscreen_window()
        # self.browser.find_element_by_class_name('<span class="l-btn-text">登录</span>')

    def find_element(self , attr):
        if 'id' in attr.keys():
            try:
                element = self.browser.find_element_by_id(attr['id'])
            except Exception as e:
                element = None
            if element is not None:
                return element
        if 'class' in attr.keys():
            try:
                element = self.browser.find_element_by_class_name(attr['class'])
            except selenium.common.exceptions.InvalidSelectorException as e:
                element = None
            if element is not None:
                return element

        if 'xpath' in attr.keys():
            try:
                element = self.browser.find_element_by_xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

        sleep(2)

        if 'id' in attr.keys():
            try:
                element = self.browser.find_element_by_id(attr['id'])
            except Exception as e:
                element = None
            if element is not None:
                return element
        if 'class' in attr.keys():
            try:
                element = self.browser.find_element_by_class_name(attr['class'])
            except selenium.common.exceptions.InvalidSelectorException as e:
                element = None
            if element is not None:
                return element

        if 'xpath' in attr.keys():
            try:
                element = self.browser.find_element_by_xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

        sleep(5)

        if 'id' in attr.keys():
            try:
                element = self.browser.find_element_by_id(attr['id'])
            except Exception as e:
                element = None
            if element is not None:
                return element
        if 'class' in attr.keys():
            try:
                element = self.browser.find_element_by_class_name(attr['class'])
            except selenium.common.exceptions.InvalidSelectorException as e:
                element = None
            if element is not None:
                return element

        if 'xpath' in attr.keys():
            try:
                element = self.browser.find_element_by_xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

    def click(self , text):
        attr = None
        element = self.find_element(attr)
        if element is not None:
            sleep(1)
            element.screenshot('')
            element.click()
            sleep(1)
            element.screenshot('')
        else:
            print('没有查找到元素：',text , attr)

    def send_key(self , text, value):
        attr = None
        element = self.find_element(attr)
        if element is not None:
            element.send_keys(value)
        else:
            print('没有查找到元素：', text, attr)


    def asserts(self , text):
        if True:
            pass
        elif True:
            attr = get_attr_login(text)
            element = self.find_element(attr)
            if element is not None:
                pass




driver = MyWebDriver('http://fota-web-test.nioint.com/desktop/')

if __name__ == '__main__':
    pass

#!/user/bin/env python
#coding=utf-8
import selenium
from appium import webdriver
from utils.devices import MyDevices
from utils.lxml_parser import MyLxmlParser
import os
import allure
import time
import operator
from time import sleep

class MyAppiumIosDriver(object):

    def __init__(self , platformName = None , automationName = None, udid = None ,
                 port = None , systemPort = None):
        self.udid = udid
        self.mydevices = MyDevices()
        path = os.path.dirname(__file__).split('appium_up')[0] + os.sep.join(["ipa"])
        fle = os.listdir(path)[0]

        desired_caps = {}
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = udid.split('_')[1]
        desired_caps['deviceName'] = udid.split('_')[2]
        desired_caps['udid'] = udid.split('_')[0]
        desired_caps['automationName'] = automationName
        desired_caps['bundleId'] = 'com.b.cbtc.debug'
        # desired_caps['app'] = path + '/' + fle
        # desired_caps['appPackage'] = package
        # desired_caps['appActivity'] = mainActivity
        # desired_caps['autoAcceptAlerts'] = True
        desired_caps['noRest'] = True
        desired_caps['wdaLocalPort'] = str(int(systemPort) - 11900)
        desired_caps['newCommandTimeout'] = 0
        desired_caps['connectHardwareKeyboard'] = True
        desired_caps['clearSystemFiles'] = True
        print('desired_caps' ,desired_caps)
        self.browser = webdriver.Remote('http://localhost:{0}/wd/hub'.format(port), desired_caps)

    def reset_install_app(self):
        pass
        # boolValue = False
        # for app in self.mydevices.is_install_app(self.device):
        #     if package in app:
        #         boolValue = True
        # if boolValue:
        #     req = self.mydevices.uninstall_app_to_devices(self.device, package)
        #     print('uninstall result:', req)
        #     self.mydevices.install_app_to_devices(self.device, path + '/' + fle)
        # else:
        #     self.mydevices.install_app_to_devices(self.device, path + '/' + fle)
        # self.browser.app_start(package)


    def get_attr(self , text):
        path = os.path.dirname(__file__).split('appium_up')[0] + os.sep.join(["page_obj_ios"])
        for i in os.listdir(path):
            if i not in ('func.py', '__init__.py', '__pycache__'):
                a = __import__('page_obj_ios.{0}'.format(i.split('.')[0]), fromlist=True)
                b = eval('a.{0}()'.format(i.split('.')[0].capitalize()))
                for i in dir(b):
                    if i.find('__') < 0:
                        if b.__getattribute__(i).func_name == text:
                            return b.__getattribute__(i)()


    def find_element(self , attr):
        self.startTime = time.time()
        if 'xpath' in attr.keys():
            try:
                element = self.browser.find_element_by_xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

        if 'name' in attr.keys():
            try:
                element = self.browser.find_element_by_accessibility_id(attr['name'])
            except Exception as e:
                element = None
            if element is not None:
                return element
        # if 'class' in attr.keys():
        #     try:
        #         element = self.browser.find_element_by_class_name(attr['class'])
        #     except selenium.common.exceptions.NoSuchElementException as e:
        #         element = None
        #     if element is not None:
        #         return element

        sleep(2)

        if 'xpath' in attr.keys():
            try:
                element = self.browser.find_element_by_xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

        if 'name' in attr.keys():
            try:
                element = self.browser.find_element_by_accessibility_id(attr['name'])
            except Exception as e:
                element = None
            if element is not None:
                return element
        # if 'class' in attr.keys():
        #     try:
        #         element = self.browser.find_element_by_class_name(attr['class'])
        #     except selenium.common.exceptions.InvalidSelectorException as e:
        #         element = None
        #     if element is not None:
        #         return element

        sleep(3)

        if 'xpath' in attr.keys():
            try:
                element = self.browser.find_element_by_xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

        if 'name' in attr.keys():
            try:
                element = self.browser.find_element_by_accessibility_id(attr['name'])
            except Exception as e:
                element = None
            if element is not None:
                return element
        # if 'class' in attr.keys():
        #     try:
        #         element = self.browser.find_element_by_class_name(attr['class'])
        #     except selenium.common.exceptions.InvalidSelectorException as e:
        #         element = None
        #     if element is not None:
        #         return element

        sleep(20)

        if 'xpath' in attr.keys():
            try:
                element = self.browser.find_element_by_xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

        if 'name' in attr.keys():
            try:
                element = self.browser.find_element_by_accessibility_id(attr['name'])
            except Exception as e:
                element = None
            if element is not None:
                return element
        # if 'class' in attr.keys():
        #     try:
        #         element = self.browser.find_element_by_class_name(attr['class'])
        #     except selenium.common.exceptions.InvalidSelectorException as e:
        #         element = None
        #     if element is not None:
        #         return element

    def creat_page_object(self , mattr):
        path = os.path.dirname(__file__).split('appium_up')[0] + os.sep.join(
            ["test/backphoto"]) + os.sep + self.udid
        with open(path + '/page.xml' , 'w' ,encoding='utf-8') as f:
            f.write(self.browser.page_source)

        file_path = path + '/page.xml'
        mylxml = MyLxmlParser(html=file_path, xpath='/AppiumAUT//*', parser='xml')
        mylxml.parser_appium_ios_xml(mylxml.etree_elements, mylxml.etree_elementTrees,
                             mylxml.elements, mylxml.parent_elements)
        pge_path = path.split('test')[0] + os.sep.join(["page_obj_ios"])
        if len(mylxml.attrs) > 0:
            with open(pge_path + '/' + mattr['page'][0]['name'] + '.py' , 'w' , encoding='utf-8') as f:
                f.writelines('#!/user/bin/env python\n#coding=utf-8\nfrom page_object.func import func_name\n')
                f.writelines('class ' + mattr['page'][0]['name'].capitalize() + '(object):\n')
                f.writelines('\tdef __init__(self):\n\t\tpass\n\n')
                index = 1
                for attr in mylxml.attrs:
                    bname = False
                    btext = None
                    for ttr in mattr['page'][1:]:
                        if 'xpath' in ttr.keys():
                            if mylxml.etree_elements.xpath(ttr['xpath'])[0] is not None:
                                req = operator.eq(attr , mylxml.etree_elements.xpath(ttr['xpath'])[0].attrib)
                                if req is True:
                                    bname = True
                                    btext = ttr['alias']
                                    break
                        elif 'id' in ttr.keys():
                            if mylxml.etree_elements.xpath('//*[@name="' + ttr['id'] + '"]')[0] is not None:
                                req = operator.eq(attr, mylxml.etree_elements.xpath('//*[@name="' + ttr['id'] + '"]')[0].attrib)
                                if req is True:
                                    bname = True
                                    btext = ttr['alias']
                                    break
                            #mylxml.etree_elements.find('//*[@resource-id="' + parent.getparent().attrib['resource-id'] + '"]')
                    if bname is True:
                        f.writelines("\t@func_name('{0}')\n".format(str(btext)))
                    else:
                        f.writelines("\t@func_name('null')\n")
                    f.writelines("\tdef get_attr{0}(self):\n".format(str(index)))
                    f.writelines("\t\treturn {0}\n\n".format(str(attr)))
                    index += 1
                f.close()

    def monkey_click_or_input(self , mattr):
        if mattr['action'] == 'click':
            if '//' in mattr['idOrXpath']:
                try:
                    self.startTime = time.time()
                    self.browser.find_element_by_xpath(mattr['idOrXpath']).click()
                except Exception as e:
                    print(e)
                    try:
                        sleep(1)
                        self.browser.find_element_by_xpath(mattr['idOrXpath']).click()
                    except Exception as e:
                        print(e)
                        sleep(1)
                        self.browser.find_element_by_xpath(mattr['idOrXpath']).click()
                sleep(int(mattr['times']))
                self.monkey_allure_step(mattr)
                if 'page' in mattr.keys():
                    self.creat_page_object(mattr)
            else:
                try:
                    self.startTime = time.time()
                    self.browser.find_element_by_accessibility_id(mattr['idOrXpath']).click()
                except Exception as e:
                    print(e)
                    try:
                        sleep(1)
                        self.browser.find_element_by_accessibility_id(mattr['idOrXpath']).click()
                    except Exception as e:
                        print(e)
                        sleep(1)
                        self.browser.find_element_by_accessibility_id(mattr['idOrXpath']).click()
                sleep(int(mattr['times']))
                self.monkey_allure_step(mattr)
                if 'page' in mattr.keys():
                    self.creat_page_object(mattr)
        elif mattr['action'] == 'swipe left':
            self.startTime = time.time()
            self.browser.swipe(self.browser.get_window_size()['width'],self.browser.get_window_size()['height']/2 ,
                               0 , self.browser.get_window_size()['height']/2 , 1000)
            sleep(int(mattr['times']))
            self.monkey_allure_step(mattr)
            if 'page' in mattr.keys():
                self.creat_page_object(mattr)
        elif mattr['action'] == 'swipe right':
            self.startTime = time.time()
            self.browser.swipe(0,self.browser.get_window_size()['height']/2 ,
                               self.browser.get_window_size()['width'] , self.browser.get_window_size()['height']/2 , 1000)
            sleep(int(mattr['times']))
            self.monkey_allure_step(mattr)
            if 'page' in mattr.keys():
                self.creat_page_object(mattr)
        elif mattr['action'] == 'swipe up':
            self.startTime = time.time()
            self.browser.swipe(self.browser.get_window_size()['width']/2,self.browser.get_window_size()['height'] ,
                               self.browser.get_window_size()['width'] / 2 , 0 , 1000)
            sleep(int(mattr['times']))
            self.monkey_allure_step(mattr)
            if 'page' in mattr.keys():
                self.creat_page_object(mattr)
        elif mattr['action'] == 'swipe down':
            self.startTime = time.time()
            self.browser.swipe(self.browser.get_window_size()['width']/2,0 ,
                               self.browser.get_window_size()['width'] / 2 , self.browser.get_window_size()['height'] , 1000)
            sleep(int(mattr['times']))
            self.monkey_allure_step(mattr)
            if 'page' in mattr.keys():
                self.creat_page_object(mattr)
        else:
            if '//' in mattr['idOrXpath']:
                try:
                    self.startTime = time.time()
                    self.browser.find_element_by_xpath(mattr['idOrXpath']).send_keys(mattr['action'])
                except Exception as e:
                    print(e)
                    try:
                        sleep(1)
                        self.browser.find_element_by_xpath(mattr['idOrXpath']).send_keys(mattr['action'])
                    except Exception as e:
                        print(e)
                        sleep(1)
                        self.browser.find_element_by_xpath(mattr['idOrXpath']).send_keys(mattr['action'])
                sleep(int(mattr['times']))
                self.monkey_allure_step(mattr)
                if 'page' in mattr.keys():
                    self.creat_page_object(mattr)
            else:
                try:
                    self.startTime = time.time()
                    self.browser.find_element_by_accessibility_id(mattr['idOrXpath']).send_keys(mattr['action'])
                except Exception as e:
                    print(e)
                    try:
                        sleep(1)
                        self.browser.find_element_by_accessibility_id(mattr['idOrXpath']).send_keys(mattr['action'])
                    except Exception as e:
                        print(e)
                        sleep(1)
                        self.browser.find_element_by_accessibility_id(mattr['idOrXpath']).send_keys(mattr['action'])
                sleep(int(mattr['times']))
                self.monkey_allure_step(mattr)
                if 'page' in mattr.keys():
                    self.creat_page_object(mattr)

    def monkey_allure_step(self , mattr):
        with allure.step(str(mattr['action']) + ' : ' + mattr['idOrXpath']):
            self.endTime = time.time()
            allure.attach('spend-time', str(self.endTime - self.startTime))
            allure.attach('wait-time', str(mattr['times']))
            if 'screenshot' in mattr.keys():
                path = os.path.dirname(__file__).split('appium_up')[0] + os.sep.join(
                    ["test/backphoto"]) + os.sep + self.udid
                if os.path.exists(path):
                    self.browser.save_screenshot(path + '/' + mattr['screenshot'] + '.png')
                else:
                    os.mkdir(path)
                    self.browser.save_screenshot(path + '/' + mattr['screenshot'] + '.png')

                with open(path + '/' + mattr['screenshot'] + '.png', 'rb') as f:
                    allure.attach(mattr['screenshot'] + '.PNG', f.read(), allure.attach_type.PNG)

    def allure_step(self , text , attr):
        with allure.step(text + '(details)'):
            self.endTime = time.time()
            allure.attach(text, str(attr))
            allure.attach('time', str(self.endTime - self.startTime))
            path = os.path.dirname(__file__).split('appium_up')[0] + os.sep.join(
                ["test/photo"]) + os.sep + self.udid
            if os.path.exists(path):
                self.browser.save_screenshot(path + '/' + text + '.png')
            else:
                os.mkdir(path)
                self.browser.save_screenshot(path + '/' + text + '.png')

            with open(path + '/' + text + '.png', 'rb') as f:
                allure.attach(text + '.PNG', f.read(), allure.attach_type.PNG)

    def click(self , text):
        attr = self.get_attr(text)
        if attr is None:
            return
        element = self.find_element(attr)
        if element is not None:
            element.click()
        else:
            print('没有查找到元素：',text , attr)
        self.allure_step(text , attr)

    def send_key(self , text, value):
        attr = self.get_attr(text)
        if attr is None:
            return
        element = self.find_element(attr)
        if element is not None:
            element.send_keys(value)
        else:
            print('没有查找到元素：', text, attr)
        self.allure_step(text, attr)

    def swipe(self):
        pass


    def asserts(self , text):
        if True:
            pass
        elif True:
            attr = self.get_attr(text)
            element = self.find_element(attr)
            if element is not None:
                pass

if __name__ == '__main__':
    pass
    # driver = MyAppiumIosDriver(platformName='ios', automationName='XCUITest',
    #                                 udid='40215B8D-D6C8-4211-BD2B-73278878C9B5_12.1_iphoneXS', port='4725', systemPort='20000')
    # print(driver.browser.get_window_size()['width'])
    # print(driver.browser.get_window_size()['height'])
    # driver.browser.swipe(driver.browser.get_window_size()['width'] , driver.browser.get_window_size()['height']/2 ,
    #                      0 ,driver.browser.get_window_size()['height']/2 ,1000)
    # driver.browser.swipe(driver.browser.get_window_size()['width'], driver.browser.get_window_size()['height'] / 2, 0,
    #                      driver.browser.get_window_size()['height'] / 2, 1000)
    # driver.browser.swipe(driver.browser.get_window_size()['width'], driver.browser.get_window_size()['height'] / 2, 0,
    #                      driver.browser.get_window_size()['height'] / 2, 1000)
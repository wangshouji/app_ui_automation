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

class MyAppiumAndroidDriver(object):

    def __init__(self , platformName = None , automationName = None, udid = None ,
                 port = None , systemPort = None):
        self.udid = udid
        self.mydevices = MyDevices()
        path = os.path.dirname(__file__).split('appium_up')[0] + os.sep.join(["apk"])
        fle = os.listdir(path)[0]
        version = self.mydevices.get_devices_info(udid)
        package = self.mydevices.get_devices_package_info(path + '/' + fle)
        package = package[0].split(' ')[1].split("'")[1]
        print('package', package)
        mainActivity = self.mydevices.get_devices_main_activity(path + '/' + fle)
        mainActivity = mainActivity[0].split(' ')[1].split("'")[1]
        deivce_name = self.mydevices.get_devices_model(udid)

        desired_caps = {}
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = version[0]
        desired_caps['deviceName'] = deivce_name[0]
        desired_caps['udid'] = udid
        desired_caps['automationName'] = automationName
        desired_caps['app'] = path + '/' + fle
        # desired_caps['appPackage'] = package
        # desired_caps['appActivity'] = mainActivity
        # desired_caps['autoAcceptAlerts'] = True
        # desired_caps['noRest'] = True
        desired_caps['systemPort'] = str(int(systemPort) - 5000)

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
        path = os.path.dirname(__file__).split('appium_up')[0] + os.sep.join(["page_object"])
        for i in os.listdir(path):
            if i not in ('func.py', '__init__.py', '__pycache__'):
                a = __import__('page_object.{0}'.format(i.split('.')[0]), fromlist=True)
                b = eval('a.{0}()'.format(i.split('.')[0].capitalize()))
                for i in dir(b):
                    if i.find('__') < 0:
                        if b.__getattribute__(i).func_name == text:
                            return b.__getattribute__(i)()


    def find_element(self , attr):
        if 'xpath' in attr.keys():
            try:
                element = self.browser.find_element_by_xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

        if 'resource-id' in attr.keys():
            try:
                element = self.browser.find_element_by_id(attr['resource-id'])
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

        if 'resource-id' in attr.keys():
            try:
                element = self.browser.find_element_by_id(attr['resource-id'])
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

        if 'resource-id' in attr.keys():
            try:
                element = self.browser.find_element_by_id(attr['resource-id'])
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

        if 'resource-id' in attr.keys():
            try:
                element = self.browser.find_element_by_id(attr['resource-id'])
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
        mylxml = MyLxmlParser(html=file_path, xpath='/hierarchy//*', parser='xml')
        mylxml.parser_appium_android_xml(mylxml.etree_elements, mylxml.etree_elementTrees,
                             mylxml.elements, mylxml.parent_elements)
        pge_path = path.split('test')[0] + os.sep.join(["page_object"])
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
                            if mylxml.etree_elements.xpath('//*[@resource-id="' + ttr['id'] + '"]')[0] is not None:
                                req = operator.eq(attr, mylxml.etree_elements.xpath('//*[@resource-id="' + ttr['id'] + '"]')[0].attrib)
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
                    self.browser.find_element_by_id(mattr['idOrXpath']).click()
                except Exception as e:
                    print(e)
                    try:
                        sleep(1)
                        self.browser.find_element_by_id(mattr['idOrXpath']).click()
                    except Exception as e:
                        print(e)
                        sleep(1)
                        self.browser.find_element_by_id(mattr['idOrXpath']).click()
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
                    self.browser.find_element_by_id(mattr['idOrXpath']).send_keys(mattr['action'])
                except Exception as e:
                    print(e)
                    try:
                        sleep(1)
                        self.browser.find_element_by_id(mattr['idOrXpath']).send_keys(mattr['action'])
                    except Exception as e:
                        print(e)
                        sleep(1)
                        self.browser.find_element_by_id(mattr['idOrXpath']).send_keys(mattr['action'])
                sleep(int(mattr['times']))
                self.monkey_allure_step(mattr)
                if 'page' in mattr.keys():
                    self.creat_page_object(mattr)

    def monkey_allure_step(self , mattr):
        with allure.step(str(mattr['action']) + ' : ' + mattr['idOrXpath']):
            self.endTime = time.time()
            allure.attach('spend-time', str(self.endTime - self.startTime))
            allure.attach('wait-time', str(mattr['times']))
            # if 'screenshot' in mattr.keys():
            #     path = os.path.dirname(__file__).split('uiautomator2')[0] + os.sep.join(
            #         ["test/backphoto"]) + os.sep + self.device
            #     if os.path.exists(path):
            #         self.browser.screenshot(path + '/' + mattr['screenshot'] + '.png')
            #     else:
            #         os.mkdir(path)
            #         self.browser.screenshot(path + '/' + mattr['screenshot'] + '.png')
            #
            #     with open(path + '/' + mattr['screenshot'] + '.png', 'rb') as f:
            #         allure.attach(mattr['screenshot'] + '.PNG', f.read(), allure.attach_type.PNG)

    def click(self , text):
        attr = self.get_attr(text)
        element = self.find_element(attr)
        if element is not None:
            element.click()
        else:
            print('????????????????????????',text , attr)

    def send_key(self , text, value):
        attr = self.get_attr(text)
        element = self.find_element(attr)
        if element is not None:
            element.send_keys(value)
        else:
            print('????????????????????????', text, attr)

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
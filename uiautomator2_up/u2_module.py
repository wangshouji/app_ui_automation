#!/user/bin/env python
#coding=utf-8
import os
from time import sleep
import uiautomator2 as u2
from utils.devices import MyDevices
from utils.lxml_parser import MyLxmlParser
import allure
import time
import operator

class MyUiautomatorDriver(object):

    def __init__(self , device):
        self.device = device
        self.browser = u2.connect(device)
        print(self.browser.info)
        self.mydevices = MyDevices()

    def reset_install_app(self):
        path = os.path.dirname(__file__).split('uiautomator2')[0] + os.sep.join(["apk"])
        fle = os.listdir(path)[0]
        package = self.mydevices.get_devices_package_info(path + '/' + fle)
        print('devices_package_info' , package)
        package = package[0].split(' ')[1].split("'")[1]
        print('package', package)
        #print(self.mydevices.is_install_app(self.device))
        boolValue = False
        for app in self.mydevices.is_install_app(self.device):
            if package in app:
                boolValue = True
        if boolValue:
            req = self.mydevices.uninstall_app_to_devices(self.device, package)
            print('uninstall result:', req)
            self.mydevices.install_app_to_devices(self.device, path + '/' + fle)
        else:
            self.mydevices.install_app_to_devices(self.device, path + '/' + fle)
        self.browser.app_start(package)  # "de.cted.cn.int"

    def get_attr(self , text):
        path = os.path.dirname(__file__).split('uiautomator2')[0] + os.sep.join(["page_object"])
        for i in os.listdir(path):
            if i not in ('func.py', '__init__.py', '__pycache__'):
                a = __import__('page_object.{0}'.format(i.split('.')[0]), fromlist=True)
                b = eval('a.{0}()'.format(i.split('.')[0].capitalize()))
                for i in dir(b):
                    if i.find('__') < 0:
                        if b.__getattribute__(i).func_name == text:
                            return b.__getattribute__(i)()


    def find_element(self , attr):
        self.startTime = time.time()
        if 'xpath' in attr.keys():
            try:
                element = self.browser.xpath(attr['xpath'])
            except Exception as e:
                element = None
            if element is not None:
                return element

        if 'resource-id' in attr.keys():
            try:
                element = self.browser(resourceId=attr['resource-id'])
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

    def creat_page_object(self , mattr):
        path = os.path.dirname(__file__).split('uiautomator2')[0] + os.sep.join(
            ["test/backphoto"]) + os.sep + self.device
        with open(path + '/page.xml' , 'w' ,encoding='utf-8') as f:
            f.write(self.browser.dump_hierarchy())

        file_path = path + '/page.xml'
        mylxml = MyLxmlParser(html=file_path, xpath='/hierarchy//*', parser='xml')
        mylxml.parser_uiautomator_xml(mylxml.etree_elements, mylxml.etree_elementTrees,
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
                    self.browser.xpath(mattr['idOrXpath']).click()
                except u2.ext.xpath.TimeoutException as e:
                    print(e)
                    try:
                        self.browser.xpath(mattr['idOrXpath']).click()
                    except u2.ext.xpath.TimeoutException as e:
                        print(e)
                        self.browser.xpath(mattr['idOrXpath']).click()
                sleep(int(mattr['times']))
                self.monkey_allure_step(mattr)
                if 'page' in mattr.keys():
                    self.creat_page_object(mattr)
            else:
                try:
                    self.startTime = time.time()
                    self.browser(resourceId=mattr['idOrXpath']).click()
                except u2.exceptions.UiObjectNotFoundError as e:
                    print(e)
                    try:
                        self.browser(resourceId=mattr['idOrXpath']).click()
                    except u2.exceptions.UiObjectNotFoundError as e:
                        print(e)
                        self.browser(resourceId=mattr['idOrXpath']).click()
                sleep(int(mattr['times']))
                self.monkey_allure_step(mattr)
                if 'page' in mattr.keys():
                    self.creat_page_object(mattr)
        elif mattr['action'] == 'swipe up':
            pass
        else:
            if '//' in mattr['idOrXpath']:
                try:
                    self.startTime = time.time()
                    self.browser.xpath(mattr['idOrXpath']).click()
                    self.browser.xpath(mattr['idOrXpath'])._d.send_keys(mattr['action'])
                except u2.ext.xpath.TimeoutException as e:
                    print(e)
                    try:
                        self.browser.xpath(mattr['idOrXpath']).click()
                        self.browser.xpath(mattr['idOrXpath'])._d.send_keys(mattr['action'])
                    except u2.ext.xpath.TimeoutException as e:
                        print(e)
                        self.browser.xpath(mattr['idOrXpath']).click()
                        self.browser.xpath(mattr['idOrXpath'])._d.send_keys(mattr['action'])
                sleep(int(mattr['times']))
                self.monkey_allure_step(mattr)
                if 'page' in mattr.keys():
                    self.creat_page_object(mattr)
            else:
                try:
                    self.startTime = time.time()
                    self.browser(resourceId=mattr['idOrXpath']).send_keys(mattr['action'])
                except u2.exceptions.UiObjectNotFoundError as e:
                    print(e)
                    try:
                        self.browser(resourceId=mattr['idOrXpath']).send_keys(mattr['action'])
                    except u2.exceptions.UiObjectNotFoundError as e:
                        print(e)
                        self.browser(resourceId=mattr['idOrXpath']).send_keys(mattr['action'])
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
                path = os.path.dirname(__file__).split('uiautomator2')[0] + os.sep.join(
                    ["test/backphoto"]) + os.sep + self.device
                if os.path.exists(path):
                    self.browser.screenshot(path + '/' + mattr['screenshot'] + '.png')
                else:
                    os.mkdir(path)
                    self.browser.screenshot(path + '/' + mattr['screenshot'] + '.png')

                with open(path + '/' + mattr['screenshot'] + '.png', 'rb') as f:
                    allure.attach(mattr['screenshot'] + '.PNG', f.read(), allure.attach_type.PNG)

    def allure_step(self , text , attr):
        with allure.step(text + '(details)'):
            self.endTime = time.time()
            allure.attach(text, str(attr))
            allure.attach('time', str(self.endTime - self.startTime))
            path = os.path.dirname(__file__).split('uiautomator2')[0] + os.sep.join(
                ["test/photo"]) + os.sep + self.device
            if os.path.exists(path):
                self.browser.screenshot(path + '/' + text + '.png')
            else:
                os.mkdir(path)
                self.browser.screenshot(path + '/' + text + '.png')

            with open(path + '/' + text + '.png', 'rb') as f:
                allure.attach(text + '.PNG', f.read(), allure.attach_type.PNG)

    def click(self , text):
        attr = self.get_attr(text)
        element = self.find_element(attr)
        print('element type:' , element)
        if element is not None:
            try:
                element.click()
            except u2.exceptions.UiObjectNotFoundError as e:
                print('error:' , e)
                try:
                    element.click()
                except u2.exceptions.UiObjectNotFoundError as e:
                    print('error:', e)
                    try:
                        element.click()
                    except u2.exceptions.UiObjectNotFoundError as e:
                        print('error:', e)
            except u2.ext.xpath.TimeoutException as e:
                print('error:', e)
                try:
                    element.click()
                except u2.ext.xpath.TimeoutException as e:
                    print('error:', e)
                    try:
                        element.click()
                    except u2.ext.xpath.TimeoutException as e:
                        print('error:', e)
            self.allure_step(text , attr)
        else:
            print('没有查找到元素：',text , attr)

    def send_key(self , text, value):
        attr = self.get_attr(text)
        element = self.find_element(attr)
        if element is not None:
            try:
                element.click()
                element._d.send_keys(value)
            except u2.exceptions.UiObjectNotFoundError as e:
                print(e,self.device)
                try:
                    element.click()
                    element._d.send_keys(value)
                except u2.exceptions.UiObjectNotFoundError as e:
                    print(e, self.device)
                    try:
                        element.click()
                        element._d.send_keys(value)
                    except u2.exceptions.UiObjectNotFoundError as e:
                        print(e, self.device)
            except u2.ext.xpath.TimeoutException as e:
                print(e, self.device)
                try:
                    element.click()
                    element._d.send_keys(value)
                except u2.ext.xpath.TimeoutException as e:
                    print(e, self.device)
                    try:
                        element.click()
                        element._d.send_keys(value)
                    except u2.ext.xpath.TimeoutException as e:
                        print(e, self.device)
            self.allure_step(text, attr)
        else:
            print('没有查找到元素：', text, attr)


    def asserts(self , text):
        if True:
            pass
        elif True:
            attr = self.get_attr(text)
            element = self.find_element(attr)
            if element is not None:
                pass




#driver = MyAppiumDriver('C:\\Users\\QXY0087\\Desktop\\behave_selenium\\apk\\b.apk' , '4725')

if __name__ == '__main__':
    pass
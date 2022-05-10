
#coding=utf-8
import sys
import os
from utils.devices import MyDevices
from time import sleep

import multiprocessing
class MyRunCaseProcess(multiprocessing.Process):

    def __init__(self , platform = None , automation = None, automationName = None , udid = None , port = None , bp = None):
        multiprocessing.Process.__init__(self)
        self.platform = platform
        self.automation = automation
        self.automationName = automationName
        self.udid = udid
        self.port = port
        self.bp = bp

    def run(self):
        appiumServer = multiprocessing.Process(target = self.start_appium_server)
        appiumServer.start()
        sleep(5)
        self.run_pytest_shell()
        self.generate_html_report()
        self.stop_appium_server()

    def stop(self):
        pass

    def start_appium_server(self):
        if self.platform == 'android':
            if self.automation == 'appium':
                appium_result = os.popen('appium -a 127.0.0.1 -p {0} -bp {1} -g ../test/appiumlog/appium-log-{2}.txt'.format(self.port , self.bp , self.udid))

                for line in appium_result:
                    pass
                    #print(line)

        elif self.platform == 'ios':
            if self.automation == 'appium':
                appium_result = os.popen('appium -a 127.0.0.1 -p {0} -bp {1} -g ../test/appiumlog/appium-log-{2}.txt'.format(self.port , self.bp , self.udid))

                for line in appium_result:
                    pass

    def stop_appium_server(self):
        if self.automation == 'appium':
            appium_result = os.popen('kill -9 `lsof -t -i:{0}`'.format(self.port))
            print('appium-server stop')

    def generate_html_report(self):
        allure_result = os.popen('cd ../test;pwd;allure generate report/allure-results-{0} -o report/allure-report-{1} --clean'.format(self.udid,self.udid))

        for line in allure_result:
            print(line)

    def run_pytest_shell(self):
        print(self.udid, 'start')
        result = os.popen('cd ../test;source activate uiautomator2;pwd;'
                          'py.test steps/test_start.py --alluredir=report/allure-results-{0} --platform={1} --automation={2} '
                          '--automationName={3} --device={4} --port={5} --bp={6} --capture=no'
                          .format(self.udid, self.platform, self.automation,self.automationName, self.udid , self.port , self.bp))

        for line in result.readlines():
            print(line)

if __name__ == '__main__' :
    print('--------test run--------')
    iphone_devices = [('40215B8D-D6C8-4211-BD2B-73278878C9B5','12.1' , 'iphoneXS')]

    md = MyDevices()
    print(md.get_all_devices())
    port = 10000
    bp = 20000
    idx = [MyRunCaseProcess(platform='android' , automation= 'uiautomator2' , automationName='UiAutomator2', udid= i) for i in md.get_all_devices()]
    for i in idx:
        i.port = port
        i.bp = bp
        i.start()
        print('i.port i.bp' , i.port , i.bp)
        port += 1
        bp += 1
    print('port , bp',port , bp)

    print('--------start run ios case--------')

    iox = [MyRunCaseProcess(platform='ios' , automation= 'appium' , automationName='XCUITest', udid= x+'_'+y+'_'+z) for x , y , z in iphone_devices]
    for m in iox:
        m.port = port
        m.bp = bp
        m.start()
        print('m.port m.bp', m.port, m.bp)
        port += 1
        bp += 1
        sleep(30)
    print('port , bp', port, bp)
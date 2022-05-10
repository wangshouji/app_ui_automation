#coding=utf-8
import sys
import os
import yaml
import pytest
import platform
import time
from time import sleep

curPath = os.path.dirname(__file__).split('test')[0] + os.sep.join(["UIfeature/android"])
print(curPath)
yamlPath = os.path.join(curPath, "bwm.yml")
print(yamlPath)
f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()

dat = yaml.load(cfg)  # 用load方法转字典
print(dat)

platform = pytest.config.getoption('--platform')
automation = pytest.config.getoption('--automation')
automationName = pytest.config.getoption('--automationName')
udid = pytest.config.getoption('--device')
port = pytest.config.getoption('--port')
bp = pytest.config.getoption('--bp')

print(platform)

if platform == 'android':
    if automation == 'uiautomator2':
        from uiautomator2_up.u2_module import MyUiautomatorDriver

        driver = MyUiautomatorDriver(udid)
    elif automation == 'appium':
        from appium_up.appium_android_module import MyAppiumAndroidDriver

        driver = MyAppiumAndroidDriver(platformName=platform, automationName=automationName,
                                            udid=udid, port=port, systemPort=bp)

data = dat['actions']
ids = [str(i) for i in range(len(data))]
print(time.time())
driver.reset_install_app()

sleep(20)
print(time.time())

class TestMonkeyUI(object):

    @pytest.mark.parametrize('data',data, ids=ids)
    def test_all(self,data):
        driver.monkey_click_or_input(data)
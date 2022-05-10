#coding=utf-8
import sys
import os
sys.path.append("./behave")
import pytest
import platform
if 'Darwin' == platform.system():
    from behave.start import *
    from behave import *
elif 'Windows' == platform.system():
    from behave.behave import *
    from behave.behave import *
import importlib
from time import sleep
from utils.common import Common
importlib.reload(sys)

paths = os.path.dirname(__file__).split('steps')[0] + os.sep.join(["features"])

platform = pytest.config.getoption('--platform')
automation = pytest.config.getoption('--automation')
device = pytest.config.getoption('--device')

print(platform)

from utils.devices import MyDevices
devices = MyDevices()
plt = devices.get_all_devices()
from utils.Mythreading import MyThreading
threadlist = []

for i in plt:
    obj = MyThreading(platform = 'android' , automation = 'uiautomator2' , device = i)
    obj.start()
    data, ids =obj.com.parse_file(paths)
    threadlist.append(obj)

class TestAppUI(object):

    @pytest.mark.parametrize('data',data, ids=ids)
    @pytest.fixture(scope='function' , autouse=True)
    def prepare(self ,data):
        print(data['text'])
        runner = main()
        runner.reset_features(data['text'])
        return runner

    @pytest.mark.parametrize('data',data, ids=ids)
    def test_all(self,data ,prepare):

        @Given(data['given'])
        def step_impl(context, **kwargs):
            for i in threadlist:
                while i.index:
                    if i.index == 0:
                        i.run_case(**kwargs)
                        break

        @when(data['when'])
        def step_impl(context, **kwargs):
            for i in threadlist:
                while i.index:
                    if i.index == 0:
                        i.run_case(**kwargs)
                        break

        @then(data['then'])
        def step_impl(context, **kwargs):
            for i in threadlist:
                while i.index:
                    if i.index == 0:
                        i.run_case(**kwargs)
                        break

        result = prepare.reporter()

        assert result == False

        #install_pytest_asserts()
        #C:\Users\shouji.wang.o\PycharmProjects\behave_selenium\test\features\testsuite.UIfeature
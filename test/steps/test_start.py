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

platform = pytest.config.getoption('--platform')
automation = pytest.config.getoption('--automation')
automationName = pytest.config.getoption('--automationName')
udid = pytest.config.getoption('--device')
port = pytest.config.getoption('--port')
bp = pytest.config.getoption('--bp')

print(platform)
if platform == 'android':
    paths = os.path.dirname(__file__).split('steps')[0] + os.sep.join(["features"])
elif platform == 'ios':
    paths = os.path.dirname(__file__).split('steps')[0] + os.sep.join(["features_ios"])

obj = Common(platform = platform , automation = automation  , automationName = automationName,
             udid = udid , port = port , bp = bp)

data, ids =obj.parse_file(paths)

obj.init_install_app()

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
            obj.run(**kwargs)

        @when(data['when'])
        def step_impl(context, **kwargs):
            obj.run(**kwargs)

        @then(data['then'])
        def step_impl(context, **kwargs):
            obj.run(**kwargs)

        result = prepare.reporter()

        assert result == False

        #install_pytest_asserts()
        #C:\Users\shouji.wang.o\PycharmProjects\behave_selenium\test\features\testsuite.UIfeature
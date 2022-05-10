#!/user/bin/env python
#coding=utf-8

import pytest

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android",
        help="my option: android or ios")

    parser.addoption("--automation" , action = 'store' ,
                     default = 'appium' , help = " my option : appium or uiautomator2、macaca、selenium")

    parser.addoption("--automationName", action='store',
                     default='appium', help=" my option : appium or uiautomator2、XCUITest")

    parser.addoption("--device", action='store',
                     default='null', help=" my option : {udid}")

    parser.addoption("--port", action='store',
                     default='1000', help=" my option : 1000,4725")

    parser.addoption("--bp", action='store',
                     default='10000', help=" my option : 10000,4900")

@pytest.fixture
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture
def automation(request):
    return request.config.getoption("--automation")

@pytest.fixture
def automationName(request):
    return request.config.getoption("--automationName")

@pytest.fixture
def device(request):
    return request.config.getoption("--device")

@pytest.fixture
def port(request):
    return request.config.getoption("--port")

@pytest.fixture
def bp(request):
    return request.config.getoption("--bp")



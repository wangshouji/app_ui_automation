#!/user/bin/env python
#coding=utf-8
import os
import re
import time
import operator

class MyDevices(object):

    def __init__(self):
        pass

    def get_all_devices(self):
        readDeviceId = list(os.popen('adb devices').readlines())
        deviceId = [re.findall(r'^\w*\S*\w', i) for i in readDeviceId if '\tdevice\n' in i]#r'^\w*\b'
        return [i[0] for i in deviceId]

    def get_devices_info(self , devices = None):
        if devices is not None:
            deviceAndroidVersion = list(
                os.popen('adb -s {0} shell getprop ro.build.version.release'.format(devices)).readlines())
            deviceVersion = [re.findall(r'^\w*\b', i) for i in deviceAndroidVersion]
            return [i[0] for i in deviceVersion]
        else:
            deviceAndroidVersion = list(
                os.popen('adb shell getprop ro.build.version.release').readlines())
            deviceVersion = [re.findall(r'^\w*\b', i) for i in deviceAndroidVersion]
            return [i[0] for i in deviceVersion]

    def get_devices_model(self , devices = None):
        if devices is not None:
            devicesModel = list(
                os.popen('adb -s {0} shell getprop ro.product.model'.format(devices)).readlines())
            return [i.split('\n')[0] for i in devicesModel]
        else:
            devicesModel = list(
                os.popen('adb shell getprop ro.product.model').readlines())
            return [i.split('\n')[0] for i in devicesModel]

    def get_devices_size(self , devices = None):
        if devices is not None:
            deviceSize = list(os.popen('adb -s {0} shell wm size'.format(devices)).readlines())
            return [i.split('\n')[0] for i in deviceSize]
        else:
            deviceSize = list(os.popen('adb shell wm size').readlines())
            return [i.split('\n')[0] for i in deviceSize]

    def get_devices_ip(self , devices = None):
        if devices is not None:
            deviceIp = list(os.popen('adb -s {0} shell ifconfig | grep Mask'.format(devices)).readlines())
            return [i.split('\n')[0].lstrip() for i in deviceIp]
        else:
            deviceIp = list(os.popen('adb shell ifconfig | grep Mask').readlines())
            return [i.split('\n')[0].lstrip() for i in deviceIp]

    def get_devices_wlan(self , devices = None):
        if devices is not None:
            deviceWlan = list(os.popen('adb -s {0} shell ifconfig wlan0'.format(devices)).readlines())
            return [i.split('\n')[0].lstrip() for i in deviceWlan]
        else:
            deviceWlan = list(os.popen('adb shell ifconfig wlan0'.format(devices)).readlines())
            return [i.split('\n')[0].lstrip() for i in deviceWlan]

    def get_devices_network(self , devices = None):
        if devices is not None:
            deviceNetwork = list(os.popen('adb -s {0} shell netcfg'.format(devices)).readlines())
            return [i for i in deviceNetwork]
        else:
            deviceNetwork = list(os.popen('adb shell netcfg'.format(devices)).readlines())
            return [i for i in deviceNetwork]

    def get_devices_cpu_info(self , devices = None):
        if devices is not None:
            deviceCpu = list(os.popen('adb -s {0} shell cat /proc/cpuinfo'.format(devices)).readlines())
            return [i.split('\n')[0] for i in deviceCpu]
        else:
            deviceCpu = list(os.popen('adb shell cat /proc/cpuinfo').readlines())
            return [i.split('\n')[0] for i in deviceCpu]

    def get_devices_memry(self , devices = None):
        if devices is not None:
            deviceMemry = list(os.popen('adb -s {0} shell cat /proc/meminfo'.format(devices)).readlines())
            return [i.split('\n')[0] for i in deviceMemry]
        else:
            deviceMemry = list(os.popen('adb shell cat /proc/meminfo').readlines())
            return [i.split('\n')[0] for i in deviceMemry]

    def install_app_to_devices(self , devices = None , path = None):
        if devices is not None and path is not None:
            startTime = time.time()
            installApp = list(os.popen('adb -s {0} install {1}'.format(devices , path)).readlines())
            endTime = time.time()
            return [i for i in installApp] , endTime - startTime
        else:
            installApp = list(os.popen('adb install {0}'.format(path)).readlines())
            return [i for i in installApp]

    def uninstall_app_to_devices(self , devices = None , package = None):
        if devices is not None and package is not None:
            uninstallApp = list(os.popen('adb -s {0} uninstall {1}'.format(devices , package)).readlines())
            return [i for i in uninstallApp]
        else:
            uninstallApp = list(os.popen('adb uninstall {0}'.format(package)).readlines())
            return [i for i in uninstallApp]

    def get_devices_package_info(self , path = None):
        if path is not None:
            packageInfo = list(os.popen('aapt dump badging ' + path).readlines())
            return [i for i in packageInfo if 'package' in i]

    def get_devices_main_activity(self , path = None):
        if path is not None:
            packageInfo = list(os.popen('aapt dump badging ' + path).readlines())
            return [i for i in packageInfo if 'launchable-activity' in i]

    def is_install_app(self , devices = None):
        if devices is not None:
            isInstallApp = list(os.popen('adb -s {0} shell pm list packages'.format(devices)).readlines())
            return [i.split('\n')[0] for i in isInstallApp]
        else:
            isInstallApp = list(os.popen('adb shell pm list packages'.format(devices)).readlines())
            return [i.split('\n')[0] for i in isInstallApp]

if __name__ == '__main__':
    pass
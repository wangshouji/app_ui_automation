# coding:utf-8
import yaml
import os
import re

if __name__ == '__main__' :
    curPath = os.path.dirname(os.path.realpath(__file__)) + os.sep + os.sep.join(["android"])
    print(curPath)
    yamlPath = os.path.join(curPath, "bwm.yml")
    print(yamlPath)
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()

    d = yaml.load(cfg)  # 用load方法转字典
    print(d)

    # # 读取设备 id
    # readDeviceId = list(os.popen('adb devices').readlines())
    #
    # # 正则表达式匹配出 id 信息
    # deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
    # print(readDeviceId)
    # print(deviceId)
    #
    # # 读取设备系统版本号
    # deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    # deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
    # print(deviceAndroidVersion)
    # print(deviceVersion)
    #
    # # 读取 APK 的 package 信息
    # appPackageAdb = list(os.popen('aapt dump badging ' + appLocation).readlines())
    # appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]
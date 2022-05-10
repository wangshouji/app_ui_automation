#!/user/bin/env python
#coding=utf-8
import six
import re
import os
import allure
import jieba

#driver = MyUiautomatorDriver('emulator-5556' , 'de.b.connected.cn.int')

class Common(object):

    def __init__(self , platform = None ,automation = None , automationName = None, udid = None , port = None ,bp =None):

        self.platform = platform
        self.automation = automation
        self.automationName = automationName
        self.udid = udid
        self.port = port
        self.bp = bp

        self.clicked = ['\u70b9\u51fb',#点击
                        '\u70b9\u5f00',#点开
                        '\u5c55\u5f00',#展开
                        'click',
                        '\u70b9'#点
                        ]

        self.send_key = ['\u8f93\u5165',#输入
                         '\u5199\u5165',#写入
                         'input',
                         'send_keys',
                         '\u8f93'#输
                         ]

        self.asserts = ['\u65ad\u8a00',#断言
                        '\u5224\u65ad',#判断
                        '\u68c0\u67e5',#检查
                        'assert'
                        ]

        self.values = ['\u83b7\u53d6\u5185\u5bb9',#获取内容
                       '\u53d6\u503c',#取值
                       'text'
                       ]


        self.terms = ['\u4e0b\u4e00\u6b65',#下一步
                      '\u6743\u9650\u6846',#权限框
                      '数字1',
                      '数字2',
                      '数字3',
                      '数字4'
                      ]

        self.add_jieba_word()

        if platform == 'android':
            if automation == 'uiautomator2':
                from uiautomator2_up.u2_module import MyUiautomatorDriver
                self.driver = MyUiautomatorDriver(udid)
            elif automation == 'appium':
                from appium_up.appium_android_module import MyAppiumAndroidDriver
                self.driver = MyAppiumAndroidDriver(platformName=platform , automationName=automationName ,
                                                    udid=udid , port = port , systemPort=bp)
        elif platform == 'ios':
            if automation == 'appium':
                from appium_up.appium_ios_module import MyAppiumIosDriver
                self.driver = MyAppiumIosDriver(platformName=platform , automationName= automationName ,
                                                udid = udid , port= port ,systemPort= bp)

    def init_install_app(self):
        self.driver.reset_install_app()

    def add_jieba_word(self):
        for i in self.clicked:
            jieba.add_word(i)

        for i in self.send_key:
            jieba.add_word(i)

        for i in self.asserts:
            jieba.add_word(i)

        for i in self.values:
            jieba.add_word(i)

        for i in self.terms:
            jieba.add_word(i)

    def parse_click(self , text):
        start = True
        num = 1
        while start:
            ltm = []
            for i in self.clicked:
                if text.find(i) == -1:
                    mm = 9999999
                else:
                    mm = text.find(i)
                ltm.append(mm)

            if min(ltm) == max(ltm):
                start = False
                break

            text = text.replace(self.clicked[ltm.index(min(ltm))], '{A%s}' % str(num), 1)
            sp = text.split(',')
            for i in sp:
                if i.find('{A%s}' % str(num)) >= 0:
                    parm = i.split('}')[1]
                    break
            parm = parm.replace(' ', '', parm.count(' '))
            parm = parm.replace(':', '', parm.count(':'))
            text = text.replace(parm, '{P%s}' % str(num), 1)
            # stt = re.sub(r'}(.*?),', "}{P%s}"%str(num), stt)
            num += 1
        return text

    def parse_send_key(self , text):
        start = True
        num = 1
        while start:
            ltm = []
            for i in self.send_key:
                if text.find(i) == -1:
                    mm = 9999999
                else:
                    mm = text.find(i)
                ltm.append(mm)

            if min(ltm) == max(ltm):
                start = False
                break

            text = text.replace(self.send_key[ltm.index(min(ltm))], '{S%s}' % str(num), 1)
            sp = text.split(',')
            for i in sp:
                if i.find('{S%s}' % str(num)) >= 0:
                    parm = i.split('}')[1]
                    break
            tep = parm.split(':')
            parm = tep[1]
            parm = parm.replace(' ', '', parm.count(' '))
            parm = parm.replace(':', '', parm.count(':'))
            text = text.replace(parm, '{PS%s}' % str(num), 1)
            value = tep[2]
            value = value.replace(' ', '', value.count(' '))
            value = value.replace(':', '', value.count(':'))
            text = text.replace(value, '{V%s}' % str(num), 1)
            # stt = re.sub(r'}(.*?),', "}{P%s}"%str(num), stt)
            num += 1
        return text


    def parse_asserts(self , text):
        start = True
        num = 1
        while start:
            ltm = []
            for i in self.asserts:
                if text.find(i) == -1:
                    mm = 9999999
                else:
                    mm = text.find(i)
                ltm.append(mm)

            if min(ltm) == max(ltm):
                start = False
                break

            text = text.replace(self.clicked[ltm.index(min(ltm))], '{A%s}' % str(num), 1)
            sp = text.split(',')
            for i in sp:
                if i.find('{A%s}' % str(num)) >= 0:
                    parm = i.split('}')[1]
                    break
            parm = parm.replace(' ', '', parm.count(' '))
            parm = parm.replace(':', '', parm.count(':'))
            text = text.replace(parm, '{P%s}' % str(num), 1)
            # stt = re.sub(r'}(.*?),', "}{P%s}"%str(num), stt)
            num += 1
        return text

    def parse_file(self , path):
        data = []
        ids = []
        pth = [path + os.sep + m for m in os.listdir(path) if m.find('.feature') >= 0]
        print(pth)
        for f in pth:
            for line in open(f ,encoding= 'utf-8'):
                if line != '\n' and line !='':
                    if line.find('Feature') >= 0 or line.find('feature') >= 0:
                        dct = {}
                        text = ''
                        text += line
                        dct['text'] = text
                    if line.find('Given') >= 0 or line.find('given') >= 0:
                        line = ':'.join(jieba.lcut(line))
                        line = line.replace(line[5:6] , '', 1)
                        dct['given'] = self.parse_send_key(self.parse_click(line[5:].strip().lstrip()))
                        text += line
                        dct['text'] = text

                    if line.find('When') >= 0 or line.find('when') >= 0:
                        line = ':'.join(jieba.lcut(line))
                        line = line.replace(line[4:5], '', 1)
                        dct['when'] = self.parse_send_key(self.parse_click(line[4:].strip().lstrip()))
                        text += line
                        dct['text'] = text

                    if line.find('Then') >= 0 or line.find('then') >= 0:
                        line = ':'.join(jieba.lcut(line))
                        line = line.replace(line[4:5], '', 1)
                        dct['then'] = self.parse_send_key(self.parse_click(line[4:].strip().lstrip()))
                        text += line
                        dct['text'] = text
                        try:
                            data.append((dct))
                        except UnboundLocalError as e:
                            print(e)

                    if line.find('Scenario') >= 0 or line.find('scenario') >= 0:
                        text += line
                        dct['text'] = text
                        ids.append(line[8:])

        return data , ids

    def run(self , **kwargs):

        for i in kwargs.keys():
            if 'S' in i and 'PS' not in i:
                with allure.step(kwargs[i] + kwargs['PS' + i[1:]] + kwargs['V' + i[1:]]):
                    allure.attach(kwargs[i] ,kwargs[i] + kwargs['PS' + i[1:]] + kwargs['V' + i[1:]])
                    print(kwargs[i], kwargs['PS' + i[1:]], kwargs['V' + i[1:]])
                    self.driver.send_key(kwargs['PS' + i[1:]], kwargs['V' + i[1:]])


            if 'A' in i:
                with allure.step(kwargs[i] + kwargs['P' + i[1:]]):
                    allure.attach(kwargs[i], kwargs[i] + kwargs['P' + i[1:]])
                    print(kwargs[i], kwargs['P' + i[1:]])
                    self.driver.click(kwargs['P' + i[1:]])


if __name__ == '__main__' :

    #print('\u4f60\u597d')
    stt = '点击单选框,点击同意,点击下一步,点击下一步,点击下一步,点击完成,点击权限框,输入账号13500000000,输入密码111111,点击登陆'
    #print(stt.replace('\u70b9\u51fb','{click0}' , 1))
    #stt = com.parse_send_key(stt)
    #print(stt.index('\u70b9\u51fb'))
    #print(stt)

    #print(com.parse_file('../test/features')[0])

    dt = {'S1': '输入', 'PS1': '用户名', 'V1': 'shouji.wang.o', 'S2': '输入',
          'PS2': '密码', 'V2': '129378419283','A1': '点击', 'P1': '登录'}

    dt['B1'] = 'get'

    # for i in dt.keys():
    #     if 'S' in i and 'PS' not in i:
    #         print(dt[i],dt['PS'+i[1:]] , dt['V'+i[1:]])
    #         driver.send_key(dt['PS'+i[1:]] , dt['V'+i[1:]])
    #         #print(attr)
    #
    #     if 'A' in i:
    #         print(dt[i] , dt['P'+i[1:]])
    #         driver.click(dt['P'+i[1:]])
    #         #print(attr)



    sttrt = 'a: :aasd'

    print(sttrt.replace(sttrt[1:2] , '' , 1))


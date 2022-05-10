目录结构：
    api                     api接口脚本存放目录
    behave                  固定框架
    config                  配置文件
    page_object             页面元素封装目录
    selenium_up selenium    二次封装目录
    test/steps              脚本执行文件固定不需要修改
    test/feaures            用例编写目录
    utils                   公共脚本文件


1.在utils下，common文件中，目前抽取2类事件特征：
    点击事件：
                        ['\u70b9\u51fb',#点击
                        '\u70b9\u5f00',#点开
                        '\u5c55\u5f00',#展开
                        'click',
                        '\u70b9'#点
                        ]

    输入事件：           ['\u8f93\u5165',#输入
                         '\u5199\u5165',#写入
                         'input',
                         'send_keys',
                         '\u8f93'#输
                         ]

    语法：[|点击事件|：|元素|]  {A1:P1,A2:P2,A3:P3,A4:P4,A5:P5}
         [|输入事件|：|元素|：|参数|]


         [|判断|：|元素1|：|text|：|元素2|：||text]

    如果定义新的事件可以按照当前模板增加


2.在test下，features文件下编写用例，格式如下：
        Feature:管理平台                ------模块
        Scenario:登录                  ------用例名称

        Given 输入:用户名:login          -----构建前置条件
        When 输入:密码:password         ------执行过程
        Then 点击:登录                  ------预期结果

        一个用例由以上5部分组成，不可缺少


3.在selenium下，对selenium二次封装，目前只封装了点击、输入事件

    当增加新的封装方法时，同时需要在common中定义新的方法的语法结构


4.在page_object下，对页面元素封装成对象，例如：

 class Login(object):

    def __init__(self):
        pass

    @func_name('用户名')
    def get_attr1(self):
        return {'type': 'text',
                'class': 'textbox-text validatebox-text',
                'autocomplete': 'off',
                'placeholder': '用户名',
                'style': 'padding: 11px 12px; margin-left: 38px; margin-right: 0px; width: 214px;',
                'xpath':'//*[@id="p_login"]/div/div[2]/div[1]/span/input[1]'}



5.执行进入test目录下，在命令窗口执行py.test steps/test_start.py --html=logs/log.html --cmdopt=appium --capture=no 或 --alluredir xxxx


    py.test steps/test_start.py --alluredir=/Users/Shared/Jenkins/Home/workspace/bmw_app_automation/allure-results --platform=android --automation=uiautomator2 --device={0} --capture=no


##切换环境：C:\Users\QXY0087\AppData\Local\Continuum\miniconda3\Scripts\activate untitled7

##mac  source activate uiautomator2



#!/user/bin/env python
#coding=utf-8
import threading
import time
import allure
from utils.common import Common

class MyThreading(threading.Thread):

    def __init__(self , platform = None , automation = None, device = None):
        super(MyThreading , self).__init__()
        self.platform = platform
        self.automation = automation
        self.device = device
        self.index = 1
        self.mutex = threading.Lock()
        self.com = Common(platform = self.platform , automation=self.automation , device=self.device)


    def run(self):
        while True:
            if self.mutex.acquire(1):
                if self.index == 1:
                    self.com.init_install_app()
                    self.index = 0
                elif self.index == 2:
                    with allure.step(self.device):
                        self.com.run(**self.kwargs)
                        self.index = 0
                self.mutex.release()

    def run_case(self , **kwargs):
        self.index = 2
        self.kwargs = kwargs

    def stop(self):
        pass



if __name__ == '__main__':
    devices = MyDevices()
    dat = devices.get_all_devices()
    m = MyThreading(dat[0] , 'de.bw.connected.cn.int')
    n = MyThreading(dat[1] , 'de.bw.connected.cn.int')
    m.start()
    n.start()

    print('end')
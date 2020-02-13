# coding:utf-8
__author__ = 'Eki'
'''
description:drvier配置
'''

from appium import webdriver

class driver_configure():

    def get_driver(self):
        '''獲取driver'''
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '5.1.1'
        self.desired_caps['appPackage'] = 'appPackage'
        self.desired_caps['appActivity'] = 'appActivity'
        self.desired_caps['unicodeKeyboard'] = 'true'# 是否支持unicode的鍵盤。如果需要输入中文，設為“true”
        self.desired_caps['resetKeyboard'] = 'true'# 是否在測試結束後將鍵盤設為系統預設的輸入法。
        self.desired_caps['deviceName'] = '127.0.0.1:62001'#手機or模擬器ID
        self.desired_caps['noReset'] = 'true'#true:不重新安装APP，false:重新安装
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        return self.driver

#
#
# if __name__=='__main__':
#     TestPage = driver_configure()
#     TestPage.get_driver()
#     TestPage.test()
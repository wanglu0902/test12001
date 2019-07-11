from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseSetting(object):
    # 初始化
    def __init__(self,driver):
        # # server 启动参数
        # desired_caps = {}
        # # 设备信息
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '5.1'
        # desired_caps['deviceName'] = '192.168.56.101:5555'
        # # app信息
        # desired_caps['appPackage'] = 'com.android.settings'
        # desired_caps['appActivity'] = '.Settings'
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver = driver
    # 查找元素
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 输入方法
    def base_input(self,loc,value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 点击方法
    def base_click(self,loc):
        self.base_find_element(loc).click()
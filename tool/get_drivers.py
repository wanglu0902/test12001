from appium import webdriver


class GetDriver(object):

    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            # server 启动参数
            desired_caps = {}
            # 设备信息
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # app信息
            desired_caps['appPackage'] = 'com.android.settings'
            desired_caps['appActivity'] = '.Settings'
            cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
import os
import sys
sys.path.append(os.getcwd())

from tool.get_drivers import GetDriver



import pytest

from page.page_setting import PageSetting


class TestSetting(object):

    # 初始化
    def setup(self):
        driver = GetDriver.get_driver()
        self.setting = PageSetting(driver)

    # 结束
    def teardown(self):
        self.setting.driver.quit()

    #测试方法
    @pytest.mark.parametrize("text",["123"])
    def test_setting(self,text):
        self.setting.page_setting(text)

# if __name__ == '__main__':
#     pytest.main("-s test_setting.py")
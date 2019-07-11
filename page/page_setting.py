import page

from base.base_setting import BaseSetting


class PageSetting(BaseSetting):
    # 点击搜索按钮
    def click_search_btn(self):
        self.base_click(page.search_btn)

    #输入
    def input_text(self,text):
        self.base_input(page.send_box,text)

    # 点击搜索框返回按钮
    def click_go_back_btn(self):
        self.base_click(page.go_back_btn)

    # 组合业务
    def page_setting(self,text):
        self.click_search_btn()
        self.input_text(text)
        self.click_go_back_btn()
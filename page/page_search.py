import allure

import page
from base.base_action import BaseAction


class PageSearch(BaseAction):

    # 获取最近搜索内容
    def page_search_get_recent_search_text(self):
        return self.base_get_text(page.recent_search)

    # 点击搜索放大镜
    def page_search_img_click(self):
        self.base_click(page.index_search_btn)

    # 输入搜索内容
    def page_search_input(self, value):
        self.base_input(page.text_search_keyword, value)

    # 点击搜索按钮
    def page_search_btn_click(self):
        self.base_click(page.button_search)

    # 搜索界面 返回按钮
    def page_search_list_btn_back_click(self):
        self.base_click(page.search_list_btn_back)

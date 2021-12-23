import time

from base.base_analyze import analyze_file
from base.base_driver import GetDriver
from page.page import Page
import pytest


class TestLogin:

    def setup(self):
        self.driver = GetDriver.init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        GetDriver.quit_driver()

    def test_recent_search(self):
        # 判断是否登录，没有登录则登录
        self.page.page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击首页
        self.page.page_home.page_home_index_click()
        # 点击搜索放大镜
        self.page.page_search.page_search_img_click()
        # 输入搜索内容
        self.page.page_search.page_search_input("nike")
        # 点击搜索按钮
        self.page.page_search.page_search_btn_click()
        # 返回
        time.sleep(1)
        self.page.page_search.page_search_list_btn_back_click()
        # 获取最近搜索
        time.sleep(1)
        recent_search = self.page.page_search.page_search_get_recent_search_text()
        assert "nike" == recent_search
        time.sleep(5)

import time
from base.base_analyze import analyze_file
from base.base_driver import GetDriver
from page.page import Page
import pytest


class TestClearCache:

    def setup(self):
        self.driver = GetDriver.init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        GetDriver.quit_driver()

    def test_clear_cache(self):
        page_login = self.page.page_login
        # 判断是否登录，没有登录则登录
        page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击 设置按钮
        self.page.page_me.page_me_setting_button_click()
        # 点击清理缓存
        self.page.page_setting.page_setting_clear_cache_click()
        # 判断 toast是否存在
        assert self.page.page_setting.base_is_toast_exist("清理成功")

import time
from base.base_analyze import analyze_file
from base.base_driver import GetDriver
from page.page import Page
import pytest


class TestUpdate:

    def setup(self):
        self.driver = GetDriver.init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        GetDriver.quit_driver()

    def test_update(self):
        page_login = self.page.page_login
        # 判断是否登录，没有登录则登录
        page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击 设置按钮
        self.page.page_me.page_me_setting_button_click()
        # time.sleep(2)
        # 点击关于百年奥莱
        self.page.page_setting.page_setting_about_yunmall_click()
        # 点击版本更新
        self.page.page_about_yunmall.page_yunmall_version_update_click()
        # 判断 toast是否存在
        assert  self.page.page_about_yunmall.base_is_toast_exist("最新版本")

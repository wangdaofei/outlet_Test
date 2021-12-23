import time
from base.base_analyze import analyze_file
from base.base_driver import GetDriver
from page.page import Page
import pytest


class TestVip:

    def setup(self):
        self.driver = GetDriver.init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        GetDriver.quit_driver()

    @pytest.mark.parametrize("args", analyze_file("data_vip.yaml", "test_vip"))
    def test_vip(self, args):
        element = args["element"]
        # 判断是否登录，没有登录则登录
        self.page.page_login.page_login_if_not_login(self.page)
        self.page.page_me.page_me_help_click()
        # time.sleep(20)

        # ['NATIVE_APP', 'WEBVIEW_cn.goapk.market', 'WEBVIEW_com.yunmall.lc']
        print(self.driver.contexts)
        # 切换环境进入 html
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        print(self.driver.current_context)
        # 点击帮助页面 如何注册超级VIP
        self.page.page_help.page_help_login_vip_click()
        # 找到如何注册超级VIP页面的 点此链接元素
        # assert self.page.page_vip.page_vip_find_register_vip_link()
        # 轮询page_source，找到 点击此链接  文字
        flag = self.page.page_vip.base_page_source_element_if_exist(element)
        assert flag, "%s不在page_source中" % element
        # 切换环境进入 回到app
        self.driver.switch_to.context("NATIVE_APP")
        # 点击关闭键
        self.page.page_vip.page_vip_close_btn_click()

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
        GetDriver.quit_driver()

    @pytest.mark.parametrize("args", analyze_file("data_login.yaml", "test_login"))
    def test_login(self, args):
        # 解析yaml的数据
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        page_home = self.page.page_home
        # 点击同意
        page_home.page_home_aggre_click()
        # 点击我的
        page_home.page_home_me_click()

        # 点击已有账号 登入
        page_register = self.page.page_register
        page_register.page_register_me_have_account_login_click()

        # 输入用户名、密码、点击登录
        page_login = self.page.page_login
        page_login.page_login_input_username(username)
        page_login.page_login_input_password(password)
        page_login.page_login_button_click()

        # 断言是否成功登录
        if toast is None:
            nickname = self.page.page_me.page_me_get_nickname()
            assert nickname == username, "登录后的用户名和输入的用户名不一致"
        else:
            # 找toast提示，看是否和args中的toast提示相同
            assert self.page.page_login.base_is_toast_exist(toast)

    def test_if_login(self):
        # page_home = self.page.page_home
        # # 点击同意
        # page_home.page_home_aggre_click()
        # # 点击我的
        # page_home.page_home_me_click()
        # # 如果没有登录则登录
        self.page.page_login.page_login_if_not_login(self.page)

import allure

import page
from base.base_action import BaseAction


class PageRegister(BaseAction):

    # 点击我已有账号，去登录
    @allure.step(title="点击 我已经有账号 去登录")
    def page_register_me_have_account_login_click(self):
        self.base_click(page.me_have_account_login)

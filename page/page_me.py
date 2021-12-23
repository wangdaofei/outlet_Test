import allure

import page
from base.base_action import BaseAction


class PageMe(BaseAction):

    # 登入之后获取我的用户名
    @allure.step(title="登入之后获取我的用户名")
    def page_me_get_nickname(self):
        return self.base_get_text(page.user_nikename)

    # 登录之后点击设置按钮
    @allure.step(title="点击设置按钮")
    def page_me_setting_button_click(self):
        self.base_click(page.me_setting_button)

    # 帮助页面点击
    @allure.step(title="点击帮助页面")
    def page_me_help_click(self):
        self.base_click((page.me_help_center))



import allure

import page
from base.base_action import BaseAction


class Page_about_yunmall(BaseAction):
    # 点击版本更新
    @allure.step(title="点击版本更新")
    def page_yunmall_version_update_click(self):
        self.base_click(page.about_yunmall_version_update)



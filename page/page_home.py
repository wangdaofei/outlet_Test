import page
from base.base_action import BaseAction


class PageHome(BaseAction):

    # 点同意
    def page_home_aggre_click(self):
        self.base_click(page.home_aggre)

    # 点击我
    def page_home_me_click(self):
        self.base_click(page.home_me)


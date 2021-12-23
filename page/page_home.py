import allure

import page
from base.base_action import BaseAction


class PageHome(BaseAction):

    # 点同意
    @allure.step(title="主页 点击 同意")
    def page_home_aggre_click(self):
        self.base_click(page.home_aggre)

    # 点击我
    @allure.step(title="主页 点击 我的")
    def page_home_me_click(self):
        self.base_click(page.home_me)

    # 点分类
    @allure.step(title="主页 点击 分类")
    def page_home_category_click(self):
        self.base_click(page.home_category)

    # 点击 购物车 tab_shopping_cart
    def page_home_shopping_cart_click(self):
        self.base_click(page.tab_shopping_cart)

    #点击 首页
    def page_home_index_click(self):
        self.base_click(page.tab_home)
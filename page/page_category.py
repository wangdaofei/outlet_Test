import random

import allure

import page
from base.base_action import BaseAction


class PageCategory(BaseAction):

    # 随机点击商品列表的类目
    @allure.step(title="随机点击商品列表的类目")
    def page_category_goods_random_click(self):
        category_goods = self.base_find_elements(page.category_goods)
        count = len(category_goods)
        index = random.randint(0, count - 1)
        category_goods[index].click()

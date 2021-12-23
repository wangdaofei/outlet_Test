import random

import allure

import page
from base.base_action import BaseAction


class PageGoodsList(BaseAction):
    # 随机点击商品
    @allure.step(title="随机点击商品")
    def page_goods_list_random_click(self):
        good_elements = self.base_find_elements(page.good_elements)
        count = len(good_elements)
        index = random.randint(0, count - 1)
        good_elements[index].click()

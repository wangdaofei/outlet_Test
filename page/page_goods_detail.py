import random
import time

import allure
from selenium.webdriver.common.by import By

import page
from base.base_action import BaseAction


class PageGoodsDetail(BaseAction):

    # 点击假如购物车
    @allure.step(title="点击加入购物车")
    def page_goods_detail_add_to_cart_click(self):
        self.base_click(page.btn_add_to_shopping_cart)

    # 点击 确定 按钮  detail_sure_btn
    @allure.step(title="点击确定按钮")
    def page_goods_detail_sure_btn_click(self):
        self.base_click(page.detail_sure_btn)

    # 根据 请选择 分类、规格  获取 请选择后面的 第一个规格的文字
    @allure.step(title="获取请选择后面 第一个词语")
    def page_goods_detail_get_choose_spec(self, text):
        return text.split(" ")[1]

    # 选择 分类和规格
    @allure.step(title="选择分类和规格")
    def page_goods_detail_chose_spec_click(self):

        while True:
            # 点击确定按钮
            self.page_goods_detail_sure_btn_click()
            if self.base_is_toast_exist("请选择"):
                spec_name = self.page_goods_detail_get_choose_spec(self.base_get_toast_text("请选择"))
                loc = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % spec_name
                self.base_click(loc)
                time.sleep(2)
            else:
                break

    # 获取商品标题product_title
    @allure.step(title="获取商品标题")
    def page_goods_detail_get_product_title(self):
        return self.base_get_text(page.product_title)

    # 点击购物车图标按钮  btn_shopping_cart
    @allure.step(title="点击购物车图标")
    def page_goods_detail_btn_shopping_cart_click(self):
        return self.base_click(page.btn_shopping_cart)

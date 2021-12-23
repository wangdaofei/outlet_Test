import random
import re

import allure

import page
from base.base_action import BaseAction


class PageShopCart(BaseAction):

    # 获取商品标题product_title ,如果购物车中没有商品，则返回False
    @allure.step(title="获取购物车第一个商品的title")
    def page_shop_cart_get_first_product_title(self):
        try:
            return self.base_get_text(page.product_title)
        except Exception:
            print("购物车中没有商品")
            return False

    """
    找到当前页面的  前两个 商品 并点击选中  tv_invalid_tag 并返回价格
    tv_price = By.ID, "com.yunmall.lc:id/tv_price"
    tv_num = By.ID, "com.yunmall.lc:id/tv_num"
    """

    def page_shop_cart_get_checked_price(self):
        goods = self.base_find_elements(page.tv_invalid_tag)
        total_price = 0
        if len(goods) >= 2:
            goods[0].click()
            goods[1].click()
            tv_prices = self.base_find_elements(page.tv_price)
            tv_nums = self.base_find_elements(page.tv_num)
            for i in range(2):
                tv_price = float(re.findall(r"\d+", tv_prices[i].text)[0])
                tv_num = float(re.findall(r"\d+", tv_nums[i].text)[0])
                tem_price = tv_price * tv_num
                total_price += tem_price
            # print(total_price)
            return total_price
        else:
            print("测试条件不足，请先添加商品至大于两样")
            return False

    # tv_count_money 获取总价
    def page_shop_cart_get_count_money(self):
        tv_count_money = self.base_get_text(page.tv_count_money)
        return float(re.findall(r"\d+", tv_count_money)[0])

    # 点击编辑按钮
    def page_shop_cart_edit_btn_click(self):
        self.base_click(page.tv_right_second)

    # 点击全选按
    def page_shop_cart_select_all_btn_click(self):
        self.base_click(page.iv_select_all)

    # 点击删除按钮
    def page_shop_cart_del_all_click(self):
        self.base_click(page.tv_del_all)

    # 确定删除
    def page_shop_cart_sure_delete_click(self):
        self.base_click(page.ymdialog_right_button)

    # 如果购物车有商品则删除全部
    def page_shop_cart_delete_all(self):
        if self.page_shop_cart_get_first_product_title():
            # 点击编辑按钮
            self.page_shop_cart_edit_btn_click()
            # 点击全选
            self.page_shop_cart_select_all_btn_click()
            # 点击删除
            self.page_shop_cart_del_all_click()
            # 点击确定
            self.page_shop_cart_sure_delete_click()
            print("删除成功")

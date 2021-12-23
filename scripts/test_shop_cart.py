import time
from base.base_analyze import analyze_file
from base.base_driver import GetDriver
from page.page import Page
import pytest


class TestShopCart:

    def setup(self):
        self.driver = GetDriver.init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        GetDriver.quit_driver()

    def test_add_shop_cart(self):
        # 判断是否登录，没有登录则登录
        self.page.page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击 分类
        self.page.page_home.page_home_category_click()
        # 分类里随机点一个类目
        self.page.page_category.page_category_goods_random_click()
        # 随机点一个商品
        self.page.page_goods_list.page_goods_list_random_click()
        # 点击加入购物车
        self.page.page_goods_detail.page_goods_detail_add_to_cart_click()
        # 选择规格
        self.page.page_goods_detail.page_goods_detail_chose_spec_click()
        # 获取商品的 标题
        product_title = self.page.page_goods_detail.page_goods_detail_get_product_title()
        # 点击购物车图标
        self.page.page_goods_detail.page_goods_detail_btn_shopping_cart_click()
        time.sleep(2)
        # 获取购物车中第一件商品的标题
        cart_product_title = self.page.page_shop_cart.page_shop_cart_get_first_product_title()
        # 断言
        assert product_title == cart_product_title, "添加的商品不在购物车，请检查代码"

    def test_shop_cart_price(self):
        # 判断是否登录，没有登录则登录
        self.page.page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击 购物车
        self.page.page_home.page_home_shopping_cart_click()
        # 选中当前页的 前两个商品
        time.sleep(2)
        checked_price = self.page.page_shop_cart.page_shop_cart_get_checked_price()
        time.sleep(3)
        count_money = self.page.page_shop_cart.page_shop_cart_get_count_money()
        print("checked_price", checked_price)
        print("count_money", count_money)
        assert checked_price == count_money, "购物车价格计算有误"
        time.sleep(5)

    def test_delete_all(self):
        # 判断是否登录，没有登录则登录
        self.page.page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击 购物车
        self.page.page_home.page_home_shopping_cart_click()
        time.sleep(2)
        self.page.page_shop_cart.page_shop_cart_delete_all()
        time.sleep(5)

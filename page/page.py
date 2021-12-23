from page.page_about_yunmall import Page_about_yunmall
from page.page_address_manage import PageAddressManage
from page.page_category import PageCategory
from page.page_edit_address import PageEditAddress
from page.page_goods_detail import PageGoodsDetail
from page.page_goods_list import PageGoodsList
from page.page_help import PageHelp
from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_me import PageMe
from page.page_register import PageRegister
from page.page_search import PageSearch
from page.page_setting import PageSetting
from page.page_shop_cart import PageShopCart
from page.page_vip import PageVip


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def page_home(self):
        return PageHome(self.driver)

    @property
    def page_register(self):
        return PageRegister(self.driver)

    @property
    def page_login(self):
        return PageLogin(self.driver)

    @property
    def page_me(self):
        return PageMe(self.driver)

    @property
    def page_setting(self):
        return PageSetting(self.driver)

    @property
    def page_about_yunmall(self):
        return Page_about_yunmall(self.driver)

    @property
    def page_help(self):
        return PageHelp(self.driver)

    @property
    def page_vip(self):
        return PageVip(self.driver)

    @property
    def page_address_manage(self):
        return PageAddressManage(self.driver)

    @property
    def page_edit_address(self):
        return PageEditAddress(self.driver)

    @property
    def page_category(self):
        return PageCategory(self.driver)

    @property
    def page_goods_list(self):
        return PageGoodsList(self.driver)

    @property
    def page_goods_detail(self):
        return PageGoodsDetail(self.driver)

    @property
    def page_shop_cart(self):
        return PageShopCart(self.driver)



    @property
    def page_search(self):
        return PageSearch(self.driver)
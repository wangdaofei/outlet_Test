import random
import time

import allure
from selenium.webdriver.common.by import By

import page
from base.base_action import BaseAction

"""
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
address_province = By.ID, "com.yunmall.lc:id/address_province"
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
address_default = By.ID, "com.yunmall.lc:id/address_default"
"""


class PageEditAddress(BaseAction):
    # 输入收件人
    @allure.step(title="输入收件人")
    def page_edit_address_input_receipt_name(self, receipt_name):
        self.base_input(page.address_receipt_name, receipt_name)

    # 输入手机号
    @allure.step(title="输入手机号")
    def page_edit_address_input_phone(self, phone):
        self.base_input(page.address_add_phone, phone)

    # 输入详细地址
    @allure.step(title="输入详细的地址")
    def page_edit_address_detail_addr_info(self, detail_addr_info):
        self.base_input(page.address_detail_addr_info, detail_addr_info)

    # 输入邮编
    @allure.step(title="输入邮编")
    def page_edit_address_post_code(self, post_code):
        self.base_find_element_with_scroll(page.address_post_code).send_keys(post_code)

    # 设为默认地址
    @allure.step(title="设为默认地址")
    def page_edit_address_default_click(self):
        self.base_find_element_with_scroll(page.address_default).click()

    # 点击所在地区按钮
    @allure.step(title="点击所在区域按钮")
    def page_edit_address_province_click(self):
        self.base_click(page.address_province)

    # 选择所在区域
    @allure.step(title="选择所在地区")
    def page_edit_address_area_select(self):
        # 点击进入所在地区
        self.page_edit_address_province_click()
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            # 获取 当前页地区的元素
            areas = self.base_find_elements(page.area_list)
            # 当前页面地区 的数量
            areas_count = len(areas)
            # 随机取一个 地区
            area_index = random.randint(0, areas_count - 1)
            # 点击这个 地区
            areas[area_index].click()
            time.sleep(1)

        # 选择所在区域

    @allure.step(title="点击保存按钮")
    def page_edit_address_area_save_button(self):
        self.base_click(page.area_save_button)
        print("正在点击保存地址按钮")

    # 输入 新增 的地址，一定正确
    @allure.step(title="输入新增地址信息")
    def page_edit_address_add_new_address(self, receipt_name, phone, detail_addr_info, post_code):
        # 输入新增地址信息
        self.page_edit_address_input_receipt_name(receipt_name)
        self.page_edit_address_input_phone(phone)
        self.page_edit_address_detail_addr_info(detail_addr_info)
        self.page_edit_address_post_code(post_code)
        self.page_edit_address_default_click()
        # 选择地区
        self.page_edit_address_area_select()
        # 点击保存按钮
        self.page_edit_address_area_save_button()

    # 编辑地址
    @allure.step(title="编辑地址")
    def page_edit_address_change_address(self, receipt_name, phone, detail_addr_info, post_code):
        # 输入新增地址信息
        self.page_edit_address_input_receipt_name(receipt_name)
        self.page_edit_address_input_phone(phone)
        self.page_edit_address_detail_addr_info(detail_addr_info)
        self.page_edit_address_post_code(post_code)
        # self.page_edit_address_default_click()
        # 选择地区
        self.page_edit_address_area_select()
        # 点击保存按钮
        self.page_edit_address_area_save_button()

    # 判断是否保存成功
    @allure.step(title="判断地址是否保存成功")
    def page_edit_address_is_save_succee(self):
        return self.base_is_toast_exist("保存成功")

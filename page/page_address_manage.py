import allure

import page
from base.base_action import BaseAction


class PageAddressManage(BaseAction):

    # 地址管理页面中，点击点击新增 地址
    @allure.step(title="点击新增地址")
    def page_address_manage_add_address_click(self):
        self.base_find_element_with_scroll(page.address_add_new_btn).click()

    # 获取默认的姓名 电话信息（排在第一个）用来判断新增是否成功
    @allure.step(title="获取默认地址的用户名")
    def page_address_manage_get_default_name_and_phone(self):
        return self.base_get_text(page.default_receipt_name)

    # 判断 地址管理中 是否有地址
    @allure.step(title="判断地址管理中是否有地址")
    def page_address_manage_is_address_exist(self):
        return self.base_is_element_exist(page.address_is_default)

    # 点击默认地址
    @allure.step(title="点击默认地址")
    def page_address_manage_default_address_click(self):
        self.base_click(page.address_is_default)

    # 点击编辑 按钮
    @allure.step(title="点击编辑按钮")
    def page_address_manage_address_edit_button_click(self):
        self.base_click(page.address_edit_button)

    # 点击删除 按钮
    @allure.step(title="点击删除按钮")
    def page_address_manage_address_delete_button_click(self):
        self.base_click(page.address_delete_button)

    # 判断删除是否存在
    @allure.step(title="判断删除按钮是否存在")
    def page_address_manage_is_delete_exist(self):
        return self.base_is_element_exist(page.address_delete_button)

    # 删除确定按钮
    @allure.step(title="删除之后确定按钮")
    def page_address_manage_delete_confirm_button_click(self):
        return self.base_click(page.address_delete_confirm_button)

import time
from base.base_analyze import analyze_file
from base.base_driver import GetDriver
from page.page import Page
import pytest


class TestAddress:

    def setup(self):
        self.driver = GetDriver.init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        GetDriver.quit_driver()

    @pytest.mark.parametrize("args", analyze_file("data_test_address.yaml", "test_address"))
    def test_add_address(self, args):
        receipt_name = args["receipt_name"]
        phone = args["phone"]
        detail_addr_info = args["detail_addr_info"]
        post_code = args["post_code"]
        toast = args["toast"]

        page_login = self.page.page_login
        # 判断是否登录，没有登录则登录
        page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击 设置按钮
        self.page.page_me.page_me_setting_button_click()
        # 点击地址管理
        self.page.page_setting.page_setting_address_manage_click()
        # 点击新增地址
        self.page.page_address_manage.page_address_manage_add_address_click()
        # 输入新增地址信息
        self.page.page_edit_address.page_edit_address_input_receipt_name(receipt_name)
        self.page.page_edit_address.page_edit_address_input_phone(phone)
        self.page.page_edit_address.page_edit_address_detail_addr_info(detail_addr_info)
        self.page.page_edit_address.page_edit_address_post_code(post_code)
        self.page.page_edit_address.page_edit_address_default_click()

        # 选择地区
        self.page.page_edit_address.page_edit_address_area_select()

        # 点击保存按钮
        self.page.page_edit_address.page_edit_address_area_save_button()

        if toast is None:
            # 保存成功后 返回 地址管理页面 获取第一行 默认地址的 用户名
            default_name_and_phone = self.page.page_address_manage.page_address_manage_get_default_name_and_phone()
            assert default_name_and_phone == "%s  %s" % (receipt_name, phone), "保存失败，地址管理列表中没有查询到新增的地址"
        else:
            assert self.page.page_edit_address.base_is_toast_exist(toast), "保存失败，toast内容和预期不符"

        time.sleep(5)

    # 测试 修改 默认地址
    def test_edit_address(self):
        # 判断是否登录，没有登录则登录
        self.page.page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击 设置按钮
        self.page.page_me.page_me_setting_button_click()
        # 点击地址管理
        self.page.page_setting.page_setting_address_manage_click()
        if not self.page.page_address_manage.page_address_manage_is_address_exist():
            print("列表中没有地址，将新增地址")
            # 点击新增地址
            self.page.page_address_manage.page_address_manage_add_address_click()
            self.page.page_edit_address.page_edit_address_add_new_address("小明", "17858936388", "汤臣一品88号", "314051")
        print("将修改默认地址")
        # 点击默认地址
        self.page.page_address_manage.page_address_manage_default_address_click()
        # 修改地址
        self.page.page_edit_address.page_edit_address_change_address("小明666", "17858936388", "汤臣一品88号", "314051")
        # 断言是否保存成功
        assert self.page.page_edit_address.page_edit_address_is_save_succee(), "保存失败，请检查代码"

    # 测试 全部删除完地址之后 点击编辑按钮 是否还会出现 删除按钮
    def test_delete_address(self):
        # 判断是否登录，没有登录则登录
        self.page.page_login.page_login_if_not_login(self.page)
        time.sleep(1)
        # 点击 设置按钮
        self.page.page_me.page_me_setting_button_click()
        # 点击地址管理
        self.page.page_setting.page_setting_address_manage_click()

        # 判断是否有地址可以删除
        if not self.page.page_address_manage.page_address_manage_is_address_exist():
            print("没有地址可以删除")
        else:
            # 最多只有 10个地址
            for i in range(10):
                # 点击编辑按钮
                self.page.page_address_manage.page_address_manage_address_edit_button_click()
                # 判断删除按钮是否存在,如果不存在 则 break,结束循环
                if not self.page.page_address_manage.page_address_manage_is_delete_exist():
                    print("退出循环")
                    break

                # 如果存在删除 按钮 点击删除按钮
                self.page.page_address_manage.page_address_manage_address_delete_button_click()
                # 删除确定
                self.page.page_address_manage.page_address_manage_delete_confirm_button_click()

            # 再次点击编辑按钮
            self.page.page_address_manage.page_address_manage_address_edit_button_click()
            # 断言，如果存在 删除按钮，则有问题
            assert not self.page.page_address_manage.page_address_manage_is_delete_exist(), "收货地址没有删除完毕"

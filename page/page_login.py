import page
from base.base_action import BaseAction


class PageLogin(BaseAction):

    # 输入用户名
    def page_login_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_login_input_password(self, pwd):
        self.base_input(page.login_password, pwd)

    # 点击登录按钮
    def page_login_button_click(self):
        self.base_click(page.login_button)

    # 成功登录的输入
    def page_login_success(self):
        self.base_input(page.login_username, "itheima_test")
        self.base_input(page.login_password, "itheima")
        self.base_click(page.login_button)

    # 判断是否登录
    def page_is_login(self):
        # 应该判断 是否能获取到nickname判断 是否 登录，之后再修改
        if self.driver.current_activity == "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return False
        else:
            return True

    # 如果没有登录则登录
    def page_login_if_not_login(self, page):
        # page=Page(self.driver)
        page_home = page.page_home
        # 点击同意
        page_home.page_home_aggre_click()
        # 点击我的
        page_home.page_home_me_click()
        # 判断登录状态
        if self.page_is_login():
            return
        else:
            # 如果没有登入则点击 已有账号，去登录
            page.page_register.page_register_me_have_account_login_click()
            self.page_login_success()
            print("登入成功")

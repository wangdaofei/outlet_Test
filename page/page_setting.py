import page
from base.base_action import BaseAction


class PageSetting(BaseAction):

    # 我的 设置页面 点击关于百年奥莱
    def page_setting_about_yunmall_click(self):
        self.base_find_element_with_scroll(page.setting_about_yunmall_button, "up").click()

    # 点击清理缓存
    def page_setting_clear_cache_click(self):
        self.base_find_element_with_scroll(page.setting_clear_cache, "up").click()

    # 点击地址管理
    def page_setting_address_manage_click(self):
        self.base_click(page.setting_address_manage)

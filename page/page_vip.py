import page
from base.base_action import BaseAction


class PageVip(BaseAction):

    # 如何注册超级VIP页面，找到  点此链接页面
    def page_vip_find_register_vip_link(self):
        self.base_find_element(page.register_vip_link)

    # 点击返回
    def page_vip_back_btn_click(self):
        self.base_click(page.vip_left_btn)

    # 点击 close 按钮
    def page_vip_close_btn_click(self):
        self.base_click(page.bip_btn_close)

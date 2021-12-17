from selenium.webdriver.common.by import By

# 首页
home_me = By.ID, "com.yunmall.lc:id/tab_me"

home_aggre = By.ID, "com.yunmall.lc:id/tv_info_share_text"

# 我的 登录 界面
me_have_account_login = By.ID, "com.yunmall.lc:id/textView1"

# 登入界面

login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"

login_password = By.ID, "com.yunmall.lc:id/logon_password_textview"

login_button = By.ID, "com.yunmall.lc:id/logon_button"

# 我的页面
user_nikename = By.ID, "com.yunmall.lc:id/tv_user_nikename"

# 我的页面，左上角设置按钮
me_setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 我的页面 帮助
me_help_center = By.ID, "com.yunmall.lc:id/txt_help_center"

# 我的 设置页面  关于百年奥莱 选项
setting_about_yunmall_button = By.ID, "com.yunmall.lc:id/setting_about_yunmall"
setting_clear_cache = By.ID, "com.yunmall.lc:id/setting_clear_cache"
setting_address_manage = By.ID, "com.yunmall.lc:id/setting_address_manage"

# 关于百年奥莱页面  版本更新
about_yunmall_version_update = By.ID, "com.yunmall.lc:id/about_version_update"

# 帮助页面
help_login_vip = By.XPATH, "//*[contains(text(),'VIP')]"

# 如何注册超级vip页面
register_vip_link = By.XPATH, "//*[contains(text(),'点击此链接')]"
vip_left_btn = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
bip_btn_close = By.ID, "com.yunmall.lc:id/btn_close"

# 设置——>地址管理
address_add_new_btn = By.ID, "com.yunmall.lc:id/address_add_new_btn"
default_receipt_name = By.ID, "com.yunmall.lc:id/receipt_name"
# 用来判断是否有地址
address_is_default = By.ID, "com.yunmall.lc:id/address_is_default"
address_edit_button=By.ID,"com.yunmall.lc:id/ymtitlebar_right_btn"
address_delete_button=By.ID,"com.yunmall.lc:id/delete"
address_delete_confirm_button=By.ID,"com.yunmall.lc:id/ymdialog_left_button"
# 编辑地址页面
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
address_province = By.ID, "com.yunmall.lc:id/address_province"
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
address_default = By.ID, "com.yunmall.lc:id/address_default"
#编辑地址时，选择城市
area_list = By.ID, "com.yunmall.lc:id/area_title"
area_save_button = By.ID, "com.yunmall.lc:id/button_send"

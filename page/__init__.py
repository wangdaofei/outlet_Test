from selenium.webdriver.common.by import By

# 首页
home_me = By.ID, "com.yunmall.lc:id/tab_me"

home_category = By.ID, "com.yunmall.lc:id/tab_category"

home_aggre = By.ID, "com.yunmall.lc:id/tv_info_share_text"

tab_shopping_cart = By.ID, "com.yunmall.lc:id/tab_shopping_cart"

tab_home = By.ID, "com.yunmall.lc:id/tab_home"
# 我的 登录 界面
me_have_account_login = By.ID, "com.yunmall.lc:id/textView1"

# 搜索按钮
index_search_btn = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

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
address_edit_button = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
address_delete_button = By.ID, "com.yunmall.lc:id/delete"
address_delete_confirm_button = By.ID, "com.yunmall.lc:id/ymdialog_left_button"
# 编辑地址页面
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
address_province = By.ID, "com.yunmall.lc:id/address_province"
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 编辑地址时，选择城市
area_list = By.ID, "com.yunmall.lc:id/area_title"
area_save_button = By.ID, "com.yunmall.lc:id/button_send"

# 分类 里面的商品
category_goods = By.ID, "com.yunmall.lc:id/iv_img"
good_elements = By.ID, "com.yunmall.lc:id/iv_element_1"

# 商品详情页
btn_add_to_shopping_cart = By.ID, "com.yunmall.lc:id/btn_add_to_shopping_cart"
detail_sure_btn = By.ID, "com.yunmall.lc:id/select_detail_sure_btn"
product_title = By.ID, "com.yunmall.lc:id/tv_product_title"
btn_shopping_cart = By.ID, "com.yunmall.lc:id/btn_shopping_cart"

# 购物车
tv_invalid_tag = By.ID, "com.yunmall.lc:id/tv_invalid_tag"

tv_price = By.ID, "com.yunmall.lc:id/tv_price"
tv_num = By.ID, "com.yunmall.lc:id/tv_num"
tv_count_money = By.ID, "com.yunmall.lc:id/tv_count_money"
# 编辑按钮
tv_right_second = By.ID, "com.yunmall.lc:id/tv_right_second"
# 全选按钮
iv_select_all = By.ID, "com.yunmall.lc:id/iv_select_all"
# 删除按钮
tv_del_all = By.ID, "com.yunmall.lc:id/tv_del_all"
# 确定删除
ymdialog_right_button = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

# 搜索页面
recent_search = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/keyayout']//*[@class='android.widget.TextView']"
# recent_search = By.XPATH, "//*[@class='android.widget.TextView']"

text_search_keyword = By.ID, "com.yunmall.lc:id/text_search_keyword"

button_search = By.ID, "com.yunmall.lc:id/button_search"

# 搜索界面 返回按钮
search_list_btn_back = By.ID, "com.yunmall.lc:id/btn_back"

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'

desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 找toast
desired_caps['automationName'] = 'Uiautomator2'

# 每次启动是否重置应用
# desired_caps['no_reset'] = no_reset
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def scroll_page_one_time(direction="up"):
    """
    滑动一次屏幕
    :param direction:
        up : 从下往上滑动
        down:从上往下滑动
        left: 从右往左滑动
        right:从左往右滑动
    :return:
    """
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    # 中心点
    center_x = width / 2
    center_y = height / 2
    # 中心点左边
    left_x = width / 4 * 1
    left_y = center_y
    # 中心点右边
    right_x = width / 4 * 3
    right_y = center_y
    # 中心点上边
    top_x = center_x
    top_y = height / 4 * 1
    # 中心点下边
    bottom_x = center_x
    bottom_y = height / 4 * 3
    # 判断滑动方向
    if direction == "up":
        driver.swipe(bottom_x, bottom_y, top_x, top_y)
    elif direction == "down":
        driver.swipe(top_x, top_y, bottom_x, bottom_y)
    elif direction == "left":
        driver.swipe(right_x, right_y, left_x, left_y)
    elif direction == "right":
        driver.swipe(left_x, left_y, right_x, right_y)
    else:
        raise Exception("请检查参数是否正确:up or down or left or right")


def find_element_with_scroll(loc, direction="up"):
    """
    边滑边找   某元素
    :param direction:
        up : 从下往上滑动
        down:从上往下滑动
        left: 从右往左滑动
        right:从左往右滑动
    :return:
    """
    page_source = ""
    while True:
        try:
            # driver.find_element_by_xpath("//*[@text='关于手机']").click()
            return driver.find_element(*loc)
        except Exception:
            scroll_page_one_time(direction)
            current_source = driver.page_source
            if current_source == page_source:
                print("到底了,没找到")
                break
            page_source = current_source


loc = By.XPATH, "//*[@text='关于手机']"
find_element_with_scroll(loc, direction="up").click()
# scroll_page_one_time()

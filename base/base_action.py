from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from base.base_driver import GetDriver


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=10, poll=1.0):
        # by = feature[0]
        # value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def base_find_elements(self, loc, timeout=10, poll=1.0):
        # by = feature[0]
        # value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        self.base_find_element(loc).send_keys(value)

    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 判断toast是否存在
    def base_is_toast_exist(self, msg):
        msg_xpath = By.XPATH, "//*[contains(@text,'%s')]" % msg
        try:
            self.base_find_element(msg_xpath, 5, 0.5)
            return True
        except Exception:
            return False

    # 判断 地址管理中 是否有地址
    def base_is_element_exist(self, loc):
        try:
            self.base_find_element(loc)
            return True
        except Exception:
            return False

    # 获取toast的值
    def base_get_toast_text(self, msg):
        """
        :param msg: 要查找的toast的部分内容
        :return:  查找到的toast的全部内容
        """
        msg_xpath = By.XPATH, "//*[contains(@text,'%s')]" % msg
        if self.base_is_toast_exist(msg):
            return self.base_get_text(msg_xpath)
        else:
            raise Exception("toast未出现，请检查")

    # 滑动一次
    def base_scroll_page_one_time(self, direction="up"):
        """
        滑动一次屏幕
        :param direction:
            up : 从下往上滑动
            down:从上往下滑动
            left: 从右往左滑动
            right:从左往右滑动
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
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
        top_y = height / 4 * 1 - 10
        # 中心点下边
        bottom_x = center_x
        bottom_y = height / 4 * 3 + 10
        # 判断滑动方向
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        else:
            raise Exception("请检查参数是否正确:up or down or left or right")

    # 边滑边找元素
    def base_find_element_with_scroll(self, loc, direction="up"):
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
                return self.base_find_element(loc, timeout=5, poll=1)
            except Exception:
                self.base_scroll_page_one_time(direction)
                current_source = self.driver.page_source
                if current_source == page_source:
                    print("到底了,没找到")
                    return None
                page_source = current_source

    # 点一次返回键
    def base_back_one_time(self):
        self.driver.press_keycode(4)

    def base_page_source_element_if_exist(self, element, timeout=10, poll=0.1):
        end_time = time.time() + timeout
        while True:
            if end_time < time.time():
                print("time out")
                return False
            if element in self.driver.page_source:
                print("succeed find element:", element)
                return True
            time.sleep(poll)


if __name__ == '__main__':
    base = BaseAction(GetDriver.init_driver(no_reset=False))
    # base.base_scroll_page_one_time()
    loc = By.XPATH, "//*[@text='关于手机']"
    base.base_find_element_with_scroll(loc, direction="up")

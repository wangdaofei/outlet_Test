import time

from appium import webdriver


class GetDriver:
    driver = None

    @classmethod
    def init_driver(cls, no_reset=True):
        if cls.driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            desired_caps['appPackage'] = 'com.yunmall.lc'
            desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
            # desired_caps['appPackage'] = 'com.android.settings'
            # desired_caps['appActivity'] = '.Settings'
            # 找toast
            desired_caps['automationName'] = 'Uiautomator2'

            # 每次启动是否重置应用
            desired_caps['no_reset'] = no_reset
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            time.sleep(1)
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    GetDriver().init_driver().quit()

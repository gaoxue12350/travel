from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page.hand_black import hand_black

class BasePage:
    black_list = [(By.XPATH, '//*[@text="知道了"]')]
    error_num=0
    max_num=3
    def __init__(self,driver:WebDriver=None):
        if driver==None:
            caps={}
            caps["platformName"]="android"
            caps["deviceName"]="test1"
            caps["appActivity"]=".homepage.LaunchActivity"
            caps["appPackage"]="com.tuniu.app.ui"
            caps["noReset"]="true"
            self.driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver=driver

    @hand_black
    def find(self,by,locator=None):
        if locator==None:
            result=self.driver.find_element(*by)
        else:
            result=self.driver.find_element(by,locator)
        return result

    def find_and_click(self,by,locator):
        return self.find(by,locator).click()

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                         .scrollable(true).instance(0))\
                                         .scrollIntoView(new UiSelector()\
                                         .text("{text}").instance(0));')

    def goto_main(self):
        from page.main_page.main import Main
        return Main(self.driver)


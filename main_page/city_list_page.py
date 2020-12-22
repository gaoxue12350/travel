"""
城市列表页
"""
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.main_page.main import Main


class CityListPage(BasePage):
    def input_city(self):
        #输入城市
        self.find(By.XPATH,'//*[@text="输入关键字/位置/品牌/酒店名"]').send_keys("南京")
        self.find_and_click(By.XPATH,'//*[@text="南京,江苏,中国"]')
        return Main(self.driver)

    def input_subway(self):
        #输入地铁
        self.find(By.XPATH,'//*[@text="输入关键字/位置/品牌/酒店名"]').send_keys("南京")
        self.find_and_click(By.XPATH,'//*[@text="南京南站,南京,江苏,中国"]')
        return Main(self.driver)

    def input_spot(self):
        #输入景点
        self.find(By.XPATH,'//*[@text="输入关键字/位置/品牌/酒店名"]').send_keys("南京")
        self.find_and_click(By.XPATH,'//*[@text="南京鼓楼,南京,江苏,中国"]')
        return Main(self.driver)

    def city_locate(self):
        #定位
        try:
            self.find(By.XPATH,'//*[contains(@text,"定位失败")]')
        except Exception as e:
            self.find_and_click(By.XPATH, "com.tuniu.app.ui:id/tv_address")
        return Main(self.driver)

    def common_used_city(self):
        #常用城市
        self.find_and_click(By.XPATH,'//android.widget.ListView/android.widget.LinearLayout[@index=1]//android.widget.TextView[@text="上海"]')
        return Main(self.driver)

    def hot_city(self):
        #热门城市
        self.find_and_click(By.XPATH,'//android.widget.ListView/android.widget.LinearLayout[@index=2]//android.widget.TextView[@text="三亚"]')
        return Main(self.driver)
"""
入离弹窗
"""
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.main_page.main import Main


class CheckInOutDate(BasePage):
    def one_night(self):
        #单晚
        self.find_and_click(By.ID,"com.tuniu.hotel:id/layout_choose_date")
        self.find_and_click(By.XPATH,"//*[@text='29']")
        self.find_and_click(By.XPATH,"//*[@text='30']")
        return Main(self.driver)

    def several_night(self):
        #多晚
        self.find_and_click(By.ID,"com.tuniu.hotel:id/layout_choose_date")
        self.find_and_click(By.XPATH,"//*[@text='28']")
        self.find_and_click(By.XPATH,"//*[@text='30']")
        return Main(self.driver)

    def cancel(self):
        #取消
        self.find_and_click(By.ID,"com.tuniu.hotel:id/layout_choose_date")
        self.find_and_click(By.XPATH,'//*[@text="取消"]')
        return Main(self.driver)

    def Montmorillonite_layer(self):
        #蒙层
        self.find_and_click(By.ID,"com.tuniu.hotel:id/layout_choose_date")
        self.find_and_click(By.ID, "com.tuniu.hotel:id/view_blank")
        return Main(self.driver)
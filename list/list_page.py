"""
列表页
"""
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.detail_page import DetailPage

class ListPage(BasePage):
    def goto_detail_page(self):
        "上海玩具总动员酒店"
        self.find_and_click(By.XPATH,"//*[contains(@text,'上海玩具总动员酒店')]")
        return DetailPage(self.driver)
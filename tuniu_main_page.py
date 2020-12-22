from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.main_page.main import Main

class TuniuMainPage(BasePage):
    def goto_main_Page(self):
        self.find_and_click(By.XPATH,'//*[@text="酒店"]')
        return Main(self.driver)
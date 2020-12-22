"""
首页
"""
#coding:utf-8
from selenium.webdriver.common.by import By
from page.main_page.banner_page import BannerPage
from page.main_page.club_memb import ClubMed
from page.main_page.collection_page import CollectionPage
from page.main_page.key_word_page import KeyWordPage
from page.main_page.map_page import MapPage
from page.main_page.order_page import OrderPage
from page.main_page.stars_level_page import StarsLevelPage
from page.base_page import BasePage
from page.list.list_page import ListPage


class Main(BasePage):

    def goto_return_page(self):
        #返回
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/iv_title_back_background"]')
        from page.tuniu_main_page import TuniuMainPage
        return TuniuMainPage(self.driver)

    def goto_banner_page(self):
        #进入banner页面
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/iv_product_detail_image"]')
        return BannerPage(self.driver)

    def goto_list_page(self):
        #查询
        self.find_and_click(By.XPATH,'//*[@text="查询"]')
        return ListPage(self.driver)

    def locate(self):
        #定位
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/iv_local"]')
        return self.find(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/tv_destination"]').text

    def goto_cityListPage(self):
        #进入城市列表页
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/ll_destination"]')
        from page.main_page.city_list_page import CityListPage
        return CityListPage(self.driver)

    def goto_check_in_out_date(self):
        #进入入离日期
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/rl_check_in_area"]')
        from page.main_page.check_in_out_date_page import CheckInOutDate
        return CheckInOutDate(self.driver)

    def goto_key_word(self):
        #进入关键词页面
        self.find_and_click(By.XPATH,'//*[@text="搜索酒店名/地名/关键字"]')
        return KeyWordPage(self.driver)

    def goto_stars_level_page(self):
        #进入星级弹窗
        self.find_and_click(By.XPATH,'//*[@text="设置喜欢的酒店档次/价格"]')
        return StarsLevelPage(self.driver)

    def goto_map_page(self):
        #进入地图页面
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/iv_map_query"]')
        return MapPage(self.driver)

    def goto_collection_page(self):
        #进入我的收藏页面
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/rl_my_collection"]')
        return CollectionPage(self.driver)

    def goto_order_page(self):
        #进入我的订单页面
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/rl_my_order"]')
        return OrderPage(self.driver)

    def goto_club_member_page(self):
        #进入ClubMed页面
        self.find_and_click(By.XPATH,'//*[@resource-id="com.tuniu.hotel:id/rl_flag_ship_one"]')
        return ClubMed(self.driver)
import time
from selenium import webdriver
import unittest
from Amazon.SignInPage import SignInPageClass
from Amazon.AmazonMainPage import AmazonMainPageClass
from Amazon.CartSection import CartSectionPageClass


class AmazonTestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.SignInPage = SignInPageClass(self.driver)
        self.AmazonMainPage = AmazonMainPageClass(self.driver)
        self.CartSection = CartSectionPageClass(self.driver)

    def test_amazon_TC(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        time.sleep(3)
        self.SignInPage.fill_login_field("barkhudaryanrosa@gmail.com")
        time.sleep(3)
        self.SignInPage.press_continue_button()
        time.sleep(3)
        self.SignInPage.fill_password_field("Barkhudaryan1")
        time.sleep(3)
        self.SignInPage.put_remember_me_tick()
        time.sleep(3)
        self.SignInPage.press_signin_button()
        time.sleep(3)

        self.AmazonMainPage.press_cart_section()
        time.sleep(3)
        self.CartSection.press_first_item_delete_button()
        time.sleep(3)
        self.CartSection.delete_all_items_from_cart()
        time.sleep(3)

        self.AmazonMainPage.press_homepage_button()
        time.sleep(3)
        self.AmazonMainPage.fill_search_field("LS2 Helmets")
        time.sleep(3)
        self.AmazonMainPage.press_search_button()
        time.sleep(3)
        self.AmazonMainPage.scroll_down()
        time.sleep(3)
        self.AmazonMainPage.open_second_photo()
        time.sleep(3)
        self.AmazonMainPage.click_add_to_cart_Buttton()

    def tearDown(self):
        time.sleep(4)
        self.driver.close()



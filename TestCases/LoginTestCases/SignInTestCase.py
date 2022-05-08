import time
import unittest
from selenium import webdriver
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.MainPage.MainPage import MainPageClass
from Pages.CartSection.CartSection import CartPageClass
from Pages.SearchResultsPage.SearchResultsPage import SearchPageClass
from Pages.ItemDetailPage.ItemDetailPage import ItemDetailPageClass
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.SignInPage.PasswordPage import PasswordPageClass
import pathlib
from Common.Setup.SetupFile import SetupClass


class AmazonTestClass(unittest.TestCase, SetupClass):
    def setUp(self):
        self.setup_general()
        self.LoginPage = LoginPageClass(self.driver)
        self.PasswordPage = PasswordPageClass(self.driver)
        self.AmazonMainPage = MainPageClass(self.driver)
        self.CartSection = CartPageClass(self.driver)
        self.SearchPage = SearchPageClass(self.driver)
        self.ItemDetailPage = ItemDetailPageClass(self.driver)


    def test_sign_in_TC(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.LoginPage.fill_login_field("barkhudaryanrosa@gmail.com")
        self.LoginPage.press_continue_button()
        self.PasswordPage.fill_password_field("Barkhudaryan1")
        self.PasswordPage.check_remember_me_checkbox()
        self.PasswordPage.press_sign_in_button()

        self.AmazonMainPage.press_cart_button()
        self.CartSection.press_first_item_delete_button()
        self.CartSection.delete_all_items_from_cart()

        self.AmazonMainPage.press_home_button()
        self.AmazonMainPage.fill_search_field("LS2 Helmets")
        self.AmazonMainPage.press_search_button()
        self.SearchPage.scroll_down_1500_pixels()  #todo try, move to open product function
        self.SearchPage.click_on_second_product()
        self.ItemDetailPage.click_add_to_cart_button()

    def tearDown(self):
        self.driver.close()


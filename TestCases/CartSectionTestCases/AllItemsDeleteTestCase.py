import time
import unittest
from Common.Documentations.DataUsed import *
from Pages.MainPage.MainPage import MainPageClass
from Pages.CartSection.CartSection import CartPageClass
from Pages.SearchResultsPage.SearchResultsPage import SearchPageClass
from Pages.ItemDetailPage.ItemDetailPage import ItemDetailPageClass
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.SignInPage.PasswordPage import PasswordPageClass
from Common.Setup.SetupFile import SetupClass


class ItemSearchTestClass(unittest.TestCase, SetupClass):
    def setUp(self):
        self.setup_general()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.amazonMainPage = MainPageClass(self.driver)
        self.cartSection = CartPageClass(self.driver)
        self.searchPage = SearchPageClass(self.driver)
        self.itemDetailPage = ItemDetailPageClass(self.driver)
        self.LoginPage = LoginPageClass(self.driver)
        self.PasswordPage = PasswordPageClass(self.driver)

    def test_item_search_TC(self):
        self.driver.get(amazonSignInPageUrl)
        self.loginPage.fill_login_field(loginNameValidInput)
        self.loginPage.press_continue_button()
        self.passwordPage.fill_password_field(passwordValidInput)
        self.passwordPage.check_remember_me_checkbox()
        self.passwordPage.press_sign_in_button()
        self.amazonMainPage.press_cart_button()
        self.cartSection.delete_all_items_from_cart()
        self.amazonMainPage.press_log_out_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


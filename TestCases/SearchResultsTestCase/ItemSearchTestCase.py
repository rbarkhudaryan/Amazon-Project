import time
import unittest
from Common.Documentations.Variables import *
from Pages.MainPage.MainPage import MainPageClass
from Pages.CartSection.CartSection import CartPageClass
from Pages.SearchResultsPage.SearchResultsPage import SearchPageClass
from Pages.ItemDetailPage.ItemDetailPage import ItemDetailPageClass
from Pages.SignInPage.LoginPage import LoginPageClass
from Pages.SignInPage.PasswordPage import PasswordPageClass
from Common.SetUp.SetUpFile import SetUpClass


class ItemSearchTestClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.setup_general()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.amazonMainPage = MainPageClass(self.driver)
        self.cartSection = CartPageClass(self.driver)
        self.searchPage = SearchPageClass(self.driver)
        self.itemDetailPage = ItemDetailPageClass(self.driver)


    def test_item_search_TC(self):
        self.driver.get(amazonSignInPageUrl)
        self.loginPage.fill_login_field(loginNameValidInput)
        self.loginPage.press_continue_button()
        self.passwordPage.fill_password_field(passwordValidInput)
        self.passwordPage.check_remember_me_checkbox()
        self.passwordPage.press_sign_in_button()
        self.amazonMainPage.press_home_button()
        self.amazonMainPage.fill_search_field(searchInput)
        self.amazonMainPage.press_search_button()
        self.searchPage.click_on_second_product()
        self.itemDetailPage.click_add_to_cart_button()
        self.amazonMainPage.press_log_out_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()







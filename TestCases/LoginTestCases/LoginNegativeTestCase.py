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


class NegativeLogInTestClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.setup_general()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.amazonMainPage = MainPageClass(self.driver)
        self.cartSection = CartPageClass(self.driver)
        self.searchPage = SearchPageClass(self.driver)
        self.itemDetailPage = ItemDetailPageClass(self.driver)

    def test_negative_log_in_TC(self):
        self.driver.get(amazonSignInPageUrl)
        self.loginPage.fill_login_field(loginNameInvalidInput)
        self.loginPage.press_continue_button()
        self.assertEqual(self.loginPage.validate_login_page_invalid_functionality().text, "We cannot find an account with that email address", "Error")

    def tearDown(self):
        time.sleep(2)
        self.driver.close()



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


class SignInTestClass(unittest.TestCase, SetupClass):
    def setUp(self):
        self.setup_general()
        self.loginPage = LoginPageClass(self.driver)
        self.passwordPage = PasswordPageClass(self.driver)
        self.amazonMainPage = MainPageClass(self.driver)
        self.cartSection = CartPageClass(self.driver)
        self.searchPage = SearchPageClass(self.driver)
        self.itemDetailPage = ItemDetailPageClass(self.driver)

    def test_sign_in_TC(self):
        self.driver.get(amazonSignInPageUrl)
        self.loginPage.fill_login_field(loginNameValidInput)
        self.loginPage.press_continue_button()
        self.passwordPage.fill_password_field(passwordInvalidInput)
        self.passwordPage.check_remember_me_checkbox()
        self.passwordPage.press_sign_in_button()
        self.assertEqual(self.passwordPage.validate_password_page_invalid_functionality().text, "Your password is incorrect", "Error")

    def tearDown(self):
        time.sleep(2)
        self.driver.close()



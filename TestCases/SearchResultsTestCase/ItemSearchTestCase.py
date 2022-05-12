import time
import unittest
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


    def test_item_search_TC(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.loginPage.fill_login_field("barkhudaryanrosa@gmail.com")
        self.loginPage.press_continue_button()
        self.passwordPage.fill_password_field("Barkhudaryan1")
        self.passwordPage.check_remember_me_checkbox()
        self.passwordPage.press_sign_in_button()
        self.amazonMainPage.press_home_button()
        self.amazonMainPage.fill_search_field("Cardo SPPT0002")
        self.amazonMainPage.press_search_button()
        self.searchPage.click_on_second_product()
        self.itemDetailPage.click_add_to_cart_button()
        self.amazonMainPage.press_log_out_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()







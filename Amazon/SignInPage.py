from Locators.LocatorsAmazon import *

class SignInPageClass():
    def __init__(self, driver):
        self.driver = driver

    def fill_login_field(self, text):
        loginField = self.driver.find_element(*SignInPageLoginFieldLocator)
        loginField.send_keys(text)

    def press_continue_button(self):
        continueButton = self.driver.find_element(*SignInPageContinueButtonLocator)
        continueButton.click()

    def fill_password_field(self, text):
        passwordField = self.driver.find_element(*SignInPagePasswordFieldLocator)
        passwordField.send_keys(text)

    def put_remember_me_tick(self):
        rememberMeTick = self.driver.find_element(*SignInPageRememberMeTick)
        rememberMeTick.click()

    def press_signin_button(self):
        signInButton = self.driver.find_element(*SignInPageSignInButtonLocator)
        signInButton.click()
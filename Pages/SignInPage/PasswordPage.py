from Locators.Locators import *
from Common.CustomFind import FindElement


class PasswordPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def fill_password_field(self, text):
        passwordField = self.findElement.find(*signInPagePasswordFieldLocator)
        passwordField.send_keys(text)

    def check_remember_me_checkbox(self):
        rememberMeTick = self.findElement.find(*signInPageRememberMeTick)
        rememberMeTick.click()

    def press_sign_in_button(self):
        signInButton = self.findElement.find(*signInPageSignInButtonLocator)
        signInButton.click()
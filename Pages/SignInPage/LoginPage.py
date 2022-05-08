from Locators.Locators import *
from Common.CustomFind import FindElement


class LoginPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def fill_login_field(self, text):
        loginField = self.findElement.find(*signInPageLoginFieldLocator)
        loginField.clear()
        loginField.send_keys(text)

    def press_continue_button(self):
        continueButton = self.findElement.find(*signInPageContinueButtonLocator)
        continueButton.click()

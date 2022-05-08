from Locators.Locators import *
from Common.CustomFind import FindElement


class MainPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_cart_button(self):
        cartButton = self.driver.find_element(*mainPageCartButtonLocator)
        cartButton.click()

    def press_home_button(self):
        homePageButton = self.findElement.find(*homeButtonLocator)
        homePageButton.click()

    def fill_search_field(self, text):
        searchField = self.findElement.find(*mainPageSearchFieldLocator)
        searchField.clear()
        searchField.send_keys(text)

    def press_search_button(self):
        searchButton = self.findElement.find(*searchButtonLocator)
        searchButton.click()

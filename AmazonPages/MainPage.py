from Locators.LocatorsAmazon import *

class AmazonMainPageClass():
    def __init__(self, driver):
        self.driver = driver

    def press_cart_section(self):
        cartSection = self.driver.find_element(*MainPageCartSectionButtonLocator)
        cartSection.click()

    def press_homepage_button(self):
        homePageButton = self.driver.find_element(*AmazonHomePageLocator)
        homePageButton.click()

    def fill_search_field(self, text):
        searchField = self.driver.find_element(*MainPageSearchFieldLocator)
        searchField.clear()
        searchField.send_keys(text)

    def press_search_button(self):
        searchButton = self.driver.find_element(*SearchButtonLocator)
        searchButton.click()




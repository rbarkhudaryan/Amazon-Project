from Locators.LocatorsAmazon import *
import time

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

    def scroll_down(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1500)")

    def open_second_photo(self):
        SecondPhotoButton = self.driver.find_element(*SecondItemLocator)
        SecondPhotoButton.click()

    def click_add_to_cart_Buttton(self):
        AddToCartButton = self.driver.find_element(*AddToCartButtonLocator)
        AddToCartButton.click()



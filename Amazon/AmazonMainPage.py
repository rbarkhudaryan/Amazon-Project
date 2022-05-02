from Locators.LocatorsAmazon import *

class AmazonMainPageClass():
    def __init__(self, driver):
        self.driver = driver

    def press_cart_section(self):
        cartSection = self.driver.find_element(*MainPageCartSectionButtonLocator)
        cartSection.click()
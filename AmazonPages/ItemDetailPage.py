from Locators.LocatorsAmazon import *

class ItemDetailPageClass():
    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart_Button(self):
        AddToCartButton = self.driver.find_element(*AddToCartButtonLocator)
        AddToCartButton.click()

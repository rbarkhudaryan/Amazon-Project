from Locators.Locators import *
from Common.CustomFind import FindElement

class ItemDetailPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def click_add_to_cart_button(self):
        addToCartButton = self.findElement.find(*addToCartButtonLocator)
        addToCartButton.click()

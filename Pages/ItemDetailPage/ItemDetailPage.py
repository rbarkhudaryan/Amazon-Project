import time
from Locators.Locators import addToCartButtonLocator
from Common.CustomFind.FindElement import FindElement

class ItemDetailPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def click_add_to_cart_button(self):
        addToCartButton = self.findElement.find(*addToCartButtonLocator)
        addToCartButton.click()


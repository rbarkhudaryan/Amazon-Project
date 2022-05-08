import time
from Locators.Locators import *
from Common.CustomFind import FindElement

class CartPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_first_item_delete_button(self):
            firstItemDeleteButton = self.findElement.find(*cartSectionDeleteButtonLocator)
            firstItemDeleteButton.click()

    def delete_all_items_from_cart(self):
            cartItemsCount = self.findElement.find(*mainPageCartButtonLocator)
            numberCartItemsCount = int(cartItemsCount.text)
            try:
                while numberCartItemsCount > 0:
                    deleteItemsButton = self.findElement.find(*cartSectionDeleteButtonLocator)
                    deleteItemsButton.click()
                    numberCartItemsCount -= 1
                    time.sleep(1)
            except:
                pass















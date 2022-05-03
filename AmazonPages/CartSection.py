import time
from Locators.LocatorsAmazon import *

class CartSectionPageClass():
    def __init__(self, driver):
        self.driver = driver

    def press_first_item_delete_button(self):
        try:
            firstItemDeleteButton = self.driver.find_element(*CartSectionDeleteButtonLocator)
            firstItemDeleteButton.click()
        except:
            pass

    def delete_all_items_from_cart(self):
            cartItemsCount = self.driver.find_element(*MainPageCartSectionButtonLocator)
            numberCartItemsCount = int(cartItemsCount.text)
            try:
                while numberCartItemsCount > 0:
                    deleteItemsButton = self.driver.find_element(*CartSectionDeleteButtonLocatorAll)
                    deleteItemsButton.click()
                    numberCartItemsCount -= 1
                    time.sleep(2)
            except:
                pass















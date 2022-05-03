from Locators.LocatorsAmazon import *
import time

class AmazonSearchPageClass():
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1500)")

    def open_second_photo(self):
        SecondPhotoButton = self.driver.find_element(*SecondItemLocator)
        SecondPhotoButton.click()




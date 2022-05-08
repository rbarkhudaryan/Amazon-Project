from Locators.Locators import *
from Common.CustomFind import FindElement


class SearchPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def scroll_down_1500_pixels(self):
        self.driver.execute_script("window.scrollTo(0, 1500)")

    def click_on_second_product(self):
        SecondPhotoButton = self.findElement.find(*secondProductLocator)
        SecondPhotoButton.click()




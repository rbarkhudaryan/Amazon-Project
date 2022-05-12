from Locators.Locators import secondProductLocator
from Common.CustomFind.FindElement import FindElement


class SearchPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def click_on_second_product(self):
        self.driver.execute_script("window.scrollTo(0, 1500)")
        secondProductButton = self.findElement.find(*secondProductLocator)
        secondProductButton.click()





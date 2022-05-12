from Locators.Locators import mainPageCartButtonLocator, homeButtonLocator, mainPageSearchFieldLocator, searchButtonLocator, mainPageAccountsListsButtonLocator, mainPageLogOutButtonLocator
from Common.CustomFind.FindElement import FindElement
from selenium.webdriver.common.action_chains import ActionChains

class MainPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_cart_button(self):
        cartButton = self.driver.find_element(*mainPageCartButtonLocator)
        cartButton.click()

    def press_home_button(self):
        homePageButton = self.findElement.find(*homeButtonLocator)
        homePageButton.click()

    def fill_search_field(self, text):
        searchField = self.findElement.find(*mainPageSearchFieldLocator)
        searchField.clear()
        searchField.send_keys(text)

    def press_search_button(self):
        searchButton = self.findElement.find(*searchButtonLocator)
        searchButton.click()

    def press_log_out_button(self):
        element_to_hover_over = self.findElement.find(*mainPageAccountsListsButtonLocator)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        logOutButton = self.findElement.find(*mainPageLogOutButtonLocator)
        logOutButton.click()

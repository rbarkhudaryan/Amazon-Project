from selenium import webdriver


class SetupClass():
    def setup_general(self):
        self.driver = webdriver.Chrome("../../Common/Drivers/chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
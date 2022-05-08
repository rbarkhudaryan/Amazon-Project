from selenium import webdriver
import pathlib

class SetupClass():
    def setup_general(self):
        self.driver = webdriver.Chrome(executable_path=str(pathlib.Path().absolute().parent.joinpath('Common').joinpath('Drivers').joinpath('chromedriver.exe')))
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
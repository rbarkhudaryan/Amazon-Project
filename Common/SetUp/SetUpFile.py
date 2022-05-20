from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SetUpClass():
    def setup_general(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
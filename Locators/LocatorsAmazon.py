from selenium.webdriver.common.by import By

#Sign in Page
SignInPageLoginFieldLocator = (By.ID, "ap_email")
SignInPageContinueButtonLocator = (By.ID, "continue")
SignInPagePasswordFieldLocator = (By.ID, "ap_password")
SignInPageRememberMeTick = (By.NAME, "rememberMe")
SignInPageSignInButtonLocator = (By.ID, "signInSubmit")

#Main page
MainPageCartSectionButtonLocator = (By.ID, "nav-cart-count")

#Card Section
CartSectionDeleteButtonLocator = (By.XPATH, "(//input[@value ='Delete'])[1]")
CartSectionDeleteButtonLocatorAll = (By.XPATH, "//input[@value='Delete']")

#MainPage
AmazonHomePageLocator = (By.ID, "nav-logo-sprites")
MainPageSearchFieldLocator = (By.ID, "twotabsearchtextbox")
SearchButtonLocator = (By.ID, "nav-search-submit-button")
SecondItemLocator = (By.XPATH, "(//img[@class ='s-image'])[2]")
AddToCartButtonLocator = (By.ID, "add-to-cart-button")

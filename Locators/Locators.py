from selenium.webdriver.common.by import By

# Signin Page
signInPageLoginFieldLocator = (By.ID, "ap_email")
signInPageContinueButtonLocator = (By.ID, "continue")
signInPagePasswordFieldLocator = (By.ID, "ap_password")
signInPageRememberMeTick = (By.NAME, "rememberMe")
signInPageSignInButtonLocator = (By.ID, "signInSubmit")

# Main page
mainPageCartButtonLocator = (By.ID, "nav-cart-count")

# Cart Section
cartSectionDeleteButtonLocator = (By.XPATH, "(//input[@value ='Delete'])[1]")

# MainPage
homeButtonLocator = (By.ID, "nav-logo-sprites")
mainPageSearchFieldLocator = (By.ID, "twotabsearchtextbox")

# SearchPage
searchButtonLocator = (By.ID, "nav-search-submit-button")
secondProductLocator = (By.XPATH, "(//img[@class ='s-image'])[2]")

# ProductDetailPage
addToCartButtonLocator = (By.ID, "add-to-cart-button")

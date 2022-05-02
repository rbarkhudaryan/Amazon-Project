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
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK= (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_link")
    REGISTRATION_FORM=(By.CSS_SELECTOR, "#login_link")
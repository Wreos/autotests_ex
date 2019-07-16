from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK= (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_link")
    REGISTRATION_FORM=(By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    ADD_TO_BASKET=(By.CSS_SELECTOR, '.btn-lg.btn-primary.btn-add-to-basket')
    PRICE=(By.CSS_SELECTOR, '.alertiner')
    MESSAGE=(By.CSS_SELECTOR, '.btn-lg.btn-primary.btn-add-to-basket')
    PRICE_NOM=(By.CSS_SELECTOR, '.price_color')
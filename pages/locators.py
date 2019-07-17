from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK= (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_link")
    REGISTRATION_FORM=(By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    ADD_TO_BASKET=(By.CSS_SELECTOR, '.btn-lg.btn-primary.btn-add-to-basket')
    MESSAGEAFTERADD=(By.XPATH, "//*[contains(text(), 'Был добавлен в корзину')]")
    NAMEBOOKCART=(By.CSS_SELECTOR, '.alert:nth-child(1)>.alertinner strong')
    NAMEBOOK=(By.CSS_SELECTOR, '.col-sm-6 h1')
    MESSAGE_CART = (By.XPATH, "//*[contains(.,'составляет')]")
    PRICE=(By.CSS_SELECTOR, '.alert:nth-child(3) .alertinner strong')
    PRICE_NOM=(By.CSS_SELECTOR, '.col-sm-6 .price_color')
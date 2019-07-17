from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK= (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_link")
    REGISTRATION_FORM=(By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    ADD_TO_BASKET=(By.CSS_SELECTOR, '.btn-lg.btn-primary.btn-add-to-basket')
    MESSAGEAFTERADD=(By.CSS_SELECTOR, 'был добавлен в вашу корзину')
    NAMEBOOK=(By.CSS_SELECTOR, '.alert:nth-child(1)>.alertinner>strong')
    MESSAGE_CART = (By.PARTIAL_LINK_TEXT, 'Стоимость корзины теперь составляет')
    PRICE=(By.CSS_SELECTOR, '.alert:nth-child(3) .alertinner strong')
    PRICE_NOM=(By.CSS_SELECTOR, '.col-sm-6 .price_color')
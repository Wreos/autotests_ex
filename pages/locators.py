from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    EMPTYBASKETMESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators(object):
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-lg.btn-primary.btn-add-to-basket')
    MESSAGEAFTERADD = (By.CSS_SELECTOR, 'div.alertinner')
    NAMEBOOKCART = (By.CSS_SELECTOR, '.alert:nth-child(1)>.alertinner strong')
    NAMEBOOK = (By.CSS_SELECTOR, '.col-sm-6 h1')
    MESSAGE_CART = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRICE = (By.CSS_SELECTOR, '.alert:nth-child(3) .alertinner strong')
    PRICE_NOM = (By.CSS_SELECTOR, '.col-sm-6 .price_color')

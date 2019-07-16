from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        # реализуйте проверку на корректный url адрес
        linkcart=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET), "Basket is not found"
        linkcart.click()


from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        # реализуйте проверку на корректный url адрес
        linkcart=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        linkcart.click()

    def compare_message(self):
        message_cart=self.browser.find_element(*ProductPageLocators.MESSAGE_CART).text
        print(message_cart)
        #assert self.is_element_present(*ProductPageLocators.MESSAGE_CART), "Нет сообщения об добавлении товара"
        bookname = self.browser.find_element(*ProductPageLocators.NAMEBOOK).text
        print(bookname)
        booknamecart = self.browser.find_element(*ProductPageLocators.NAMEBOOKCART).text
        print(booknamecart)
        assert bookname==booknamecart

    def check_sum(self):
        price_nom=self.browser.find_element(*ProductPageLocators.PRICE_NOM).text
        price_cart=self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price_cart==price_nom



from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        # реализуйте проверку на корректный url адрес
        linkcart=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        linkcart.click()

    def compare_message(self):

        assert self.is_element_present(*ProductPageLocators.MESSAGE_CART), "Нет сообщения об добавлении товара"
        messageadding= self.browser.find_element(*ProductPageLocators.MESSAGEAFTERADD).text

        p="Coders at Work был добавлен в вашу корзину."
        assert p == messageadding, "Текст сообщения не соответствует эталонному"
        bookname = self.browser.find_element(*ProductPageLocators.NAMEBOOK).text
        booknamecart = self.browser.find_element(*ProductPageLocators.NAMEBOOKCART).text
        assert bookname==booknamecart

    def check_sum(self):
        price_nom=self.browser.find_element(*ProductPageLocators.PRICE_NOM).text
        price_cart=self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price_cart==price_nom, "Суммы не совпадают"



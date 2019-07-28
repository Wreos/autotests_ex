from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators


class CartPage(BasePage):

    def checkbasket(self):
        emptybasketmessage =self.browser.find_element(*MainPageLocators.EMPTYBASKETMESSAGE).text
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEM)
        print(emptybasketmessage)
        assert "Your basket is empty" in emptybasketmessage, "Нет сообщения об пустой корзине"
from .pages.main_page import MainPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
import time
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):

    def test_geust_should_see_login_link(self, browser):


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.checkbasket()
    time.sleep(5)

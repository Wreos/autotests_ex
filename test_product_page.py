from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time


def test_add_to_card(browser):

    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(50)


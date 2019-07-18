from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                 ])

def test_add_to_card(browser, link):

    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.compare_message()
    page.check_sum()



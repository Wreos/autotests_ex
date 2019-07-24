from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage(object):
    def __init__(self,browser,url, timeout=10):
        self.browser=browser
        self.url=url
        self.browser.implicitly_wait(timeout)

#метод открытия ссылки
    def open(self):
        self.browser.get(self.url)

#проверка того, что элемент представлен
    def is_element_present(self, how,what):
        try:
            self.browser.find_element(how,what)
        except NoSuchElementException:
            return False
        return True

# метод для определения что элемент не представлен
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

#метод для определения того, что элемент исчезнет
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

#метод для поиска страницы логина
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

# решение математической задачи
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 15).until(EC.alert_is_present())
        alert=self.browser.switch_to.alert
        x=alert.text.split(" ")[2]
        answer = str(math.log(abs((12*math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert=self.browser.switch_to.alert
            print("Your code:{}".format(alert.text))

            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


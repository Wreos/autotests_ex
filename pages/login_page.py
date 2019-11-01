from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in str(self.current_url)

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login link is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration link is not presented"

    def register_new_user(self,email,password):
        registration_link=self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        registration_link.click()
        email=str(time.time())+"@fakeemail.org"
        password="pahan"
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD).sendkeys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD).sendkeys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORDCONFIRM_FIELD).sendkeys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
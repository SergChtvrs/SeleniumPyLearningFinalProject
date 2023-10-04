from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url
        if "login" in get_url:
            assert True
        else:
            assert False, "the url does not contain 'login'"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), " login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM), "register form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        input_email.send_keys(email)
        input_pass = self.browser.find_element(*LoginPageLocators.REG_PASS)
        input_pass.send_keys(password)
        input_confirm_pass = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASS)
        input_confirm_pass.send_keys(password)
        registr_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        registr_button.click()
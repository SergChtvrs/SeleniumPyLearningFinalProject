from .base_page import BasePage
from .locators import LoginPageLocators


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
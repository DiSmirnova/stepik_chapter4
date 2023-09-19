from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_url.click()
        assert ("login" in self.browser.current_url), "There is not login url"

    def should_be_login_form(self):
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_url.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_url.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no register form"

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket_with_alert_check(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
        BasePage.solve_quiz_and_get_code(self)

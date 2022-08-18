from pages.base_page import Page
from selenium.webdriver.common.by import By


class ShoppingCartPage(Page):
    CART_EMPTY_LABEL = (By.CSS_SELECTOR, 'h2')
    PRODUCT_IN_CART = (By.CSS_SELECTOR, 'span.a-truncate-cut')

    def verify_shopping_cart_empty_text_present(self):
        expected_text = 'Your Amazon Cart is empty'
        actual_text = self.driver.find_element(*self.CART_EMPTY_LABEL).text
        assert expected_text == actual_text, f'Expected {expected_text} but turned {actual_text}'

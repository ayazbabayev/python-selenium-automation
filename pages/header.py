from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURNS_ORDERS = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')
    COUNT_OF_ELEMENTS = (By.ID, 'nav-cart-count')

    def search_product(self, search_word):
        self.input_text(search_word, *self.INPUT_FIELD)
        self.click(*self.SEARCH_ICON)

    def returns_and_orders(self):
        self.click(*self.RETURNS_ORDERS)
        # Alternative(Sv): self.find_element(*self.RETURNS_ORDERS).click()

    def cart_icon(self):
        self.click(*self.CART_ICON)

    def verify_cart_has_element(self, expected_number_of_elements):
        actual_no_of_elements = self.find_element(*self.COUNT_OF_ELEMENTS).text
        assert expected_number_of_elements == actual_no_of_elements,\
            f'Error: expected {expected_number_of_elements} but got {actual_no_of_elements}'

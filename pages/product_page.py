from selenium.webdriver.common.by import By
from pages.base_page import Page
# from selenium.webdriver.support import expected_conditions as EC


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    def add_into_cart(self):
        # self.click(*self.ADD_TO_CART_BTN)
        # self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)


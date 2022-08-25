from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    NEW_ARRIVALS_TAB = (By.CSS_SELECTOR, "[href*='New-Arrivals']")
    # Alternative (Label text): (By.XPATH, "//span[contains(text(),'New Arrivals')]"
    NEWARR_SUBTABS = (By.CSS_SELECTOR, "a.mm-merch-panel[href*='na']")


    def add_into_cart(self):
        # self.click(*self.ADD_TO_CART_BTN)
        # self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS_TAB)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_new_arrivals_deals(self, expected_deals_count):
        expected_deals_count = int(expected_deals_count)
        actual_deals_count = len(self.find_elements(*self.NEWARR_SUBTABS))
        assert expected_deals_count == actual_deals_count,\
            f'Error: expected {expected_deals_count} but got {actual_deals_count}'


  # def five_links_verification(context, expected_count):
#     expected_count = int(expected_count)
#     five_links_count = len(context.driver.find_elements(*five_links))
#     assert five_links_count == expected_count, f'Expected {expected_count} but turned {five_links_count}'

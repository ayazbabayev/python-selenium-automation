from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURNS_ORDERS = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')
    COUNT_OF_ELEMENTS = (By.ID, 'nav-cart-count')
    SELECTED_FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    SPANISH_FLAG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')

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

    def hover_over_lang_options(self):
        selected_flag = self.find_element(*self.SELECTED_FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(selected_flag)
        actions.perform()

    def select_dept(self, alias):
        department = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department)
        select.select_by_value(f'search-alias={alias}')

    def verify_esp_option_present(self):
        self.wait_for_element_appear(*self.SPANISH_FLAG)
        # Below is my contribution, extending with clicking via action chains.
        esp_flag = self.find_element(*self.SPANISH_FLAG)
        actions = ActionChains(self.driver)
        actions.click(esp_flag)
        actions.perform()

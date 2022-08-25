from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT = (By.CSS_SELECTOR, 'img.s-image')
    NAV_SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{SUB_STRING}']")

    def get_subnav_locator(self, category):
        return [self.NAV_SUBNAV[0], self.NAV_SUBNAV[1].replace('{SUB_STRING}', category)]

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT)

    def select_product(self):
        self.click(*self.PRODUCT)
        # self.wait_for_element_click(*self.PRODUCT)

    def verify_dept_is_selected(self, category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)

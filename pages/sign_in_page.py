from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN_LABEL = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    # EMAIL_BAR = (By.ID, 'ap_email')

    def verify_sign_in_page_opened(self):
        text_expected = 'Sign in'
        text_actual = self.driver.find_element(*self.SIGN_IN_LABEL).text
        assert text_expected == text_actual, f'Expected {text_expected} but turned {text_actual}'
        # assert self.find_element(*s
        # elf.EMAIL_BAR).is_displayed()

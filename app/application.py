from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage               # < a
from pages.shopping_cart_page import ShoppingCartPage   # < b
from pages.product_page import ProductPage              # < c


class Application:
    # (7) CONNECTING PAGE OBJECTS TO APPLICATION:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)                 # < a
        self.shopping_cart_page = ShoppingCartPage(self.driver)     # < b
        self.product_page = ProductPage(self.driver)                # < c

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

searched_product = (By.CSS_SELECTOR, "#twotabsearchtextbox")
selected_product = (By.CSS_SELECTOR, "img[alt*='First Coffee. Yemen Medium Roast (whole bean)']")


@when('User searches for {search_word}')
def user_searches_product(context, search_word):
    context.driver.find_element(*searched_product).send_keys(search_word)
    context.driver.find_element(*searched_product).send_keys(Keys.RETURN)


@when('User selects the product')
def user_selects_product(context):
    context.driver.find_element(*selected_product).click()


@when('User adds product into cart')
def user_adds_product_into_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()


@when('User clicks Amazon cart icon')
def user_clicks_amazon_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart').click()


@then('Cart shows {search_word} in the cart')
def verifying_product_in_the_cart(context, search_word):
    expected_word = context.driver.find_element(By.CSS_SELECTOR, "span.a-truncate-cut").text
    assert expected_word == search_word, f'expected and search word results not matching.'

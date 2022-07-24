from selenium.webdriver.common.by import By
from behave import given, when, then

five_links = (By.CSS_SELECTOR, "#zg_header a")


@when('User clicks on Bestsellers page')
def user_clicks_bestsellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a.nav-a[href*='bestseller']").click()


@then('Verify that {expected_count} links are present')
def five_links_verification(context, expected_count):
    expected_count = int(expected_count)
    five_links_count = len(context.driver.find_elements(*five_links))
    assert five_links_count == expected_count, f'Expected {expected_count} but turned {five_links_count}'

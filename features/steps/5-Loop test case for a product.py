from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'span.selection')


@given('Amazon page for product {product_id}')
def page_for_productid(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click shown colors')
def user_can_click_shown_colors(context):
    expected_colors = ['Fresh Green', 'Green Stripe', 'Navy Blue', 'Orange', 'Violet', 'Yellow', 'Olive Green', 'Black', 'Red', 'Dark Blue', 'Fern Green', 'Lavender']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    actual_colors = []

    for color in colors:
        color.click()
        actual_colors += [context.driver.find_element(*SELECTED_COLOR).text]
        print('Actual colors', actual_colors)

    assert expected_colors == actual_colors, '\n'f'EXPECTED: {expected_colors} \n do not match with \n  ACTUAL: {actual_colors}'

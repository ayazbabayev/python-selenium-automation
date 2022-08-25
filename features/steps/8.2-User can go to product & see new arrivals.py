from behave import given, when, then


@given('User goes to product {target_product} on amazon')
def user_goes_to_product_page(context, target_product):
    page = 'https://www.amazon.com/gp/product/'
    context.driver.get(page+target_product)


@when('Hovers over new arrivals')
def hover_over_new_arrivals(context):
    context.app.product_page.hover_over_new_arrivals()


@then('Verify that user sees {number} deals in new arrivals tab')
def verify_new_arrivals_deals(context, number):
    context.app.product_page.verify_new_arrivals_deals(number)

from behave import given, when, then
# 1- 1st scenario


@given('open amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('click amazon orders link')
def click_amazon_orders(context):
    context.app.header.returns_and_orders()
    # Alternative(Sv): context.app.header.click_orders()


@then('verify sign in page is opened')
def verify_sign_in_page_opened(context):
    context.app.sign_in_page.verify_sign_in_page_opened()


########################################################################################
# 1- 2nd scenario...


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.header.cart_icon()


@then('Verify "Your Shopping Cart is empty." text present')
def verify_shopping_cart_empty_text_present(context):
    context.app.shopping_cart_page.verify_shopping_cart_empty_text_present()


########################################################################################

# 2- Rewrite “Add a product to cart” scenario using Page Object pattern.

@when('user will search for {search_word}')
def search_for_product(context, search_word):
    context.app.header.search_product(search_word)


@when('user will select the product')
def select_product(context):
    context.app.search_results_page.select_product()


@when('user will add product into cart')
def user_adds_product_into_cart(context):
    context.app.product_page.add_into_cart()


@then('Verify {search_word} item is shown in the cart')
def verify_added_product_is_in_cart(context, search_word):
    context.app.header.verify_cart_has_element(search_word)

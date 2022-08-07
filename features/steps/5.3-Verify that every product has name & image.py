from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

SEARCH_RESULTS = (By.CSS_SELECTOR,"[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span.a-text-normal")
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")

@then('Verify that every product has name & image')
def every_product_has_name_and_image(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    for product in all_products:
        print('***** print(product)')
        print(product)

        print('***** print(product.text)')
        print(product.text)

        title = product.find_element(*PRODUCT_TITLE).text

        print('***** print(\n\nTITLE, title)')
        print('\n\nTITLE', title)

        assert title !="", 'Error: Title should not be blank'
        product.find_element(*PRODUCT_IMG)

from behave import when, then
from time import sleep

#   Note:
#   To run action chains (For Language selection in AMAZON FLAG DROP-DOWN MENU):
#   In header.py you import-->     from selenium.webdriver.common.action_chains import ActionChains
#   To hover over the selected flag, find locator (SELECTED FLAG) & add it into header.py under class.
#   Then in steps you create a def for hover - here at the bottom.
#   Same way for selecting Spanish flag: add locator & def at the bottom.

@when('hover over language options')
def hover_over_lang_options(context):
    context.app.header.hover_over_lang_options()


@then('verify spanish option present')
def verify_esp_option_present(context):
    context.app.header.verify_esp_option_present()
    #sleep(3)

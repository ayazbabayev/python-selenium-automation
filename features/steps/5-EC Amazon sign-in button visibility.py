from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# When Wait for 8 seconds
# Then Verify that Sign -In button disappears

SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip span.nav-action-inner")

@then('Verify that Sign-In button is clickable')
def verify_signin_button_is_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN), message='Error: Sign-In not clickable')

@when("Wait for {sec} seconds")
def wait_x_sec(context, sec):
    sleep(int(sec))

@then('Verify that Sign-In button disappears')
def verify_sign_in_btn_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP_BTN), message='Error: Sign-In still visible')

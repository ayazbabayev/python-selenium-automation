from selenium.webdriver.common.by import By
from behave import when, given, then
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_NOTICE = (By.CSS_SELECTOR, "[href*='amazon.com/privacy']")
PRIVACY_HEADER = (By.CSS_SELECTOR, "h1")


@given('Open Amazon Terms & Conditions page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original Window: ', context.original_window)


@when('Click on Privacy Notice link')
def click_on_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print('Current Windows: ', context.driver.window_handles)
    privacy_window = context.driver.window_handles[1]
    context.driver.switch_to.window(privacy_window)


@then('Verify Amazon Privacy Notice page opened')
def verify_privacy_page_opened(context):
    expected_header = "Amazon.com Privacy Notice"
    actual_header = context.driver.find_element(By.CSS_SELECTOR, "h1").text
    # Can we shorten line above to a shorcut as PRIVACY_NOTICE?
    assert expected_header == actual_header, f'Error: failed to open Privacy Notice page'


@then('User can close new window & switch back to original')
def close_window_and_return_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)

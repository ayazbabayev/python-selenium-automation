# STORE ALL WINDOWS IN A VARIABLE:
# original_window = driver.current_window_handle
# old_windows = driver.window_handles


# CLICK ON ELEMENT THAT OPENS NEW WINDOW:
# link.click()


# WAIT FOR NEW WINDOW TO OPEN:
# context.wait.until(EC.new_window_is_opened)


# SWITCH TO NEW WINDOW:
# new_window = driver.window_handles(1)
# driver.switch_to.window(new_window)


# CLOSE NEW WINDOW:
# context.driver.close()

# GO BACK:
# context.driver.switch_to.window(original_window)


# EXAMPLE: ###############################################################

from selenium.webdriver.common.by import By
from behave import when, given, then
from selenium.webdriver.support import expected_conditions as EC

DOG_IMG = (By.CSS_SELECTOR, 'img#d')

@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original window: ', context.original_window)

@when('Click on a dog image')
def click_on_dog_image(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(DOG_IMG), message= 'Error: image not clickable.'
    ).click()

@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print('Current windows: ', context.driver.window_handles)
    # Wait above is to wait for 2 windows to be present and ready to be printed.
    # Print will give you window IDs, their sequence go like 0, 1, 2, 3...
    # ['CDwindow-52C22950B858C62C25D917E85EA2C8E1', 'CDwindow-581231D85D0747F391E1A5064EF4794C']
    # [0, 1] ... So the line below points to new window ID:
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)

@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/'))

@then('Close blog')
def close_blog(context):
    context.driver.close()

@then('Return to original window')
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
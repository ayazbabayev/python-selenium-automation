from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

@given('open amazon bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/BestSellers/')
    sleep(2)

@when('User can click through top links and verify correct page')
def click_through_toplinks_and_verify_pages(context):
    top_links = context.driver.find_elements(*TOP_LINKS)
    print(top_links)

    for i in range(len(top_links)):    # for EVERY ITERATION(i) from 0 to 4
        link_to_click = context.driver.find_elements(*TOP_LINKS)[i] # HER iteration'da LINKLERI TAP - Will search for all elements & click the ele-s using its' index
        link_text = link_to_click.text  # TEXTLERI GOTUR - grabs the text of those links
        link_to_click.click()           # LINKLERE TIKLA - clicks on those links
        sleep(2)                        # browser not updated to 104 so gives loading status error. sleep used to avoid flakiness.
        header_text = context.driver.find_element(*HEADER).text #BASLIGI GOTUR
        assert link_text in header_text, f'Expected {link_text} but got {header_text}'


# top_links = context.driver.find_elements(*TOP_LINKS) # To avoid stale element situation ea. time the page refreshes, we make it to find elements again in this loop

    # link_text = link_to_click.text
    # link_to_click.click()
    # sleep(2)
    # header_text = context.driver.find_element(*HEADER).text

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(r'C:\\Users\\ababa\\Desktop\\QA Automation\\PythonSeleniumAutomation\\python-selenium-automation\\chromedriver.exe')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 12)
    context.app = Application(context.driver)
    # (7) WE IMPORTED APPLICATION in line 3 & WE ADDED IT INSIDE BEHAVE CONTEXT above.
    # Context app will call our application.

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

from behave import fixture, use_fixture
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


@fixture
def browser_edge(context):
    context.browser = Edge(executable_path=r'E:/DEV/Driver/edgedriver.exe')
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(browser_edge, context)


def after_feature(context, feature):
    context.browser.get('https://test-bees.herokuapp.com')
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/form/button'))).click()
    context.browser.delete_all_cookies()


def before_step(context, step):
    sleep(1)

from behave import fixture, use_fixture
from selenium.webdriver import Edge
from time import sleep


@fixture
def browser_edge(context):
    context.browser = Edge(executable_path=r'E:/DEV/Driver/edgedriver.exe')
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(browser_edge, context)


def before_step(context, step):
    sleep(1)

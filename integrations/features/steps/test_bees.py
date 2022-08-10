from behave import given, when, then
from integrations.elements.login_elements import LoginElements
import time

# Acesso a tela de login
@given('que entro no site')
def goto_url(context):
    context.login_elements = LoginElements(context.browser)
    context.browser.get(context.login_elements.url)


# Fazer cadastro na plataforma
@then('devo visualizar a tela de login')
def view_initial_page(context):
    assert context.login_elements.view_initial_page() is not None


# Fazer cadastro na plataforma
@given('que clico no botão de signup')
def button_signup_click(context):
    context.login_elements = LoginElements(context.browser)
    context.browser.get(context.login_elements.url)
    context.login_elements.button_signup().click()


@when('insiro os dados para o cadastro e clico em login')
def signup_data(context):
    time.sleep(1)
    context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    context.login_elements.signup_element_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_confirm_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_button().click()
    context.login_elements.login_element_button().click()


@then('devo ser direcionado para a tela principal')
def button_login_page(context):
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/users/sign_in'


# Scenario: Acesso a conta
@given('que estou na tela de login')
def initial_viewpage(context):
    context.login_elements = LoginElements(context.browser)
    context.browser.get(context.login_elements.url)


@when('preencho os dados')
def insert_login(context):
    context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    context.login_elements.signup_element_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_button().click()


@then('devo ser direcionado para a tela inicial')
def login_redirect(context):
    retorno = context.login_elements.login_redirect().text
    print(retorno)
    time.sleep(10)
    assert retorno == 'Signed in successfully.'





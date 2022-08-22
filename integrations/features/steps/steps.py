from behave import given, when, then
from integrations.elements.login_elements import LoginElements


@given('que entro no site')
def goto_url(context):
    context.login_elements = LoginElements(context.browser)
    context.browser.get(context.login_elements.url)


@then('devo visualizar a tela de login')
def view_initial_page(context):
    assert context.login_elements.view_initial_page() is not None


@given('que clico no botão de signup')
def button_signup_click(context):
    context.login_elements = LoginElements(context.browser)
    context.browser.get(context.login_elements.url)
    context.login_elements.button_signup().click()


@when('insiro os dados para o cadastro e clico em login')
def signup_data(context):
    context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    context.login_elements.signup_element_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_confirm_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_button().click()
    context.login_elements.login_element_button().click()


@then('devo ser direcionado para a tela principal')
def button_login_page(context):
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/users/sign_in'


@given('que estou na tela de login')
def initial_viewpage(context):
    context.login_elements = LoginElements(context.browser)
    context.browser.get(context.login_elements.url)


@when('preencho os dados')
def insert_login(context):
    context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    context.login_elements.signup_element_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_button().click()


@when('preencho as informações de login com o email incorreto')
def insert_login(context):
    context.login_elements.signup_element_email().send_keys('teste_gmail.com')
    context.login_elements.signup_element_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_button().click()


@then('devo visualizar uma notificação de email ou senha incorreta')
def view_notification(context):
    assert context.login_elements.message_error_login() is not False


@when('preencho as informações de login com a senha incorreta')
def insert_login(context):
    context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    context.login_elements.signup_element_pass().send_keys('123@MudarERRADO')
    context.login_elements.signup_element_button().click()


@then('devo ser direcionado para a tela inicial')
def login_redirect(context):
    retorno = context.login_elements.login_redirect().text
    assert retorno == 'Signed in successfully.'


@when('clico em "Forgot your password?"')
def click_button_forgot_password(context):
    context.login_elements.click_button_forgot_password().click()


@when('insiro o email e aperto a tecla "enter"')
def insert_email_to_send_pass(context):
    context.login_elements.input_email_forgot_password()


@then('devo ver a mensagem "sent to registered email"')
def send_email_reset_pass(context):
    assert context.login_elements.forgot_pass_error() is True


@when('clico em logout')
def click_logout_button(context):
    context.login_elements.button_logout().click()


@then('devo ver uma mensagem de logout e ser desconectado da conta')
def message_logout(context):
    assert context.login_elements.message_logout() is True

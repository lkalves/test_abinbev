from behave import given, when, then
from integrations.elements.login_elements import LoginElements
from integrations.elements.deposits_elements import DepositsElements


@given('que estou na tela inicial')
def initial_screen(context):
    context.login_elements = LoginElements(context.browser)
    context.deposits_elements = DepositsElements(context.browser)
    context.browser.get(context.login_elements.url)
    context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    context.login_elements.signup_element_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_button().click()


@when('clico em deposits no menu superior')
def click_button_deposits(context):
    context.deposits_elements.menu_element_deposits().click()


@then('devo ser redirecionado para a lista de depositos')
def deposits_list(context):
    a = context.deposits_elements.deposits_itens()
    assert len(a) != 0


@given('que estou na tela de depositos')
def deposits_list(context):
    context.deposits_elements = DepositsElements(context.browser)
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/deposits'


@when('clico no botão show this deposit')
def click_button_show_deposit(context):
    context.browser.get(context.deposits_elements.button_show_deposit())


@then('devo ser direcionado para os detalhes do deposito')
def view_page_deposits(context):
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/deposits/361'


@given('que estou na tela de detalhes do deposito')
def check_screen_deposit(context):
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/deposits/361'


@when('clico no botao de edit this deposit e insiro as informações que desejo trocar e clico em update')
def edit_data_deposit(context):
    context.deposits_elements = DepositsElements(context.browser)
    context.deposits_elements.button_edit_deposit().click()
    context.deposits_elements.edit_name_deposit().clear()
    context.deposits_elements.edit_name_deposit().send_keys('Deposito VR')
    context.deposits_elements.edit_city_deposit().clear()
    context.deposits_elements.edit_city_deposit().send_keys('Volta Redonda')
    context.deposits_elements.edit_zipcode_deposit().clear()
    context.deposits_elements.edit_zipcode_deposit().send_keys('27213000')
    context.deposits_elements.button_update_deposit().click()


@then('devo ver a mensagem de Deposit was successfully updated e as informações trocadas')
def update_deposit_sucess(context):
    message = context.deposits_elements.deposit_sucess_update()
    assert message.text == 'Deposit was successfully updated.'


@given('que estou na tela de deposito e abro um deposito para destruir')
def open_page_destroy_deposit(context):
    context.deposits_elements = DepositsElements(context.browser)
    context.login_elements = LoginElements(context.browser)
    context.deposits_elements.menu_element_deposits().click()
    context.deposits_elements.click_deposit_destroy().click()


@when('clico em destruir deposito')
def destroy_deposit_button(context):
    context.deposits_elements.click_destroy_button().click()


@then('devo ver que o deposito foi excluido')
def destroy_is_sucess(context):
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/deposits'

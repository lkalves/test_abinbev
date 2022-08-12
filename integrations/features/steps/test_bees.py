import time

from behave import given, when, then
from integrations.elements.login_elements import LoginElements
from integrations.elements.deposits_elements import DepositsElements
from integrations.elements.items_elements import ItemsElements
from integrations.elements.inventories_elements import InventoriesElements


# Feature: login.feature
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
    assert retorno == 'Signed in successfully.'


# Feature: deposits.feature
# Scenario: Lista de depositos
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


# Scenario: Abrir deposito selecionado
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


# Scenario: Editar deposito
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
    after_edit = context.deposits_elements.deposit_edit_name_response().text
    assert message.text == 'Deposit was successfully updated.'
    # assert after_edit == 'Name: Deposito Beer VR'


# Scenario: Destroir deposito
@given('que estou na tela de deposito e abro um deposito para destroir')
def open_page_destroy_deposit(context):
    context.deposits_elements = DepositsElements(context.browser)
    context.login_elements = LoginElements(context.browser)
    # context.browser.get(context.login_elements.url)
    # context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    # context.login_elements.signup_element_pass().send_keys('123@Mudar')
    # context.login_elements.signup_element_button().click()
    context.deposits_elements.menu_element_deposits().click()
    context.deposits_elements.click_deposit_destroy().click()


@when('clico em destruir deposito')
def destroy_deposit_button(context):
    context.deposits_elements.click_destroy_button().click()


@then('devo ver que o deposito foi excluido')
def destroy_is_sucess(context):
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/deposits'


# Feature: Items
# Scenario: Lista de items

# @given('que estou na tela inicial e c')
# def initial_screen(context):
#     context.deposits_elements = DepositsElements(context.browser)
#     context.login_elements = LoginElements(context.browser)
#     context.browser.get(context.login_elements.url)
#     context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
#     context.login_elements.signup_element_pass().send_keys('123@Mudar')
#     context.login_elements.signup_element_button().click()


@when('clico em items no menu superior')
def click_button_items(context):
    context.items_elements = ItemsElements(context.browser)
    context.items_elements.menu_element_items().click()


@then('devo ser redirecionado para a lista de items')
def check_redirect_items(context):
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/items'


# Scenario: Abrir lista de itens selecionado
@given('que estou na tela de items e clico no botão show this item')
def click_button_show_item(context):
    context.login_elements = LoginElements(context.browser)
    context.items_elements = ItemsElements(context.browser)
    # context.browser.get(context.login_elements.url)
    # context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    # context.login_elements.signup_element_pass().send_keys('123@Mudar')
    # context.login_elements.signup_element_button().click()
    context.items_elements.menu_element_items().click()
    assert len(context.items_elements.list_itens()) != 0
    context.items_elements.click_item_description().click()


@then('devo ser direcionado para os detalhes de item')
def redirect_is_correct(context):
    assert context.items_elements.button_edit_item() is not None


# Scenario: Criar item
@given('que estou na tela de item')
def click_button_show_item(context):
    context.login_elements = LoginElements(context.browser)
    context.items_elements = ItemsElements(context.browser)
    # context.browser.get(context.login_elements.url)
    # context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    # context.login_elements.signup_element_pass().send_keys('123@Mudar')
    # context.login_elements.signup_element_button().click()
    context.items_elements.menu_element_items().click()


@when('clico em add item e insiro as informações')
def click_button_add_item(context):
    context.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    context.items_elements.button_insert_item().click()
    context.items_elements.name_insert_item().send_keys('Dreher')
    context.items_elements.height_insert_item().send_keys('18')
    context.items_elements.width_insert_item().send_keys('8')
    context.items_elements.weight_insert_item().send_keys('1')
    context.items_elements.button_new_item().click()


@then('devo visualizar o item recém criado')
def verify_create_item_sucess(context):
    response = context.items_elements.create_item_sucess().text
    assert 'Item was successfully created.' == response
    print(response)
    import ipdb
    ipdb.sset_trace()


# Scenario: Editar item
@when('clico em edit item e insiro as informações para atualizar')
def edit_item(context):
    context.items_elements.click_item_description().click()
    context.items_elements.button_edit_item_info().click()
    context.items_elements.edit_name_item().clear()
    context.items_elements.edit_name_item().send_keys('Banana nanica')
    context.items_elements.edit_height_item().clear()
    context.items_elements.edit_height_item().send_keys(10)
    context.items_elements.edit_width_item().clear()
    context.items_elements.edit_width_item().send_keys(8)
    context.items_elements.edit_weight_item().clear()
    context.items_elements.edit_weight_item().send_keys(19)
    context.items_elements.button_new_item().click()


@then('ser redirecionado e mostrada a mensagem de sucesso')
def redirect_after_edit_item(context):
    texto = context.items_elements.redirect_after_edit().text
    assert 'Item was successfully updated.' == texto


# Inventario
# Scenario: Abrir lista de inventários
@given('que realizo o login')
def login(context):
    context.login_elements = LoginElements(context.browser)
    context.items_elements = ItemsElements(context.browser)
    context.browser.get(context.login_elements.url)
    context.login_elements.signup_element_email().send_keys('teste_lucas@gmail.com')
    context.login_elements.signup_element_pass().send_keys('123@Mudar')
    context.login_elements.signup_element_button().click()


@when('clico em inventaries do menu superior')
def click_menu_inventory(context):
    context.inventories_elements = InventoriesElements(context.browser)
    context.inventories_elements.menu_element_inventories().click()


@then('devo ver a lista de inventários')
def view_inventaries(context):
    elements = context.inventories_elements.get_list_inventory()
    assert len(elements) >= 0
    # import ipdb
    # ipdb.sset_trace()


# Scenario: Criar um inventario
@when('clico no botao de new inventory')
def click_button_new_inventory(context):
    context.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
    context.inventories_elements.button_new_inventory().click()


@then('devo visualizar a tela de criação de inventário')
def view_page_create_inventory(context):
    current_url = context.browser.current_url
    assert 'https://test-bees.herokuapp.com/inventories/new' == current_url


@when('preencho os dados e clico em criar')
def insert_data_new_inventory(context):
    context.inventories_elements.item_new_inventory()
    context.inventories_elements.deposit_new_inventory()
    context.inventories_elements.item_count_new_inventory().send_keys(199)
    context.inventories_elements.button_create_inventory().click()


@then('devo visualizar a mensagem de inventory created with success')
def inventory_created_is_success(context):
    lista = context.inventories_elements.inventory_created_is_success()
    assert lista.text == 'Inventory was successfully created.'


# Scenario: Visualizar inventario
@when('clico em show this inventory')
def click_details_inventory(context):
    context.inventories_elements.click_inventory_description().click()


@then('devo visualizar o inventário')
def view_inventory_page(context):
    element = context.inventories_elements.inventory_page_element()
    assert element.text == 'Destroy this inventory'


# Scenario: Editar inventario
@when('clicar em edit this inventory')
def button_edit_inventory(context):
    context.inventories_elements.button_edit_inventory().click()

@when('preencho o formulario e clico em edit')
def editing_inventory(context):
    context.inventories_elements.edit_item_inventory()
    context.inventories_elements.edit_deposit_inventory()
    context.inventories_elements.edit_item_count_inventory().send_keys(1999)
    context.inventories_elements.edit_item_send_form().click()


@then('devo visualizar a mensagem de que foi editado com sucesso')
def edit_inventory_is_success(context):
    elemento = context.inventories_elements.edit_inventory_is_success().text
    assert elemento == 'Inventory was successfully updated.'

# Scenario: Apagar inventario
@when('clico em destroy this inventory')
def destroy_inventory(context):
    context.inventories_elements.destroy_inventory_button().click()


@then('devo visualizar a mensagem de inventário destruido')
def destroy_inventory_is_sucess(context):
    elemento = context.inventories_elements.destroy_inventory_is_sucess().text
    assert elemento == 'Inventory was successfully destroyed.'
    import ipdb
    ipdb.sset_trace()


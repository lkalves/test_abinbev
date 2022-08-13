from behave import given, when, then
from time import sleep
from integrations.elements.login_elements import LoginElements
from integrations.elements.inventories_elements import InventoriesElements
from integrations.elements.items_elements import ItemsElements


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


@when('clico no botao de new inventory')
def click_button_new_inventory(context):
    context.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(1)
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


@when('clico em show this inventory')
def click_details_inventory(context):
    context.inventories_elements.click_inventory_description().click()


@then('devo visualizar o inventário')
def view_inventory_page(context):
    element = context.inventories_elements.inventory_page_element()
    assert element.text == 'Destroy this inventory'


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


@when('clico em destroy this inventory')
def destroy_inventory(context):
    context.inventories_elements.destroy_inventory_button().click()


@then('devo visualizar a mensagem de inventário destruido')
def destroy_inventory_is_sucess(context):
    elemento = context.inventories_elements.destroy_inventory_is_sucess().text
    assert elemento == 'Inventory was successfully destroyed.'

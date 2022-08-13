from behave import given, when, then
from integrations.elements.login_elements import LoginElements
from integrations.elements.items_elements import ItemsElements
from time import sleep


@when('clico em items no menu superior')
def click_button_items(context):
    context.items_elements = ItemsElements(context.browser)
    context.items_elements.menu_element_items().click()


@then('devo ser redirecionado para a lista de items')
def check_redirect_items(context):
    current_url = context.browser.current_url
    assert current_url == 'https://test-bees.herokuapp.com/items'


@given('que estou na tela de items e clico no botão show this item')
def click_button_show_item(context):
    context.login_elements = LoginElements(context.browser)
    context.items_elements = ItemsElements(context.browser)
    context.items_elements.menu_element_items().click()
    assert len(context.items_elements.list_itens()) != 0
    context.items_elements.click_item_description().click()


@then('devo ser direcionado para os detalhes de item')
def redirect_is_correct(context):
    assert context.items_elements.button_edit_item() is not None


@given('que estou na tela de item')
def click_button_show_item(context):
    context.login_elements = LoginElements(context.browser)
    context.items_elements = ItemsElements(context.browser)
    context.items_elements.menu_element_items().click()


@when('clico em add item e insiro as informações')
def click_button_add_item(context):
    context.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(2)
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

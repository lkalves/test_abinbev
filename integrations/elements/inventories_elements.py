from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class InventoriesElements:
    def __init__(self, browser):
        self.url = 'https://test-bees.herokuapp.com/'
        self.driver = browser

    # Scenario: Abrir lista de inventários
    def menu_element_inventories(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a')))

    def get_list_inventory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="inventories"]/table/tbody/tr')))

    def click_inventory_description(self):
        lista = self.get_list_inventory()
        return lista[0].find_element(By.XPATH, 'td[4]/a')

    # Scenario: Criar um inventario
    def button_new_inventory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/a')))

    def item_new_inventory(self):
        selecao = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'inventory_item_id'))))
        return selecao.select_by_index(1)

    def deposit_new_inventory(self):
        selecao = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'inventory_deposit_id'))))
        return selecao.select_by_index(9)

    def item_count_new_inventory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'inventory_item_count')))

    def button_create_inventory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'commit')))

    def inventory_created_is_success(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/p')))

    # Scenario: Visualizar inventario
    def inventory_page_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/button')))

    # Scenario: Editar inventario
    def button_edit_inventory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/a[1]')))

    def edit_item_inventory(self):
        selecao = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'inventory_item_id'))))
        return selecao.select_by_visible_text('Dreher')

    def edit_deposit_inventory(self):
        selecao = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'inventory_deposit_id'))))
        return selecao.select_by_visible_text('Deposito VR')

    def edit_item_count_inventory(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'inventory_item_count')))
        return elemento

    def edit_item_send_form(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'commit')))
        return elemento

    def edit_inventory_is_success(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/p')))
        return elemento

    # Scenario: Apagar inventario
    def destroy_inventory_button(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/button')))
        return elemento

    def destroy_inventory_is_sucess(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/p')))
        return elemento

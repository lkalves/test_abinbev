from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ItemsElements:
    def __init__(self, browser):
        self.url = 'https://test-bees.herokuapp.com/'
        self.driver = browser

    def menu_element_items(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')))

    def list_itens(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="items"]/table/tbody/tr')))

    def click_item_description(self):
        lista = self.list_itens()
        return lista[0].find_element(By.XPATH, 'td[5]/a')

    def button_edit_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/a[1]')))

    def button_insert_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/a')))

    def name_insert_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item_name')))

    def height_insert_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item_height')))

    def width_insert_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item_width')))

    def weight_insert_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item_weight')))

    def button_new_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'commit')))

    # edit
    def create_item_sucess(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/p')))

    def button_edit_item_info(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div:nth-child(4) > a:nth-child(1)')))

    def edit_name_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item_name')))

    def edit_height_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item_height')))

    def edit_width_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item_width')))

    def edit_weight_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item_weight')))

    def redirect_after_edit(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/p')))

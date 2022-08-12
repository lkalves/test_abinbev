from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DepositsElements:
    def __init__(self, browser):
        self.url = 'https://test-bees.herokuapp.com/'
        self.driver = browser

    def menu_element_deposits(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/a')))

    def deposits_itens(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="deposits"]/table/tbody/tr')))

    def button_show_deposit(self):
        return 'https://test-bees.herokuapp.com/deposits/361'
        # import ipdb
        # ipdb.sset_trace()
        # return WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="deposits"]/table/tbody/tr[5]/td[7]/a')))

    def button_edit_deposit(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div:nth-child(4) > a:nth-child(1)')))

    def edit_name_deposit(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'deposit_name')))

    def edit_city_deposit(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'deposit_city')))

    def edit_zipcode_deposit(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'deposit_zipcode')))

    def button_update_deposit(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'commit')))

    def deposit_sucess_update(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/p')))

    def deposit_edit_name_response(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="deposit_361"]/p[1]')))

    def click_deposit_destroy(self):
        lista = self.deposits_itens()
        return lista[0].find_element(By.XPATH, 'td[7]/a')

    def click_destroy_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div:nth-child(4) > form > button')))


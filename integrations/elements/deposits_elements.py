from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageObject:
    def __init__(self, browser):
        self.driver = browser

    def find_element(self, element, by=By.XPATH):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((by, element))
        )

    def find_elements(self, element, by=By.XPATH):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((by, element))
        )

    def find_element_css_selector(self, element, by=By.CSS_SELECTOR):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((by, element))
        )

    def find_element_id(self, element, by=By.ID):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((by, element))
        )

    def find_element_name(self, element, by=By.NAME):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((by, element))
        )


class DepositsElements(PageObject):
    def __init__(self, browser):
        self.url = 'https://test-bees.herokuapp.com/'
        super().__init__(browser)

    @property
    def menu_element_deposits(self):
        return self.find_element('//*[@id="navbarSupportedContent"]/ul/li[1]/a')

    @property
    def deposits_itens(self):
        return self.find_elements('//*[@id="deposits"]/table/tbody/tr')

    @property
    def button_show_deposit(self):
        return 'https://test-bees.herokuapp.com/deposits/361'

    @property
    def button_edit_deposit(self):
        return self.find_element_css_selector('body>div>div:nth-child(4)>a:nth-child(1)')

    @property
    def edit_name_deposit(self):
        return self.find_element_id('deposit_name')

    @property
    def edit_city_deposit(self):
        return self.find_element_id('deposit_city')

    @property
    def edit_zipcode_deposit(self):
        return self.find_element_id('deposit_zipcode')

    @property
    def button_update_deposit(self):
        return self.find_element_name('commit')

    @property
    def deposit_sucess_update(self):
        return self.find_element('/html/body/div/p')

    @property
    def deposit_edit_name_response(self):
        return self.find_element('//*[@id="deposit_361"]/p[1]')

    @property
    def click_deposit_destroy(self):
        lista = self.deposits_itens
        return lista[0].find_element(By.XPATH, 'td[7]/a')

    @property
    def click_destroy_button(self):
        return self.find_element_css_selector('body>div>div:nth-child(4)>form>button')

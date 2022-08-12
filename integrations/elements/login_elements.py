from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginElements:
    def __init__(self, browser):
        self.url = 'https://test-bees.herokuapp.com/'
        self.driver = browser

    def view_initial_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, 'commit')))

    def button_signup(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/a[1]')))
        return element

    def signup_element_email(self):
        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'user_email')))
        return email

    def signup_element_pass(self):
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'user_password')))
        return password

    def signup_element_confirm_pass(self):
        confirm_pass = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'user_password_confirmation')))
        return confirm_pass

    def signup_element_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'commit')))

    def login_element_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/a')))

    def login_redirect(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/p')))

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

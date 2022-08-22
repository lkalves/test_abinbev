from selenium.common import TimeoutException
from selenium.webdriver import Keys
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

    def message_error_login(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'is not correct')]")))
            return True
        except TimeoutException:
            return False

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

    def click_button_forgot_password(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/a[2]')))

    def input_email_forgot_password(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'user_email')))
        elemento.send_keys('teste_lucas@gmail.com')
        elemento.send_keys(Keys.RETURN)

    def forgot_pass_error(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'sent to registered email')]")))
            return True
        except TimeoutException:
            return False

    def button_logout(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/form/button')))

    def message_logout(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'successfully disconnected from "
                                                          "account')]")))
            return True
        except TimeoutException:
            return False

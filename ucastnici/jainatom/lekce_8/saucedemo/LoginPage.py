from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class LoginPage:
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    submit_button = (By.ID, "login-button")
    page_url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def we_are_on_page(self):
        assert self.page_url == self.driver.current_url, f"We are not on the right page '{self.page_url}'"

    def login_user(self, username, password):
        field_username = self.driver.find_element(*self.username_field)
        field_username.send_keys(username)
        field_password = self.driver.find_element(*self.password_field)
        field_password.send_keys(password)
        button_submit = self.driver.find_element(*self.submit_button)
        button_submit.click()

    def verify_logout(self):
        '''Checks that user is on login page.'''
        login_button = self.driver.find_element(By.ID, 'login-button').is_displayed()
        assert login_button, 'Logout failed, login button not displayed.'
        logging.info('Correct page displayed after logout.')

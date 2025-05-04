from selenium.webdriver.common.by import By
import logging
import env_variables

class LoginPage:
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    submit_button = (By.ID, "login-button")
    page_url = env_variables.login_page_url

    def __init__(self, driver):
        self.driver = driver

    def we_are_on_page(self):
        assert self.page_url == self.driver.current_url, f"We are not on the right page '{self.page_url}'"

    def login_user(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

    def verify_logout(self):
        '''Checks that user is on login page.'''
        login_button = self.driver.find_element(By.ID, 'login-button').is_displayed()
        assert login_button, 'Logout failed, login button not displayed.'
        logging.info('Login button found.')
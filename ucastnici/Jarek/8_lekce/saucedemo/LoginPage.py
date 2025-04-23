from selenium.webdriver.common.by import By
import logging

class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def login_user(self, username, password):
        logging.info("Přihlašuji uživatele")
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def we_are_on_page(self):
        assert self.driver.find_element(*self.LOGIN_BUTTON).is_displayed()

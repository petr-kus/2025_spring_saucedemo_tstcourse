from selenium.webdriver.common.by import By
from selenium import webdriver
import logging

class Login:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: webdriver.Firefox, options=None):
        self.__driver = driver
        if options:
            options.add_argument('--start-maximized')

    @property
    def driver(self) -> webdriver.Firefox:
        return self.__driver

    def open_browser(self, url: str):
        logging.info("Otevírám stránku: %s", url)
        self.driver.get(url)

    def login(self, username: str, password: str) -> None:
        logging.info("Přihlašování uživatele: %s", username)
        try:
            self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
            self.driver.find_element(*self.LOGIN_BUTTON).click()
        except Exception as e:
            logging.error("Chyba při přihlašování: %s", e)
            raise

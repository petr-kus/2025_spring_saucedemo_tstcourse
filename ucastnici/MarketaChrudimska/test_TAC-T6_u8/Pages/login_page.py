from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Config import config
from Pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open_login_page(self):
        self.driver.get(config.URL)

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        print(f"Přihlašuji uživatele: {username}")
        logger.info(f"Přihlašuji uživatele: {username}")

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.url_contains("inventory.html"))
            return True
        except:
            return False
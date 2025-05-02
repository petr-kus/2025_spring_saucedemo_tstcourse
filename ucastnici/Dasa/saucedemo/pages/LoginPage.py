from selenium.webdriver.common.by import By
import logging

class LoginPage:
    # Lokátory pomocí XPath
    USERNAME_FIELD = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error-message-container')]")

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.url = "https://www.saucedemo.com/"
        # TODO Lektor: tato stranka by se mela vzit z te konfigurace... .
        # TODO Lektor: jinak moc pekne... .

    def open(self):
        """Otevře přihlašovací stránku."""
        self.driver.get(self.url)
        self.logger.info("Otevřena přihlašovací stránka")

    def login_user(self, username, password):
        """Provede přihlášení uživatele."""
        self.open()  # Nejdřív otevřeme stránku
        self.logger.info(f"Pokus o přihlášení uživatele: {username}")
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.logger.info("Přihlašovací formulář byl odeslán")

    def we_are_on_page(self):
        """Ověří, že jsme na přihlašovací stránce."""
        assert self.url in self.driver.current_url
        self.logger.info("Ověřeno, že jsme na přihlašovací stránce")

    def get_error_message(self):
        """Získá chybovou zprávu při neúspěšném přihlášení."""
        try:
            error_text = self.driver.find_element(*self.ERROR_MESSAGE).text
            self.logger.info(f"Získána chybová zpráva: {error_text}")
            return error_text
        except:
            self.logger.info("Žádná chybová zpráva nebyla nalezena")
            return None 
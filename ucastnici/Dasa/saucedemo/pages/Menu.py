from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class Menu:
    # Lokátory pomocí XPath
    MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")
    CLOSE_MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-cross-btn']")

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, 10)  # Čekáme maximálně 10 sekund

    def open_menu(self):
        """Otevře menu."""
        self.logger.info("Otevírám menu")
        # Počkáme na načtení tlačítka menu
        menu_button = self.wait.until(EC.presence_of_element_located(self.MENU_BUTTON))
        menu_button.click()
        self.logger.info("Menu bylo otevřeno")
        # Počkáme na načtení menu
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK))

    def close_menu(self):
        """Zavře menu."""
        self.logger.info("Zavírám menu")
        self.driver.find_element(*self.CLOSE_MENU_BUTTON).click()
        self.logger.info("Menu bylo zavřeno")

    def press_logout(self):
        """Klikne na odkaz pro odhlášení."""
        self.logger.info("Klikám na odkaz pro odhlášení")
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
        self.logger.info("Byl kliknut odkaz pro odhlášení") 
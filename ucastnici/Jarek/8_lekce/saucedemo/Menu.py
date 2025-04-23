from selenium.webdriver.common.by import By
import logging

class Menu:
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        logging.info("Otevírám menu")
        self.driver.find_element(*self.MENU_BUTTON).click()

    def press_logout(self):
        logging.info("Odhlášení uživatele")
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

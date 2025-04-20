from selenium.webdriver.common.by import By
import logging

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def we_are_on_page(self):
        logging.info("Ověřuji, že jsme na stránce s produkty")
        assert self.driver.find_element(*self.TITLE).is_displayed()

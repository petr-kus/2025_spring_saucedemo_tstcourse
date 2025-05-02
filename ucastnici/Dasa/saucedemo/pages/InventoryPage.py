from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import logging

class InventoryPage:
    # Lokátory
    INVENTORY_CONTAINER = (By.CLASS_NAME, "inventory_container")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(@id, 'remove')]")
    CART_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    PRODUCTS = (By.XPATH, "//div[@class='inventory_item']")

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, 10)  # Čekáme maximálně 10 sekund

    def we_are_on_page(self):
        """Ověří, že jsme na stránce s produkty."""
        try:
            # Počkáme na načtení stránky
            self.wait.until(EC.url_contains(self.INVENTORY_URL))
            # Počkáme na načtení produktů
            self.wait.until(EC.presence_of_element_located(self.PRODUCTS))
            # TODO Lektor: toto cekani by nemelo byt potreba dle me pro overeni ze jsi na strance :-).

            self.logger.info("Stránka s produkty byla úspěšně načtena")
            return True
        except Exception as e:
            self.logger.error(f"Stránka s produkty nebyla načtena: {str(e)}")
            return False

    def add_random_products_to_cart(self):
        """Přidá náhodný počet produktů do košíku."""
        self.logger.info("Přidávám náhodné produkty do košíku")
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if not add_buttons:
            self.logger.error("Nenalezeny žádné tlačítka pro přidání do košíku")
            return
        
        num_products = random.randint(1, len(add_buttons))
        for i in range(num_products):
            add_buttons[i].click()
            self.logger.info("Produkt přidán do košíku")

    def remove_from_cart_all_products(self):
        """Odebere všechny produkty z košíku."""
        self.logger.info("Odebírám všechny produkty z košíku")
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        for button in remove_buttons:
            button.click()
            self.logger.info("Produkt odebrán z košíku")

    def sort_products(self, option):
        """Seřadí produkty podle zvolené možnosti."""
        self.logger.info(f"Řadím produkty podle: {option}")
        self.driver.find_element(*self.SORT_DROPDOWN).click()
        sort_option = (By.XPATH, f"//option[text()='{option}']")
        self.driver.find_element(*sort_option).click()
        self.logger.info("Produkty byly seřazeny") 
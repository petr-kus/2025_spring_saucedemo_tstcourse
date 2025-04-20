from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import wait_for_element, wait_for_element_with_text
import random
import logging
import time

class InventoryPage:
    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
    remove_from_cart_button = (By.XPATH, "//button[text()='Remove']")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    page_url = "inventory"

    def __init__(self, driver):
        self.driver = driver

    def we_are_on_page(self):
        assert self.page_url in self.driver.current_url

    def add_product_to_cart(self,add_button):
        add_button.click()

    def remove_product_from_cart(self,remove_button):
        remove_button.click()
    
    def add_random_products_to_cart(self):
        add_to_cart_buttons = self.driver.find_elements(*self.add_to_cart_button)
        num_to_add = random.randint(1, len(add_to_cart_buttons))
        buttons_to_add = random.sample(add_to_cart_buttons, num_to_add)

        for button in buttons_to_add:
            self.add_product_to_cart(button)
            logging.info(f"Item '{button}' was added to cart.")

        wait_for_element_with_text(self.driver, 5, (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']"), str(num_to_add))
        cart_count = int(self.driver.find_element(*self.cart_badge).text)
        assert cart_count == num_to_add, f"Expected '{num_to_add}' items, but found '{cart_count}' in cart."

    def verify_login(self):
        """Checks that Products is loaded in header."""
        products_header = self.driver.find_element(By.CLASS_NAME, 'title').text
        assert products_header == 'Products', 'Login failed, "Products" header not found.'
        assert self.driver.title == 'Swag Labs', 'Title incorrect after login.'
        logging.info("Correct page displayed after login.")


    
            

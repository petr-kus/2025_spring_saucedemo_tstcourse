from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random

class CartPage:
    ADD_TO_CART_BUTTONS_LOCATOR       = (By.XPATH, "//button[starts-with(@id, 'add-to-cart-')]")
    REMOVE_FROM_CART_BUTTONS_LOCATOR  = (By.XPATH, "//button[starts-with(@id, 'remove')]")
    CART_BADGE_LOCATOR                = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    def add_to_cart_buttons(self):
        return self.driver.find_elements(*self.ADD_TO_CART_BUTTONS_LOCATOR)

    @property
    def remove_from_cart_buttons(self):
        return self.driver.find_elements(*self.REMOVE_FROM_CART_BUTTONS_LOCATOR)

    @property
    def cart_badge(self):
        elems = self.driver.find_elements(*self.CART_BADGE_LOCATOR)
        return elems[0] if elems else None

    def add_random_item_to_cart(self):
        buttons = self.add_to_cart_buttons
        if not buttons:
            raise RuntimeError("No add-to-cart buttons found")
        idx = self.wait.until(lambda d: random.randint(0, len(buttons) - 1))
        buttons[idx].click()

    def get_cart_item_count(self) -> int:
        if not self.cart_badge:
            return 0
        text = self.cart_badge.text.strip()
        return int(text) if text.isdigit() else 0

    def get_remove_buttons_count(self) -> int:
        return len(self.remove_from_cart_buttons)

    def clear_cart(self):
        while self.remove_from_cart_buttons:
            before = len(self.remove_from_cart_buttons)
            self.remove_from_cart_buttons[0].click()
            self.wait.until(lambda d: len(d.find_elements(*self.REMOVE_FROM_CART_BUTTONS_LOCATOR)) < before)

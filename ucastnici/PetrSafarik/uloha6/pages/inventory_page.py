from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.XPATH, "//span[@data-test='title']")
        self.number_of_items_in_cart = (By.XPATH, "//span[@data-test='shopping-cart-badge']")
        self.add_backpack_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.enter_the_cart = (By.XPATH, "//a[@data-test='shopping-cart-link']")

    def check_page(self):
        actual_title = self.driver.find_element(*self.page_title).text
        return actual_title

    def get_number_of_items_in_cart(self):
        try:
            number = self.driver.find_element(*self.number_of_items_in_cart)
        except WebDriverException as e:
            return ""
        return number.text

    def add_item_to_cart(self):
        # Add item Backpack to the cart
        backpack_to_cart = self.driver.find_element(*self.add_backpack_to_cart)
        backpack_to_cart.click()

    def enter_cart_page(self):
        # Enter the cart page
        button_cart = self.driver.find_element(*self.enter_the_cart)
        button_cart.click()

from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class InventoryPage:
    
    page_title = (By.XPATH, "//span[@data-test='title']")
    number_of_items_in_cart = (By.XPATH, "//span[@data-test='shopping-cart-badge']")
    add_backpack_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    enter_the_cart = (By.XPATH, "//a[@data-test='shopping-cart-link']")
    
    expected_title_products = "Products"
    expected_title_cart = "Your Cart"

    def __init__(self, driver):
        self.driver = driver

    def check_product_page(self):
        actual_title = self.driver.find_element(*self.page_title).text
        assert actual_title == (self.expected_title_products), "Title mismatch"
        
    def check_cart_page(self):
        actual_cart_page_title = self.driver.find_element(*self.page_title).text
        assert actual_cart_page_title == self.expected_title_cart, "Title mismatch"    

    def get_number_of_items_in_cart(self):
        try:
            number = self.driver.find_element(*self.number_of_items_in_cart)
        except WebDriverException as e:
            return ""
        return number.text

    def add_item_to_cart(self):
        # Add item Backpack to the cart 
        backpack_to_cart = self.driver.find_element(*self.add_backpack_to_cart)
        #TODO: Lektor - tady se dela volba uvnitr, zviditelnil bych ji ven do test casu
        backpack_to_cart.click()

    def enter_cart_page(self):
        button_cart = self.driver.find_element(*self.enter_the_cart)
        button_cart.click()

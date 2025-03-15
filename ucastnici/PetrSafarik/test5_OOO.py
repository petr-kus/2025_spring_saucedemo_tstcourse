from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class ItemOrderSmokeTest:
    def __init__(self, user_name: str, password: str, first_name: str, last_name: str, post_code: str):
        self.user_name = user_name
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.post_code = post_code
        self.driver = webdriver.Firefox()
        
    def initialize_webdriver(self):
        # launch the saucedemo page
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(1)  # waiting time
        
    def login_enter_user_name(self):
        # Find and fill username field
        field_username = self.driver.find_element(By.ID, "user-name")
        field_username.send_keys(self.user_name)
        time.sleep(1)  # waiting time

    def login_enter_password(self):    
        # Find and fill password field
        field_password = self.driver.find_element(By.ID, "password")
        field_password.send_keys(self.password)
        time.sleep(1)  # waiting time
        
    def login_button(self):
        # click on login button
        button_login = self.driver.find_element(By.ID, "login-button")
        button_login.click()
        time.sleep(1)  # waiting time
        
    def add_item_to_cart(self):
        # Add item Backpack to the cart
        backpack_to_cart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_to_cart.click()
        time.sleep(1)  # waiting time
        
    def enter_cart_page(self):
        # Enter the cart page
        #button_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        button_cart = self.driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
        button_cart.click()
        time.sleep(1)  # waiting time
        
    def enter_checkout_page(self):
        # Enter checkout page
        button_checkout = self.driver.find_element(By.ID, "checkout")
        button_checkout.click()
        time.sleep(1)  # waiting time
        
    def checkout_enter_first_name(self):
        # Find and fill First Name
        field_first_name = self.driver.find_element(By.ID, "first-name")
        field_first_name.send_keys(self.first_name)
        time.sleep(1)  # waiting time
        
    def checkout_enter_last_name(self):
        # Find and fill Last Name
        field_last_name = self.driver.find_element(By.ID, "last-name")
        field_last_name.send_keys(self.last_name)
        time.sleep(1)  # waiting time
        
    def checkout_enter_postal_code(self):
        # Find and fill First Name, Last Name and Postal code
        field_postal_code = self.driver.find_element(By.ID, "postal-code")
        field_postal_code.send_keys(self.post_code)
        time.sleep(1)  # waiting time
    
    def enter_overview_page(self):
        # click on Continute button and enter overview page
        button_login = self.driver.find_element(By.ID, "continue")
        button_login.click()
        time.sleep(5)  # Wait to see checkout overview
    
    def finish_button(self):
        # click on Finish button
        button_finish = self.driver.find_element(By.ID, "finish")
        button_finish.click()
        time.sleep(3)  # Wait to see result
        
    def driver_quit(self):
        self.driver.quit()
        
          
def do_smoke_test(test: ItemOrderSmokeTest):
    test.initialize_webdriver()
    test.login_enter_user_name()
    test.login_enter_password()
    test.login_button()
    test.add_item_to_cart()
    test.enter_cart_page()
    test.enter_checkout_page()
    test.checkout_enter_first_name()
    test.checkout_enter_last_name()
    test.checkout_enter_postal_code()
    test.enter_overview_page()
    test.finish_button()
    test.driver_quit()
    
if __name__ == "__main__":
        
    user1 = ItemOrderSmokeTest(user_name="standard_user", password="secret_sauce", first_name="Petr", last_name="Safarik", post_code="10900")
    do_smoke_test(user1)

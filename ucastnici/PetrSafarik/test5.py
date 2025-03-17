from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class ItemOrderViewController:
    def __init__(self):

        self.driver = webdriver.Firefox()
        
    def initialize_webdriver(self):
        # launch the saucedemo page
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(1)  # waiting time
        
    def login_enter_user_name(self, user_name ):
        # Find and fill username field
        field_username = self.driver.find_element(By.ID, "user-name")
        field_username.send_keys(user_name)
        time.sleep(1)  # waiting time

    def login_enter_password(self, password):    
        # Find and fill password field
        field_password = self.driver.find_element(By.ID, "password")
        field_password.send_keys(password)
        time.sleep(1)  # waiting time
        
    def login_button(self):
        # click on login button
        button_login = self.driver.find_element(By.ID, "login-button")
        button_login.click()
        time.sleep(1)  # waiting time
    
    def login_error_message(self):
        # Enter the cart page
        error_message = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']//h3[@data-test='error']")
        return error_message.text

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
        
    def checkout_enter_first_name(self, first_name):
        # Find and fill First Name
        field_first_name = self.driver.find_element(By.ID, "first-name")
        field_first_name.send_keys(first_name)
        time.sleep(1)  # waiting time
        
    def checkout_enter_last_name(self, last_name):
        # Find and fill Last Name
        field_last_name = self.driver.find_element(By.ID, "last-name")
        field_last_name.send_keys(last_name)
        time.sleep(1)  # waiting time
        
    def checkout_enter_postal_code(self, postal_code):
        # Find and fill First Name, Last Name and Postal code
        field_postal_code = self.driver.find_element(By.ID, "postal-code")
        field_postal_code.send_keys(postal_code)
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
        
          
def do_smoke_test_correct_login(controller: ItemOrderViewController):
    controller.initialize_webdriver()
    controller.login_enter_user_name("standard_user")
    controller.login_enter_password("secret_sauce")
    controller.login_button()
    controller.add_item_to_cart()
    controller.enter_cart_page()
    controller.enter_checkout_page()
    controller.checkout_enter_first_name("Petr")
    controller.checkout_enter_last_name("Safarik")
    controller.checkout_enter_postal_code("10900")
    controller.enter_overview_page()
    controller.finish_button()
    controller.driver_quit()

def do_smoke_test_incorrect_user_name(controller: ItemOrderViewController):
    controller.initialize_webdriver()
    controller.login_enter_user_name("incorrect_user_name")
    controller.login_enter_password("secret_sauce")
    controller.login_button()
    error_message = controller.login_error_message()
    if error_message != "Epic sadface: Username and password do not match any user in this service":
        print("do_smoke_test_incorrect_user_name: Test failed - incorrect error message.")

def do_smoke_test_incorrect_password(controller: ItemOrderViewController):
    controller.initialize_webdriver()
    controller.login_enter_user_name("standard_user")
    controller.login_enter_password("incorrect_password")
    controller.login_button()
    error_message = controller.login_error_message()
    if error_message != "Epic sadface: Username and password do not match any user in this service!":
        print("do_smoke_test_incorrect_password: Test failed - incorrect error message.")


if __name__ == "__main__":      
    item_order_view_controller = ItemOrderViewController()
    do_smoke_test_incorrect_user_name(item_order_view_controller)
    do_smoke_test_incorrect_password(item_order_view_controller)
    do_smoke_test_correct_login(item_order_view_controller)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time

from functools import wraps
from functools import partial

class ItemOrderViewController:
   
    def initialize_webdriver(self, url):
        self.driver = webdriver.Firefox()
        try:
            self.driver.get(url)
        except WebDriverException as e:
            return False
        time.sleep(1)  # waiting time
        return True
       
    def login_enter_user_name(self, user_name):
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
        try:
            error_message = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']//h3[@data-test='error']")
        except WebDriverException as e:
            return ""
        return error_message.text

    def add_item_to_cart(self):
        # Add item Backpack to the cart
        backpack_to_cart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_to_cart.click()
        time.sleep(1)  # waiting time
    
    def get_number_of_items_in_cart(self):
        try:
            number = self.driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']")
        except WebDriverException as e:
            return ""
        return number.text
        
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


class TestCaseRunner:
    def __init__(self):
        self.test_cases = []

    def register_test_case(self, test_case):
        self.test_cases.append(test_case)

    def run_test_cases(self):
        for test_case in self.test_cases:
            try:
                test_case()
                print("- passed")
            except AssertionError as e:
                print("- failed")
                print("- Assertion failed: " + str(e))
            except Exception as e:
                print("- failed")
                print(e)

def test_case(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Executing: ' + f.__name__)
        try:
            result = f(*args, **kwds)
        except:
            raise
        finally:
            args[0].driver_quit()
        return result
    return wrapper


@test_case
def do_smoke_test_order_item(controller: ItemOrderViewController):
    is_webdriver_initialized = controller.initialize_webdriver("https://www.saucedemo.com/")
    assert is_webdriver_initialized, "Cannot open webpage"
    controller.login_enter_user_name("standard_user")
    controller.login_enter_password("secret_sauce")
    controller.login_button()
    error_message = controller.login_error_message()
    assert error_message == "", "incorrect error message"
    number = controller.get_number_of_items_in_cart()
    assert number == "", "wrong number of items in cart"
    controller.add_item_to_cart()
    number = controller.get_number_of_items_in_cart()
    assert number == "1", "wrong number of items in cart"
    controller.enter_cart_page()
    controller.enter_checkout_page()
    controller.checkout_enter_first_name("Petr")
    controller.checkout_enter_last_name("Safarik")
    controller.checkout_enter_postal_code("10900")
    controller.enter_overview_page()
    controller.finish_button()

@test_case
def do_test_incorrect_user_name(controller: ItemOrderViewController):
    is_webdriver_initialized = controller.initialize_webdriver("https://www.saucedemo.com/")
    assert is_webdriver_initialized, "Cannot open webpage"
    controller.login_enter_user_name("incorrect_user_name")
    controller.login_enter_password("secret_sauce")
    controller.login_button()
    error_message = controller.login_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service", "incorrect error message"

@test_case
def do_test_incorrect_password(controller: ItemOrderViewController):
    is_webdriver_initialized = controller.initialize_webdriver("https://www.saucedemo.com/")
    assert is_webdriver_initialized, "Cannot open webpage"
    controller.login_enter_user_name("standard_user")
    controller.login_enter_password("incorrect_password")
    controller.login_button()
    error_message = controller.login_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service", "incorrect error message"

@test_case
def do_test_incorrect_url(controller: ItemOrderViewController):
    is_webdriver_initialized = controller.initialize_webdriver("https://www.saucedemo.cz/")
    assert is_webdriver_initialized == False, "Cannot open webpage"


if __name__ == "__main__":    
    runner = TestCaseRunner() 
    test_cases_for_execution = [do_smoke_test_order_item, do_test_incorrect_user_name, do_test_incorrect_password, do_test_incorrect_url] 
    
    for test_case in test_cases_for_execution:
        item_order_view_controller = ItemOrderViewController()
        a = partial(test_case, item_order_view_controller)
        runner.register_test_case(a)

    runner.run_test_cases()
    
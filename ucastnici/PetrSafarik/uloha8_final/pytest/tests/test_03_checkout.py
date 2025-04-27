from selenium import webdriver
import sys
import logging
import pytest

sys.path.append('../')
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')


class TestCheckout:
    class_name = "TestCheckout"
    file_handler = logging.FileHandler(f"{class_name}_debug_logs.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)   
    
    @pytest.fixture(params=["firefox", "edge"])
    def browser(self, request):
        browser = request.param
        if browser == "firefox":
            driver = webdriver.Firefox()    
        elif browser == "edge":
            driver = webdriver.Edge()
            
        return driver
    
    @pytest.fixture()
    def item_in_cart(self, browser):
        driver = browser
        login_page = LoginPage(driver)
        login_page.open_page("https://www.saucedemo.com/")
        login_page.enter_user_name("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart()
        inventory_page.enter_cart_page()
        yield driver
        driver.close()
        driver.quit()

    # @pytest.fixture()
    # def user_is_logged_on(self, browser):
    #     driver = browser
    #     login_page = LoginPage(driver)
    #     login_page.open_page("https://www.saucedemo.com/")
    #     login_page.enter_user_name("standard_user")
    #     login_page.enter_password("secret_sauce")
    #     login_page.click_login_button()
        
    #     # return driver
        
    # @pytest.fixture()
    # def item_in_cart(self, user_is_logged_on):
    #     driver = user_is_logged_on
    #     inventory_page = InventoryPage(driver)
    #     inventory_page.add_item_to_cart()
    #     inventory_page.enter_cart_page()
        
    #     yield driver
    #     driver.close()
    #     driver.quit()
        
    def test_checkout(self, item_in_cart):
        driver = item_in_cart
        checkout_page = CheckoutPage(driver) 
        checkout_page.enter_checkout_page()
        checkout_page.check_checkout_page()
        checkout_page.checkout_enter_first_name("Petr")
        checkout_page.checkout_enter_last_name("Safarik")
        checkout_page.checkout_enter_postal_code("10900")
        checkout_page.enter_overview_page()

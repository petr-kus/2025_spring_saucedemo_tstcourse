from selenium import webdriver
import sys
import logging
import pytest

sys.path.append('../')
from uloha8_final.pages.login_page import LoginPage
from uloha8_final.pages.inventory_page import InventoryPage

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')


class TestAddToCart:
    class_name = "TestAddToCart"
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
    def user_is_logged_on(self, browser):
        driver = browser
        login_page = LoginPage(driver)
        login_page.open_page("https://www.saucedemo.com/")
        login_page.enter_user_name("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        
        yield driver
        
        driver.close()
        driver.quit()

    def test_add_to_cart(self, user_is_logged_on):
        driver = user_is_logged_on
        inventory_page = InventoryPage(driver)
        inventory_page.check_product_page()
        assert inventory_page.get_number_of_items_in_cart() == "", "wrong number of items in cart"
        inventory_page.add_item_to_cart()  # jak tady zadat polozku rucne??
        number = inventory_page.get_number_of_items_in_cart()
        assert number == "1", "wrong number of items in cart"
        inventory_page.enter_cart_page()
        inventory_page.check_cart_page()

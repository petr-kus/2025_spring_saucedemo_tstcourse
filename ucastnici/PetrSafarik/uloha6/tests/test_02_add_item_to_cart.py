from selenium import webdriver
import sys
import logging
import pytest

sys.path.append('../')
from uloha6.pages.login_page import LoginPage
from uloha6.pages.inventory_page import InventoryPage

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')


class TestAddToCart:
    class_name = "TestAddToCart"
    file_handler = logging.FileHandler(f"{class_name}_debug_logs.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    @pytest.fixture()
    def fixture(self):
        driver = webdriver.Firefox()
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.enter_user_name()
        login_page.enter_password()
        login_page.click_login_button()
        expected_title_products = "Products"
        expected_title_cart = "Your Cart"

        yield driver, expected_title_products, expected_title_cart
        driver.close()
        driver.quit()

    def test_add_to_cart(self, fixture):
        driver, expected_title_products, expected_title_cart = fixture
        inventory_page = InventoryPage(driver)
        assert inventory_page.check_page() == expected_title_products, "Title mismatch"
        number = inventory_page.get_number_of_items_in_cart()
        assert number == "", "wrong number of items in cart"
        inventory_page.add_item_to_cart()
        number = inventory_page.get_number_of_items_in_cart()
        assert number == "1", "wrong number of items in cart"
        inventory_page.enter_cart_page()
        assert inventory_page.check_page() == expected_title_cart, "Title mismatch"

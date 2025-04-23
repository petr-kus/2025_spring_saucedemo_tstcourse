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

        #TODO: Lektor - zde bych to urcite nepsal vsechno do jedne fixture! Pouzil bych vice fixtures. Bud by metoda primo potreboval vice fixtures.
        # A nebo by tam byl strom vzajemne zavislych fixtures.
        # jedna by byla browser (a byla by spolecna pro vice test souboru - nacitala by se nekde v importech)
        # druha by byla v podstate precondition "User_is_logged_on(browser, username, password)"
        # test_add_to_cart by pak zral user_is_logged_on

    def test_add_to_cart(self, fixture):
        driver, expected_title_products, expected_title_cart = fixture
        inventory_page = InventoryPage(driver)

        assert inventory_page.check_page() == expected_title_products, "Title mismatch"
        #TODO: Tady se to v podstate kontroluje na spatnem levelu. Bud to zde rovnou muze byt uvedeno a nebo to muze byt schovano uvnitr?

        number = inventory_page.get_number_of_items_in_cart()
        assert number == "", "wrong number of items in cart"
        #TODO: Uvazoval bych o zkraceni na one liner 
        #assert inventory_page.get_number_of_items_in_cart() == "", "wrong number of items in cart"

        inventory_page.add_item_to_cart()
        #TODO: tady se dela volba uvnitr, zviditelnil bych ji ven do test casu

        number = inventory_page.get_number_of_items_in_cart()
        assert number == "1", "wrong number of items in cart"

        inventory_page.enter_cart_page()
        assert inventory_page.check_page() == expected_title_cart, "Title mismatch"
        #TODO: Tady se to v podstate kontroluje na spatnem levelu. Bud to zde rovnou muze byt uvedeno a nebo to muze byt schovano uvnitr?

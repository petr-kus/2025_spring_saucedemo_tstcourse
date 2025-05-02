from Utils.logger import setup_logging
import logging

setup_logging("test_TAC-T6_u8")
logger = logging.getLogger()

logger.info("Spouští se testování.")

import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.product_page import InventoryPage
from Config import config

@pytest.fixture(params=config.CREDENTIALS.items(), scope="function")
def driver_logged_in(request):
    username, password = request.param

    if config.BROWSER.lower() == "edge":
        driver = webdriver.Edge()
    elif config.BROWSER.lower() == "chrome":
        driver = webdriver.Chrome()
    elif config.BROWSER.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {config.BROWSER}")
    
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(username, password)

    yield driver

    driver.quit()

def test_inventory_and_product_details(driver_logged_in):

    logger.info("Testování detailů produktů začíná.")

    inventory_page = InventoryPage(driver_logged_in)
    products = inventory_page.get_inventory_items()

    for product in products:
        inventory_page.click_product_by_name(product['name'])

        inventory_page.verify_product_detail(
            expected_name=product['name'],
            expected_price=product['price'],
            expected_img=product['img']
        )

        driver_logged_in.back()
        inventory_page.wait_for_element(inventory_page.INVENTORY_ITEMS)
        


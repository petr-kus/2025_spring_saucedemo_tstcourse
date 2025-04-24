from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import wait_for_element
import os
from saucedemo.LoginPage import LoginPage
from saucedemo.InventoryPage import InventoryPage
import pytest
import logging

logging.basicConfig(
    filename='log_jt_test_add_item_to_cart.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Logging setup successfully!")
test_page = "https://www.saucedemo.com/"
valid_user = 'standard_user'
user_password = "secret_sauce"

@pytest.fixture(autouse=True, scope="session")
def edgeBrowser():
    global browser
    browser = webdriver.Edge()
    browser.get(test_page)
    yield browser
    browser.quit()

@pytest.fixture
def username():
    return valid_user

@pytest.fixture
def password():
    return user_password

#TEST CASE
def test_cart_badge_behavior(username, password):
    """Put random amount of items into cart and check its volume."""
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    login_page.login_user(username, password)
    wait_for_element(browser, 2, (By.CLASS_NAME, 'title'))
    inventory_page.we_are_on_page()
    inventory_page.verify_login()
    wait_for_element(browser, 2, (By.CLASS_NAME, 'title'))
    inventory_page.add_random_products_to_cart()

  
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

from web_saucedemo.LoginPage import LoginPage
from web_saucedemo.Logout import Logout
from web_saucedemo.InventoryAddCart import CartPage

page_url =  'https://www.saucedemo.com/'
page_username = "standard_user"
page_password = "secret_sauce"


@pytest.fixture( scope='session')
def browser():
    driver = webdriver.Firefox()
    driver.get(page_url)
    yield driver
    driver.quit()

@pytest.fixture
def username():
    return page_username

@pytest.fixture
def password():
    return page_password

def wait_for(driver,locator, timeout=2):
    web_driver_wait = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    return web_driver_wait

def slowdown(timeout=5):
    time.sleep(timeout)


# test case
def test_login_user(username, password, browser):
    test_page = LoginPage(browser)
    test_page.login(username,password)
    slowdown()

def test_add_item_on_cart(browser):
    test_page = CartPage(browser)
    test_page.add_random_item_to_cart()
    cart_count = test_page.get_cart_item_count()
    remove_count = test_page.get_remove_buttons_count()
    assert cart_count == remove_count,(
        f"Počet položek v košíku ({cart_count}) se neshoduje "
        f"s počtem REMOVE tlačítek ({remove_count})"
    )
    test_page.clear_cart()

def test_menu_page(browser):
    test_page = Logout(browser)
    test_page.logout()

    

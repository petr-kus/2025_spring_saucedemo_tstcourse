import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from saucedemo.LoginPage import LoginPage
from saucedemo.InventoryPage import InventoryPage
from saucedemo.Menu import Menu

USERNAME = "standard_user"
PASSWORD = "secret_sauce"
URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="session", autouse=True)
def Browser():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get(URL)
    yield driver
    driver.quit()

def slowdown():
    time.sleep(1)

def test_login_user(Browser):
    login_page = LoginPage(Browser)
    inventory_page = InventoryPage(Browser)

    login_page.login_user(USERNAME, PASSWORD)
    slowdown()
    inventory_page.we_are_on_page()

def test_logout_user(Browser):
    menu = Menu(Browser)
    login_page = LoginPage(Browser)

    menu.open_menu()
    slowdown()
    menu.press_logout()
    slowdown()
    login_page.we_are_on_page()

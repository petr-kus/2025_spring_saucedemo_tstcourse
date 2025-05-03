from selenium import webdriver
from selenium.webdriver.common.by import By
from utils_pytest.utils import wait_for_element
import os
from saucedemo.LoginPage import LoginPage
from saucedemo.InventoryPage import InventoryPage
from saucedemo.Menu import Menu
import pytest
import logging

logging.basicConfig(filename='log_jt_test_login_v3.log', level=logging.INFO)
logging.info("Logging setup successfully!")

# print("Current working directory:", os.getcwd())

test_page = "https://www.saucedemo.com/"
valid_user = 'standard_user'
invalid_users = ['locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
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

# if not os.path.exists("screenshots"):
#     os.makedirs("screenshots")

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_call(item):
#     """Pytest hook to take a screenshot on test failure."""
#     outcome = yield
#     if outcome.excinfo is not None:  
#         test_name = item.name  
#         screenshot_path = f"screenshots/{test_name}_failure.png"
#         try:
#             browser.get_screenshot_as_file(screenshot_path)  
#             print(f"Screenshot saved: {screenshot_path}")
#         except Exception as e:
#             print(f"Failed to capture screenshot: {e}")

#TEST CASES
def pytest_html_report_title(report):
    report.title = "test_login_v3.py report"

def test_login_the_user(username, password):
    """Check that user can be logged in."""
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    login_page.login_user(username, password)
    wait_for_element(browser, 2, (By.CLASS_NAME, 'title'))
    inventory_page.we_are_on_page()
    inventory_page.verify_login()

def test_logout_the_user():
    """Check that user can be logged out."""
    menu_bar = Menu(browser)
    login_page = LoginPage(browser)
    wait_for_element(browser, 2, (By.CLASS_NAME, 'title'))
    menu_bar.open_menu()
    wait_for_element(browser, 2, (By.CLASS_NAME, 'title'))
    menu_bar.press_logout()
    wait_for_element(browser, 2, (By.CLASS_NAME, 'login_logo'))
    login_page.we_are_on_page()
    login_page.verify_logout()

# log_path = 'log_jt_test_login_v3.log'
# if os.path.exists(log_path):
#     print("Log file created:", log_path)
# else:
#     print("Log file not found:", log_path)
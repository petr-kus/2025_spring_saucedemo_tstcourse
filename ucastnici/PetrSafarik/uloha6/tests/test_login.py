from selenium import webdriver
import sys
import logging
import pytest
import pytest_html

sys.path.append('../')
from pages.login_page import LoginPage

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class TestLoginPage:

    @pytest.fixture()
    def fixture(self):
        driver = webdriver.Chrome()
        url = "https://www.saucedemo.com/"
        user_name = "standard_user"
        password = "secret_sauce"
        expected_title = "Swag Labs"
        yield driver, url, user_name, password, expected_title
        driver.close()
        driver.quit()

    def test_login(self, fixture):
        driver, url, user_name, password, expected_title = fixture
        login_page = LoginPage(driver)
        actual_title = login_page.open_page(url)
        assert actual_title == expected_title, "Title mismatch"

        login_page.enter_user_name(user_name)
        login_page.enter_password(password)
        login_page.click_login_button()
        assert login_page.login_error_message() == "", "Login failed."

    def test_login_invalid_password(self, fixture):
        driver, url, user_name, password, expected_title = fixture
        password = "wrong_password"
        login_page = LoginPage(driver)
        actual_title = login_page.open_page(url)
        assert actual_title == expected_title, "Title mismatch"
        login_page.enter_user_name(user_name)
        login_page.enter_password(password)
        login_page.click_login_button()
        assert login_page.login_error_message() == "Epic sadface: Username and password do not match any user in this service", "incorrect error message"

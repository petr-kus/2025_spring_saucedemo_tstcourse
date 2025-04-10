from selenium import webdriver
import sys
import logging
import pytest

sys.path.append('../')
from uloha6.pages.login_page import LoginPage

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')


class TestLoginPage:
    class_name = "TestLoginPage"
    file_handler = logging.FileHandler(f"{class_name}_debug_logs.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    @pytest.fixture()
    def fixture(self):
        driver = webdriver.Chrome()
        expected_title = "Swag Labs"
        yield driver, expected_title
        driver.close()
        driver.quit()

    def test_login(self, fixture):
        driver, expected_title = fixture
        login_page = LoginPage(driver)
        login_page.open_page()
        assert login_page.open_page() == expected_title, "Title mismatch"
        login_page.enter_user_name()
        login_page.enter_password()
        login_page.click_login_button()
        assert login_page.login_error_message() == "", "Login failed."

    def test_login_invalid_password(self, fixture):
        driver, expected_title = fixture
        login_page = LoginPage(driver)
        assert login_page.open_page() == expected_title, "Title mismatch"
        login_page.enter_user_name()
        login_page.enter_invalid_password()
        login_page.click_login_button()
        assert login_page.login_error_message() == ("Epic sadface: Username and password do not match any user "
                                                    "in this service"), "incorrect error message"

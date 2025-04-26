from selenium import webdriver
import sys
import logging
import pytest

sys.path.append('../')
from uloha8_final.pages.login_page import LoginPage
# from uloha8_final.fixtures.fixtures import browsers

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

class TestLoginPage:
    class_name = "TestLoginPage"
    file_handler = logging.FileHandler(f"{class_name}_debug_logs.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    
    # @pytest.fixture()
    # def driver(self, browsers):
    #     driver = browsers

    #     yield driver

    #     driver.close()
    #     driver.quit()
    
    @pytest.fixture(params=["firefox", "edge"])
    def driver(self, request):
        browser = request.param
        if browser == "firefox":
            driver = webdriver.Firefox()    
        elif browser == "edge":
            driver = webdriver.Edge()

        yield driver

        driver.close()
        driver.quit()

    @pytest.mark.parametrize("user, password", [("standard_user", "secret_sauce"), ("standard_user", "Wrong_password")])
    def test_login(self, driver, user, password):
        login_page = LoginPage(driver)
        
        expected_title = "Swag Labs"
        assert login_page.open_page("https://www.saucedemo.com/") == expected_title, "Title mismatch"

        login_page.enter_user_name(user)
        login_page.enter_password(password)
        login_page.click_login_button()
        
        if user == "standard_user" and password == "secret_sauce":
            # correct login
            assert login_page.login_error_message() == "", "Login failed."
        else:
            # incorrect password
            assert login_page.login_error_message() == ("Epic sadface: Username and password do not match any user "
                                                    "in this service"), "incorrect error message"

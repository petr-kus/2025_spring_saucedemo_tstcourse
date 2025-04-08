import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webtest.loginpage import Login
import logging

class LoginTest(unittest.TestCase):

    WEB_URL = "https://www.saucedemo.com/"
    USER_NAME = "standard_user"
    PASSWORD = "secret_sauce"

    def setUp(self):
        logging.info("Zahájení testu")
        self.options = Options()
        self.driver = webdriver.Firefox(options=self.options)
        self.login_page = Login(self.driver)

    def test_successful_login(self):
        logging.info("Test: úspěšné přihlášení")
        self.login_page.open_browser(self.WEB_URL)
        self.login_page.login(self.USER_NAME, self.PASSWORD)
        self.assertIn("inventory", self.driver.current_url)

    def tearDown(self):
        logging.info("Ukončení testu a zavření prohlížeče")
        self.driver.quit()

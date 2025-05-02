from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException  
from selenium import webdriver

class LoginPage:
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    submit_button = (By.ID, "login-button")
    page_url = "https://www.saucedemo.com/"
    expected_title = "Swag Labs"

    def open_page(self,url):
        browser = webdriver.Firefox()
        self.driver = browser
        self.driver.get(url)

    def is_correct_page(self):
        assert self.page_url == self.driver.current_url, f"We are not on the right page '{self.page_url}'"

    def check_title(self):
        actual_title = self.driver.title
        assert actual_title == self.expected_title, "Title mismatch"          
        
    def enter_user_name(self, user_name):
        self.driver.find_element(*self.username_field).send_keys(user_name)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.submit_button).click()

    def login_error_message(self):
        try:
            error_message = self.driver.find_element(*self.error_message)
        except WebDriverException as e:
            return ""
        return error_message.text
        
    def is_user_logged(self):
        assert "inventory" in self.driver.current_url, f"Expected 'inventory' in url, but in url '{self.driver.current_url}' was not found."
 
    def close_driver(self):
        self.driver.close()
        self.driver.quit()
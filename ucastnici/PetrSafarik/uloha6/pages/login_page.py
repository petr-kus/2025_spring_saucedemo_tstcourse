from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "user-name")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//div[@id='login_button_container']//h3[@data-test='error']")
    
    def open_page(self, url):
        self.driver.get(url)
        actual_title = self.driver.title
        return actual_title

    def enter_user_name(self, user_name):
        self.driver.find_element(*self.username_textbox).send_keys(user_name)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login_error_message(self):
        try:
            error_message = self.driver.find_element(*self.error_message)
        except WebDriverException as e:
            return ""
        return error_message.text

from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME_INPUT_LOCATOR = (By.ID, 'user-name')
    PASSWORD_INPUT_LOCATOR = (By.ID, 'password')
    LOGIN_BUTTON_LOCATOR = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver

    @property
    def username_input(self):
        return self.driver.find_element(*self.USERNAME_INPUT_LOCATOR)
    
    @property
    def password_input(self):
        return self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR)
    
    @property
    def login_button(self):
        return self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
    
    


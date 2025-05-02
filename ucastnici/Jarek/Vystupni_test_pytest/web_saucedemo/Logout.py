from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logout:
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    @property
    def menu_button(self):
        return self.driver.find_element(*self.MENU_BUTTON)

    @property
    def logout_button(self):
        return self.driver.find_element(*self.LOGOUT_BUTTON)

    def open_menu(self):
        self.menu_button.click()

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON)
        )
        self.logout_button.click()

    def logout(self):
        self.open_menu()
        self.click_logout()

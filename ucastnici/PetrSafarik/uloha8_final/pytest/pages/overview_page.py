from selenium.webdriver.common.by import By


class OverviewPage:
    
    page_title = (By.XPATH, "//span[@data-test='title']")
    expected_title_checkout = "Checkout: Overview"
    press_finish_button = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
       
    def check_checkout_page(self):
        actual_cart_page_title = self.driver.find_element(*self.page_title).text
        assert actual_cart_page_title == self.expected_title_checkout, "Title mismatch"  
    
    def enter_complete_page(self):
        button_login = self.driver.find_element(*self.press_finish_button)
        button_login.click()
        
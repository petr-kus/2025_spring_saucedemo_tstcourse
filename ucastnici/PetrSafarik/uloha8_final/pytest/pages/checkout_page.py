from selenium.webdriver.common.by import By


class CheckoutPage:
    
    page_title = (By.XPATH, "//span[@data-test='title']")

    enter_the_checkout = (By.ID, "checkout")
    enter_first_name = (By.ID, "first-name")
    enter_last_name = (By.ID, "last-name")
    enter_postal_code = (By.ID, "postal-code")
    expected_title_checkout = "Checkout: Your Information"
    enter_overview_page_button = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def enter_checkout_page(self):
        button_checkout = self.driver.find_element(*self.enter_the_checkout)
        button_checkout.click()
        
    def check_checkout_page(self):
        actual_cart_page_title = self.driver.find_element(*self.page_title).text
        assert actual_cart_page_title == self.expected_title_checkout, "Title mismatch"  
    
    def checkout_enter_first_name(self, first_name):
        field_first_name = self.driver.find_element(*self.enter_first_name)
        field_first_name.send_keys(first_name)
        
    def checkout_enter_last_name(self, last_name):
        field_last_name = self.driver.find_element(*self.enter_last_name)
        field_last_name.send_keys(last_name)
        
    def checkout_enter_postal_code(self, postal_code):
        field_postal_code = self.driver.find_element(*self.enter_postal_code)
        field_postal_code.send_keys(postal_code)
    
    def enter_overview_page(self):
        button_login = self.driver.find_element(*self.enter_overview_page_button)
        button_login.click()
        
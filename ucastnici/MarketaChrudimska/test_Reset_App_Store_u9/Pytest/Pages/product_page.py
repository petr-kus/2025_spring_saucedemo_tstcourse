from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class ProductPage(BasePage):
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    RESET_BUTTON = (By.ID, "reset_sidebar_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def click_cart_button(self, product_id):
        add_id = f"add-to-cart-{product_id}"
        remove_id = f"remove-{product_id}"
        try:
            button = self.driver.find_element(By.ID, remove_id)
            button.click()
        except:
            try:
                button = self.driver.find_element(By.ID, add_id)
                button.click()
            except Exception as e:
                logger.error(f"❌ Tlačítko add ani remove pro produkt {product_id} nebylo nalezeno: {e}")


    def get_cart_count(self):
        elements = self.driver.find_elements(*self.CART_BADGE)
        return elements[0].text if elements else "0"

    def reset_app_state(self):
        self.click(self.MENU_BUTTON)
        self.click(self.RESET_BUTTON)
   
    def get_cart_button_text(self, product_id):
        button = self.driver.find_elements(By.ID, f"add-to-cart-{product_id}")
        if button:
            return button[0].text
        button = self.driver.find_elements(By.ID, f"remove-{product_id}")
        if button:
            return button[0].text
        return None
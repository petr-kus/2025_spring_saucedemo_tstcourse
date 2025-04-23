import logging
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

logger = logging.getLogger(__name__)

class InventoryPage(BasePage):
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_IMG = (By.CSS_SELECTOR, ".inventory_item_img img")

    DETAIL_NAME = (By.CLASS_NAME, "inventory_details_name")
    DETAIL_PRICE = (By.CLASS_NAME, "inventory_details_price")
    DETAIL_IMG = (By.CLASS_NAME, "inventory_details_img")

    def get_inventory_items(self):
        self.wait_for_element(self.INVENTORY_ITEMS)
        logger.info("Načítání produktů z inventáře.")

        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        product_data = []

        for item in items:
            name = item.find_element(*self.ITEM_NAME).text
            price = item.find_element(*self.ITEM_PRICE).text
            img_url = item.find_element(*self.ITEM_IMG).get_attribute("src")
            logger.info(f"Produkt nalezen: {name} | {price} | {img_url}")

            product_data.append({
                'name': name,
                'price': price,
                'img': img_url,
                'element': item.find_element(*self.ITEM_NAME)
            })

        logger.info(f"✅ Načteno {len(product_data)} produktů.")
        print(f"✅ Načteno {len(product_data)} produktů.")
        return product_data
    
    def click_product_by_name(self, product_name):
        self.wait_for_element(self.INVENTORY_ITEMS)
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)

        for item in items:
            name_element = item.find_element(*self.ITEM_NAME)
            if name_element.text == product_name:
                name_element.click()
                logger.info(f"Kliknuto na produkt: {product_name}")
                return
        logger.error(f"❌ Produkt '{product_name}' nebyl nalezen.")
        raise Exception(f"Produkt '{product_name}' nebyl nalezen.")

    def verify_product_detail(self, expected_name, expected_price, expected_img):
        logger.info(f"Ověřuji detail produktu: {expected_name}")
    
        actual_name = self.get_text(self.DETAIL_NAME)
        actual_price = self.get_text(self.DETAIL_PRICE)
        actual_img = self.driver.find_element(*self.DETAIL_IMG).get_attribute("src")

        logger.debug(f"Název: očekávaný '{expected_name}' | aktuální '{actual_name}'")
        logger.debug(f"Cena: očekávaná '{expected_price}' | aktuální '{actual_price}'")
        logger.debug(f"Obrázek: očekávaný '{expected_img}' | aktuální '{actual_img}'")
   
        test_passed = True

        # Test pro název
        try:
            assert actual_name == expected_name, f"Název se neshoduje: očekávaný '{expected_name}', aktuální '{actual_name}'"
        except AssertionError as e:
            logger.error(f"❌ Test selhal u nazvu produktu: {e}")
            print(f"❌ Test selhal u názvu produktu: {e}")
            test_passed = False

        # Test pro cenu
        try:
            assert actual_price == expected_price, f"Cena se neshoduje: očekávaná '{expected_price}', aktuální '{actual_price}'"
        except AssertionError as e:
            logger.error(f"❌ Test selhal u ceny produktu: {e}")
            print(f"❌ Test selhal u ceny produktu: {e}")
            test_passed = False

        # Test pro obrázek
        try:
            assert actual_img == expected_img, f"Obrázek se neshoduje.\nOčekávaný: {expected_img}\nAktuální:   {actual_img}"
        except AssertionError as e:
            logger.error(f"❌ Test selhal u obrazku produktu: {e}")
            print(f"❌ Test selhal u obrázku produktu: {e}")
            test_passed = False

        if test_passed:
            logger.info(f"✅ Detail produktu '{expected_name}' je v poradku.")
            print(f"✅ Detail produktu '{expected_name}' je v pořádku.")

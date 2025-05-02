from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time
import random
import logging
import os
from datetime import datetime

test_page = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"

class Locators:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    INVENTORY_CONTAINER = (By.CLASS_NAME, "inventory_container")

    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[starts-with(@data-test, 'add-to-cart')]")
    REMOVE_BUTTONS = (By.XPATH, "//button[starts-with(@data-test, 'remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")

def setup_logger():
    log_dir = "ucastnici/Dasa/logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"test_errors_{current_time}.log")
    
    logger = logging.getLogger("saucedemo_test")
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()

def setup_browser(test_page):
    try:
        driver = webdriver.Chrome()
        driver.get(test_page)
        logger.info("Page loaded successfully")
        return driver
    except Exception as e:
        logger.error(f"Error loading page: {str(e)}")
        return None

def login(driver, username, password):
    try:
        logger.info(f"Attempting to login user: {username}")
        
        driver.find_element(*Locators.USERNAME_FIELD).send_keys(username)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.INVENTORY_CONTAINER)
        )
        logger.info("Login successful")
        return True

    except TimeoutException:
        logger.error("Login failed - timeout")
        return False
    except NoSuchElementException as e:
        logger.error(f"Login failed - element not found: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        return False

def add_items_to_cart(driver):
    try:
        logger.info("Starting to add products to cart")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ADD_TO_CART_BUTTONS)
        )
        #TODO - Lektor - toto explicitini cekani zde nema smysl vzhledem k defaultni load strategy, ktere ceka na nacteni stranky (takze to tam uz je kdyz bezi tento kod). 

        buttons_add_to_cart = driver.find_elements(*Locators.ADD_TO_CART_BUTTONS)
        
        if not buttons_add_to_cart:
            logger.warning("No 'Add to Cart' buttons found")
            return

        num_buttons_to_click = random.randint(1, len(buttons_add_to_cart))
        buttons_to_click = random.sample(buttons_add_to_cart, num_buttons_to_click)

        logger.info(f"Total buttons found: {len(buttons_add_to_cart)}")
        logger.info(f"Randomly selected {num_buttons_to_click} buttons to click")

        for button in buttons_to_click:
            try:
                button.click()
                logger.info("Product added to cart")
                time.sleep(0.5)
            except Exception as e:
                logger.error(f"Error clicking button: {str(e)}")

        try:
            cart_count = driver.find_element(*Locators.CART_BADGE).text
            logger.info(f"Items in cart after adding: {cart_count}")
        except:
            logger.warning("No items visible in cart")

    except TimeoutException:
        logger.error("Timeout waiting for 'Add to Cart' buttons")
    except Exception as e:
        logger.error(f"Error adding products to cart: {str(e)}")

def remove_items_from_cart(driver):
    try:
        logger.info("Starting to remove products from cart")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.REMOVE_BUTTONS)
        )

        buttons_remove = driver.find_elements(*Locators.REMOVE_BUTTONS)
        
        if not buttons_remove:
            logger.warning("No 'Remove' buttons found")
            return

        logger.info(f"Found {len(buttons_remove)} items to remove")

        for button in buttons_remove:
            try:
                button.click()
                time.sleep(0.5)
                logger.info("Product removed from cart")
            except Exception as e:
                logger.error(f"Error clicking remove button: {str(e)}")

        logger.info("All items removed from cart")

    except TimeoutException:
        logger.error("Timeout waiting for 'Remove' buttons")
    except Exception as e:
        logger.error(f"Error removing products from cart: {str(e)}")

def main():
    driver = None
    try:
        driver = setup_browser(test_page)
        if not driver:
            logger.error("Test stopped - failed to initialize driver")
            return

        if not login(driver, user_name, password):
            logger.error("Test stopped - login failed")
            return

        time.sleep(3)
        
        add_items_to_cart(driver)
        time.sleep(3)

        remove_items_from_cart(driver)
        time.sleep(3)

        try:
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(Locators.ADD_TO_CART_BUTTON)
            )
            assert button.is_displayed(), "No 'Add to cart' buttons found after removing items"
            logger.info("Test completed successfully - 'Add to cart' buttons are visible")
        except TimeoutException:
            logger.error("Timeout waiting for 'Add to cart' buttons")
        except AssertionError as e:
            logger.error(f"Test failed: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error verifying buttons: {str(e)}")

    except Exception as e:
        logger.error(f"Test failed: {str(e)}")

    finally:
        if driver:
            try:
                driver.quit()
                logger.info("Driver closed successfully")
            except Exception as e:
                logger.error(f"Error closing driver: {str(e)}")

if __name__ == "__main__":
    main()

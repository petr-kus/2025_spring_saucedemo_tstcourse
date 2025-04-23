from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver


def login(driver, username, password):
    try:
        # Zadání přihlašovacích údajů
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        # Kontrola, zda jsme se skutečně přihlásili - čekáme na element, který existuje jen po přihlášení
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_container"))
        )
        print("Login successful!")
        return True

    except Exception as e:
        print(f"Login failed: {e}")
        return False

def add_items_to_cart(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[starts-with(@data-test, 'add-to-cart')]"))
        )

        buttons_add_to_cart = driver.find_elements(By.XPATH, "//button[starts-with(@data-test, 'add-to-cart')]")
        
        if not buttons_add_to_cart:
            print("No 'Add to Cart' buttons found!")
            return

        num_buttons_to_click = random.randint(1, len(buttons_add_to_cart))
        buttons_to_click = random.sample(buttons_add_to_cart, num_buttons_to_click)

        print(f"Total buttons found: {len(buttons_add_to_cart)}")
        print(f"Randomly selected {num_buttons_to_click} buttons to click")

        for button in buttons_to_click:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(button)
            )
            button.click()
            print("Item added to cart.")
            time.sleep(0.5)  # Krátká pauza po přidání položky

        try:
            cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            print(f"Items in cart after adding: {cart_count}")
        except:
            print("No items visible in cart")

    except Exception as e:
        print(f"Error adding items to cart: {e}")

def remove_items_from_cart(driver):
    try:
        # Wait for Remove buttons to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[starts-with(@data-test, 'remove')]"))
        )

        # Find all Remove buttons
        buttons_remove = driver.find_elements(By.XPATH, "//button[starts-with(@data-test, 'remove')]")
        
        if not buttons_remove:
            print("No 'Remove' buttons found!")
            return

        print(f"Found {len(buttons_remove)} items to remove")

        # Click all remove buttons
        for button in buttons_remove:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(button)
            )
            button.click()
            time.sleep(0.5)  # Krátká pauza po odstranění položky
            print("Item removed from cart.")

        print("All items removed from cart")

    except Exception as e:
        print(f"Error removing items from cart: {e}")        

def main():
    driver = setup_browser()
    try:
        # Pokud se přihlášení nepovede, ukončíme test
        if not login(driver, "standard_user", "secret_sauce"):
            print("Test stopped due to failed login")
            return

        time.sleep(3)
        
        add_items_to_cart(driver)
        time.sleep(3)

        remove_items_from_cart(driver)
        time.sleep(3)

        # Kontrola, že se tlačítka Add to cart znovu objevila
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']"))
        )
        assert button.is_displayed(), "No 'Add to cart' button found after removing items."
        print("Test passed: 'Add to cart' buttons are visible again")

    except Exception as e:
        print("Test failed:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
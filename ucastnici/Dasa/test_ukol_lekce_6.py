from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver

def login(driver, username, password):
    try:
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        print("Login successful!")

    except Exception as e:
        print(f"Login failed: {e}")

def add_items_to_cart(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory"))
        )

        button_add_to_cart = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        
        if not button_add_to_cart:
            print("No 'Add to Cart' buttons found!")
            return

        for button in button_add_to_cart:
            button.click()
            print("Item added to cart.")

        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        print(f"Items in cart after adding: {cart_count}")    
        
    except Exception as e:
        print(f"Error adding items to cart: {e}")

def remove_items_from_cart(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory"))
        )

        button_remove = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        
        if not button_remove:
            print("No 'Remove' buttons found!")
            return

        for button in button_remove:
            button.click()
            print("Item removed from cart.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

    except Exception as e:
        print(f"Error removing items from cart: {e}")

def run_test():
    driver = setup_browser()
    try:
        login(driver, "standard_user", "secret_sauce")
        add_items_to_cart(driver)  
        remove_items_from_cart(driver) 

        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']"))
        )
        assert button.is_displayed(), "Žádné tlačítko 'Add to cart' se nenašlo po odstranění zboží."

    except Exception as e:
        print("Test selhal:", e)

    finally:
        driver.quit()

run_test()


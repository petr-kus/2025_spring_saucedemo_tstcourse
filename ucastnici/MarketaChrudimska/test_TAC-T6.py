from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#time.sleep(1)  # Wait for page to load

# Find username and password fields and login button
field_username = driver.find_element(By.ID, "user-name")
# field_username.send_keys("problem_user")
field_username.send_keys("standard_user")

field_password = driver.find_element(By.ID, "password")
field_password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Počkej na načtení stránky
#time.sleep(2)

# Zkontroluj obrázek na stránce inventory.html
try:
    inventory_image = driver.find_element(By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    inventory_image_src = inventory_image.get_attribute("src")
    print("Obrázek na inventory stránce:", inventory_image_src)
except Exception as e:
    print(f"⛔ Chyba při získávání obrázku na stránce inventory: {e}")

# Zkontroluj cenu na stránce inventory.html
try:
    inventory_price = driver.find_element(By.XPATH, "//div[@class='inventory_item'][1]//div[@class='inventory_item_price']")
    inventory_price_text = inventory_price.text
    print("Cena na stránce inventory:", inventory_price_text)
except Exception as e:
    print(f"⛔ Chyba při získávání ceny na stránce inventory: {e}")

# Klikni na odkaz Sauce Labs Backpack
backpack_link = driver.find_element(By.ID, "item_4_title_link")
backpack_link.click()

#time.sleep(1)  # Wait for page to load

# Získáme URL aktuální stránky
current_url = driver.current_url
print("Aktuální URL:", current_url)

# Ověření, že URL odpovídá stránce detailu pro tento produkt
try:
    assert "inventory-item.html?id=4" in current_url, "URL neodpovídá detailu produktu!"
    print("✅ URL odpovídá detailu produktu!")
except AssertionError as e:
    print(f"⛔ Chyba při kontrole URL: {e}")

# Zkontroluj obrázek na stránce inventory-item.html
try:
    detail_image = driver.find_element(By.XPATH, "//img[@class='inventory_details_img']")
    detail_image_src = detail_image.get_attribute("src")
    print("Obrázek na detailu produktu:", detail_image_src)
except Exception as e:
    print(f"⛔ Chyba při získávání obrázku na stránce detailu produktu: {e}")

# Ověření, že obrázky jsou stejné
try:
    assert inventory_image_src == detail_image_src, "Obrázek se neshoduje!"
    print("✅ Obrázek je shodný!")
except AssertionError as e:
    print(f"⛔ Chyba při porovnání obrázků: {e}")

# Zkontroluj cenu na stránce inventory-item.html
try:
    detail_price = driver.find_element(By.CLASS_NAME, "inventory_details_price")
    detail_price_text = detail_price.text
    print("Cena na stránce detailu produktu:", detail_price_text)
except Exception as e:
    print(f"⛔ Chyba při získávání ceny na stránce detailu produktu: {e}")

# Ověření, že ceny jsou stejné
try:
    assert inventory_price_text == detail_price_text, "Cena se neshoduje!"
    print("✅ Cena je shodná!")
except AssertionError as e:
    print(f"⛔ Chyba při porovnání cen: {e}")

time.sleep(2)  # Wait to see result

driver.quit()
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
field_username.send_keys("standard_user")

field_password = driver.find_element(By.ID, "password")
field_password.send_keys("secret_sauce")

button_submit = driver.find_element(By.ID, "login-button")
button_submit.click()

# Find all the "Add to card" buttons and click on all of them
button_add_to_card = driver.find_elements(By.CLASS_NAME, "btn_inventory")

for button in button_add_to_card:
    button.click()

time.sleep(5)  # Wait to see result

# Find all the "Remove" buttons and click on all of them
button_remove = driver.find_elements(By.CLASS_NAME, "btn_inventory")

for button in button_remove:
    button.click()

time.sleep(5)   # Wait to see result
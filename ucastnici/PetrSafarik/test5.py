from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Initialize WebDriver
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

# Find and fill username and password fields and click on login button
field_username = driver.find_element(By.ID, "user-name")
field_username.send_keys("standard_user")

field_password = driver.find_element(By.ID, "password")
field_password.send_keys("secret_sauce")

button_login = driver.find_element(By.ID, "login-button")
button_login.click()

# Add item Backpack to the cart

backpack_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
backpack_to_cart.click()

# Enter the cart

#button_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
button_cart = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
button_cart.click()

# Enter checkout page

button_checkout = driver.find_element(By.ID, "checkout")
button_checkout.click()

# Find and fill First Name, Last Name and Postal code

field_first_name = driver.find_element(By.ID, "first-name")
field_first_name.send_keys("Petr")

field_second_name = driver.find_element(By.ID, "last-name")
field_second_name.send_keys("Safarik")

field_postal_code = driver.find_element(By.ID, "postal-code")
field_postal_code.send_keys("109 00")

# click on Continute button

button_login = driver.find_element(By.ID, "continue")
button_login.click()

time.sleep(5)  # Wait to see checkout overview

button_finish = driver.find_element(By.ID, "finish")
button_finish.click()

time.sleep(5)  # Wait to see result

driver.quit()
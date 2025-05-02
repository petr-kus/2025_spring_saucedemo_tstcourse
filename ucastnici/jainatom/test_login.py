from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

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

# check Swag labs page html <title> 
assert "Swag Labs" in driver.title

# log out
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()

time.sleep(1)  # Wait for menu to expand

logout_button = driver.find_element(By.ID, "logout_sidebar_link")
logout_button.click()

time.sleep(1)  # Wait for page to reload

# log in as a different user
field_username = driver.find_element(By.ID, "user-name")
field_username.send_keys("problem_user")

field_password = driver.find_element(By.ID, "password")
field_password.send_keys("secret_sauce")

button_submit = driver.find_element(By.ID, "login-button")
button_submit.click()

# check Swag labs page html <title> again
assert "Swag Labs" in driver.title

driver.quit()
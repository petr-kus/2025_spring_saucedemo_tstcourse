from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By

import time
from selenium.webdriver.firefox.options import Options



def prihlaseni(text_username: str,text_password: str ):
    Option = Options()
    Option.add_argument('start-maximized')

    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID,'user-name')
    username.send_keys(text_username)

    password = driver.find_element(By.ID,'password')
    password.send_keys(text_password)

    login_button = driver.find_element(By.ID,'login-button')
    login_button.click()

    driver.close()



if __name__ == "__main__":
    udaje = { "standart": { "username": "standart_user",
                             "password": "secret_sauce"},
           "problem": { "username": "problem_user",
                       "password": "secret_sauce"} }
    
    for key in udaje.keys():
        prihlaseni(udaje[key]["username"], udaje[key]["password"])
        
        
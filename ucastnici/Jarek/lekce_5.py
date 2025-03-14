from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.firefox.options import Options


def test_prihlasni(text_username: str,text_password: str ):
    Option = Options()
    Option.add_argument('start-maximized')

    name_web = "https://www.saucedemo.com/"
    
    driver = webdriver.Firefox()
    time.sleep(2)
    driver.get(name_web)


    username = driver.find_element(By.ID,'user-name')
    username.send_keys(text_username)

    password = driver.find_element(By.ID,'password')
    password.send_keys(text_password)

    login_button = driver.find_element(By.ID,'login-button')
    login_button.click()

    driver.close()
    
if __name__ == "__main__":
    udaje = { 
        "standart": { "username": "standard_user",
                       "password": "secret_sauce"},
                         }
    
    test_prihlasni(udaje["standart"]["username"], udaje["standart"]["password"])
        
        
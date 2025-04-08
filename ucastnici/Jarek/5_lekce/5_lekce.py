from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import time
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


def login_test(text_username: str,text_password: str ):
    Option = Options()
    Option.add_argument('start-maximized')

    name_web = "https://www.saucedemo.com/"
    try:
        # open browser
        driver = webdriver.Firefox()
        time.sleep(2)
        driver.get(name_web)
        assert "Swag Labs" in driver.title, "Špatný název stránky"

        # entering username
        username = driver.find_element(By.ID,'user-name')
        username.send_keys(text_username)

        # entering password
        password = driver.find_element(By.ID,'password')
        password.send_keys(text_password)

        # click on login button, login on web
        login_button = driver.find_element(By.ID,'login-button')
        login_button.click()   

        # get all buttons with name "add to cart"
        all_buttons_add_to_cart = driver.find_elements(By.XPATH, "//button[starts-with(@id, 'add-to-cart-')]")

        # if not found, raise exception
        if not all_buttons_add_to_cart:
            raise NoSuchElementException("Element not found")
        
        # add all items on page to the cart
        for button in all_buttons_add_to_cart:
            button.click()
            time.sleep(1)
        

        # click on shopping cart, entering
        login_button = driver.find_element(By.ID,'shopping_cart_container')
        login_button.click()   

        # click on continue shopping, return to the main page
        login_button = driver.find_element(By.ID,'continue-shopping')
        login_button.click()   

        # get all buttons with name "remove"
        all_button_remove = driver.find_elements(By.XPATH, "//button[starts-with(@id, 'remove-')]")

        # if not found, raise exception
        if not all_button_remove:
            raise NoSuchElementException("Element not found")
        
        #  all items on page where are in the cart, remove
        for button in all_button_remove:
            button.click()
            time.sleep(1)

    except NoSuchElementException as e:
        print(e)

    finally:
        time.sleep(2)
        driver.close()


        
# run the test
if __name__ == "__main__":
    udaje = { 
        "standart": { "username": "standard_user",
                       "password": "secret_sauce"},
                         }
    
    login_test(udaje["standart"]["username"], udaje["standart"]["password"])
        
        
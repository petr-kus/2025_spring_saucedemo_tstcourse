from selenium import webdriver
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
        add_to_cart = driver.find_element(By.XPATH, "//button[starts-with(@id, 'add-to-cart-')]")
        add_to_cart.click()
        
        
        test_cart(driver)

        # get all buttons with name "remove"
        all_button_remove = driver.find_element(By.XPATH, "//button[starts-with(@id, 'remove-')]")
        all_button_remove.click()

        test_cart(driver)



    finally:
        time.sleep(2)
        driver.quit()
        
def test_cart(driver):
    cart_elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    if cart_elements:
        cart = cart_elements[0].text  # text obsahující počet položek
        print("Košík je plný")
        print("toto je kosik:", cart)
    else:
        print("Košík je prázdný")

        
        
# run the test
if __name__ == "__main__":
    udaje = { 
        "standart": { "username": "standard_user",
                       "password": "secret_sauce"},
                         }
    
    login_test(udaje["standart"]["username"], udaje["standart"]["password"])
        
        
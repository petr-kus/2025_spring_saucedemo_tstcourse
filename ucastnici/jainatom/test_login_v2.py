from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
#TODO Lektor - test se me moc libi tim ze ma dobre oddelene promene a data.
# jde hezky videt ze se tady dobre pouzila prace s logama, promenyma a datama testu.

logging.basicConfig(filename='my_log.log', level=logging.DEBUG)
#TODO Lektor - TIP mohla jsi si tu nastavit naky timestamp do logu. Ted tam nic neni... .

test_page = 'https://www.saucedemo.com/'
valid_users = ['standard_user']
invalid_users = ['locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
password = "secret_sauce"

def log_exception(e, user=''):
        print(f'Test failed for user: {user} with error: {e}')
        logging.error(f'Test failed for user: {user} with error: {e}')
        
def setup(test_page):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(test_page)
    return driver
#TODO Lektor - jo hezke vyuziti implicitinho cekani. 
#TODO Lektor TIP: Driver klidne mohl byt global a nemsuela jsi si ho pak predavat mezi funkcema jako parametr.

def verify_login_page(driver):
    # check if the "Products" header is present after login
    try:
        products_header = driver.find_element(By.CLASS_NAME, 'title').text
        assert products_header == 'Products', 'Login failed, "Products" header not found.'
        assert driver.title == 'Swag Labs', 'Title incorrect after login.'
        #TODO Lektor - libi se mi ze se tu verifikuje vice veci naraz. (obecne dobre premysleni). Presne dle wisdom..
        #TODO Lektor - Wisdom - co nezkontrolujes se muze lisit(autotest je jen lepsi check list...)
        #TODO Lektor TIP: to co presne za hondoty funkce verifikuje bych si vytahl jako jeji parametr... abych ji mohl prepouzit.
        logging.info("Correct page displayed after login.")
    except Exception as e:
        log_exception(e)

def verify_logout(driver):
    # Check if the login button is displayed after logout
    try:
        login_button = driver.find_element(By.ID, 'login-button').is_displayed()
        assert login_button, 'Logout failed, login button not displayed.'
        #TODO Lektor - kdyby jsi tam nedala to is displayed selhalo by to i bez toho assertu... .
        logging.info('Correct page displayed after logout.')
        #TODO Lektor - je to detail ale je to v podstate zavadejici message. Jak jen ze zxobrazeni tlacitka poznas ze je to spravana stranka?
        #TODO Lektor - 'Login Button is displayed - you are porobaly on login page'
    except Exception as e:
        log_exception(e)

def handle_popup(driver):
    try:
        # Wait for the pop-up window to appear
        popup = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "popup-class-name"))  # Replace with the actual class name
        )
        logging.info("Pop-up detected. Closing...")
        
        # Close the pop-up (e.g., clicking a button)
        close_button = popup.find_element(By.CLASS_NAME, "close-button-class-name")  # Replace with actual class name
        close_button.click()
        logging.info("Pop-up closed successfully.")
    except Exception as e:
        logging.info("No pop-up detected or failed to close pop-up.")
        logging.error(f"Error handling pop-up: {e}")
        # TODO Lektor - ps...u me to selhalo pro zmenu na pritomnosti popupu o znamem hesle... takze ho musim pro spravny bech testu zavrit manaualne. 
        # Jen pro info, na kterem jde krasne videt ze tam muze byt naka variace v popupech a je potreba to odladit :-) 

def login_logout_user(driver, users_list: list, password):
    for user in users_list:
        try:
            logging.info(f'Logging in test user: {user}/{password}.')
            driver.find_element(By.ID, "user-name").send_keys(user)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()

            handle_popup(driver)

            verify_login_page(driver)
            logging.info(f'Login for {user} completed successfully.')
            #TODO Lektor - TIP: dal bych si tam apostrofy f"Login for '{user}' completed successfully." 
        except Exception as e:
            log_exception(e, user)
        finally:
            #log out user
            try:
                driver.find_element(By.ID, "react-burger-menu-btn").click()
                driver.find_element(By.ID, "logout_sidebar_link").click()

                verify_logout(driver)
                logging.info(f'Log out for {user} completed successfully.') 
            except Exception as e:
                log_exception(e, user)

def aftertest(driver):
    driver.quit()

driver = setup(test_page)
login_logout_user(driver, valid_users, password)
aftertest(driver)

 # TODO Lektor - na danou lekci je to hezky ukol. pouzity test data driven pristup :-) moc pekny.
 # TIP: snazil bych se jest o vetsi citelnost a srozumitelnost lepsim pojmenovanim funkci... . napr: test_login_and_logout_of_users(users)
 # odsranil bych pomoci global predavani driveru, a v users by bylo pole dictioneries "jmeno" a "heslo"
 # obdobne bych postupoval u dalsich funkci a podfunkci... setup -> Open page/browser(page), aftertest(driver) -> close browser() atp.

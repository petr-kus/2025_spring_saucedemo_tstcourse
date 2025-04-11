from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import logging

logging.basicConfig(filename='my_log.log', level=logging.DEBUG)

import time

#TODO: Step 0 - Lekce 8 - mit aspon dva test case jako skript co mohou byt atomicke (login, inventory badge? a menu?)
#TODO: Step 1 - Lekce 8 - prepsat test do OOP + POM struktury (udelat invisible predavani driveru!)
#TODO: Step 2 - Lekce 8 - zkopirovat Step 1 a prepsat do PyTestu
#TODO: Step 3 - Lekce 8 - zkopirovat Step 1 a prepsat do Robot Frameworku (s pouzitim nasi OOP a POM - just import)
#TODO: Step 4 - Lekce 8 - prepsat do Robot Frameworku (s pouzitim OpenSource libky - napr. Browser Lib - opravdu prepis)
# Nejdriv ukazka jak to prepsat bez tvorby "Domain Language" a pak ukazat ze to jde i s tím 
#TODO: Step 5 - Lekce 8 - at uz se stihnou vsechny kroky nebo ne DU je: 
# Vyber si Framework a Cestu (Step 2,3,4) a prepis tim Test! (klicove je ukazat rozdily mezi 3-4 stepem!)

#TODO: Note - Ja AI používám pro rady/reaserach jak postupovat a vygenerovaní toho od čeho začnu, pak to ale upravuji hodně sám!
# Nepíšu to celé pomocí AI! Protože to za mě děla volby, které nechi a než bych mu něco vysvětlil je jednoduší to udělat. 
# Generuje to nepotřebný kod atp.
# Když už, tím generují větší kusy kodu, tak mu dám přesý příklad architektury (můj kod) a řeknu mu udělej to stejné pro xyz a hodím mu předpis.
# Nechávám na něm spíše mechanickou činnost než skutečné přemýšlení! Pro přemýšlení to sním jen konzultuji!

test_page = "https://www.saucedemo.com/"
username = "standard_user"
password = "seacratesauce"

def log_test_false_for_me(e):
        print(f"Test xyz faild with error {e}")
        logging.error(f'This is an info message. {e}')
        
def setup(test_page):
    driver = webdriver.Chrome()
    driver.get(test_page)
    return driver

def test_login_user(username,password):
    try:
        logging.info(f'login test user {username} {password}')
        field_username = driver.find_element(By.ID, "user-name")
        field_username.send_keys(username)
        field_password = driver.find_element(By.ID, "password")
        field_password.send_keys(password)
        button_submit = driver.find_element(By.ID, "login-button")
        button_submit.click()
        logging.info(f'Test with {username} {password} passed')
    except Exception as e:
        log_test_false_for_me(e)

def teardown():
    driver.quit()

driver = setup(test_page)
test_login_user(username,password)
teardown()
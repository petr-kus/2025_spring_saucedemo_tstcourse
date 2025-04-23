from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os

def wait_for_element(driver, by_locator, timeout=3):
    """
    Funkce čeká, dokud nebude element viditelný na stránce.
    
    :param driver: WebDriver instance
    :param by_locator: By locator pro vyhledání elementu (např. (By.CLASS_NAME, 'some-class'))
    :param timeout: Maximální čas čekání na element (výchozí hodnota je 10 sekund)
    :return: Nalezený element
    """
    wait = WebDriverWait(driver, timeout)
    try:
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return element
    except Exception as e:
        logging.error(f"⛔ Chyba pri cekani na element {by_locator}: {e}")
        print(f"⛔ Chyba při čekání na element {by_locator}: {e}")
        return None

# Nastavení logování
def get_log_filename():
    script_name = os.path.basename(__file__)  # logovací soubor s názvem scriptu a _log.log
    log_filename = f"{script_name.replace('.py', '')}_log.log"
    return log_filename

def setup_logging():
    log_filename = get_log_filename()
    logging.basicConfig(filename=log_filename,
                        level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
URL = "https://www.saucedemo.com/"

CREDENTIALS = {
    'standard_user': 'secret_sauce',
    'problem_user': 'secret_sauce'
    }

def start_browser():
    return webdriver.Edge()

def login(driver, username):
    setup_logging()
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(CREDENTIALS[username])
    driver.find_element(By.ID, "login-button").click() 

    try:
        WebDriverWait(driver, 2).until(EC.url_contains("inventory.html"))
        logging.info(f"✅ Prihlasen uzivatel: {username}")
        print(f"✅ Přihlášen uživatel: {username}")
    except Exception as e:
        logging.error(f"⛔ Nepodarilo se prihlasit uzivatele: {username} - {e}")
        print(f"⛔ Nepodařilo se přihlásit uživatele: {username} - {e}")
        driver.quit()

def get_inventory_items(driver):
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    products = []
    for item in items:
        name_elem = item.find_element(By.CLASS_NAME, "inventory_item_name")
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        img = item.find_element(By.TAG_NAME, "img").get_attribute("src")
        products.append({
            'name': name_elem.text,
            'price': price,
            'img': img,
            'element': name_elem
        })
    return products

def verify_product_detail(driver, product_name, original_img, original_price):
    # obrázek
    try:
        detail_img_elem = wait_for_element(driver, (By.CLASS_NAME, "inventory_details_img"))
        detail_img = detail_img_elem.get_attribute("src")
    except Exception as e:
        logging.error(f"⛔ Chyba pri ziskavani obrazku pro {product_name}: {e}")
        print(f"⛔ Chyba při získáváni obrázku pro {product_name}: {e}")
        return
    
    # cena
    try: 
        detail_price_elem = wait_for_element(driver, (By.CLASS_NAME, "inventory_details_price"))
        detail_price = detail_price_elem.text
    except Exception as e:
        logging.error(f"⛔ Chyba pri ziskavani ceny pro {product_name}: {e}")
        print(f"⛔ Chyba při získávání ceny pro {product_name}: {e}")
        return
    
    # název
    try:
        detail_name_elem = wait_for_element(driver, (By.CLASS_NAME, "inventory_details_name"))
        detail_name = detail_name_elem.text
    except Exception as e:
        logging.error(f"⛔ Chyba při získávání názvu pro {product_name}: {e}")
        print(f"⛔ Chyba při získávání názvu pro {product_name}: {e}")
        return

    # Porovnání obrázku
    if original_img != detail_img:
        logging.error(f"⛔ Obrázek nesouhlasi u {product_name}")
        print(f"⛔ Obrázek nesouhlasí u {product_name}")

    # Porovnání ceny
    if original_price != detail_price:
        logging.error(f"⛔ Cena nesouhlasi u {product_name}")
        print(f"⛔ Cena nesouhlasí u {product_name}")

    # Porovnání názvu
    if product_name != detail_name:
        logging.error(f"⛔ Nazev polozky nesouhlasi u {product_name}")
        print(f"⛔ Název položky nesouhlasí u {product_name}")

    # Pokud všechny testy projdou
    if product_name == detail_name and original_img == detail_img and original_price == detail_price:
        logging.info(f"✅ {product_name} ma shodny nazev, obrazek a cenu.")
        print(f"✅ {product_name} má shodný název, obrázek a cenu.")

def test_all_products(username):
    driver = start_browser()
    login(driver, username)
      
    try:
        products = get_inventory_items(driver)

        for i in range(len(products)):
            products = get_inventory_items(driver)  # znovu načti po návratu
            product = products[i]
            logging.info(f"Testuji produkt: {product['name']}")

            product['element'].click()
            verify_product_detail(driver, product['name'], product['img'], product['price'])
            driver.back()
            wait_for_element(driver, (By.CLASS_NAME, "inventory_item"))
    except Exception as e:
        logging.error(f"❌ Vyjimka pri testovani produktu uzivatele {username}: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    for user in CREDENTIALS:
        test_all_products(user)

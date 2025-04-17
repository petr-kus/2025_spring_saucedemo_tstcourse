from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 #TODO Lektor - celkove super napad na test case, docela dobre provedeni, libvi se mi hodne vystup a formatovani co jde do command line i log je krasny
 #TIP: co screenshoty? :-)


import time
#TODO: Lektor - neimportovat co neni potreba :-) (ja vim jen se to tu zapomnelo...)

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
    ##TODO: Lektor - PS: Ctu ze vytchozi cekani je 3s

    wait = WebDriverWait(driver, timeout)
    try:
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return element
    except Exception as e:
        logging.error(f"⛔ Chyba při čekání na element {by_locator}: {e}")
        print(f"⛔ Chyba při čekání na element {by_locator}: {e}")
        return None
    #TODO: Lektor - moc pekne libi se mi ze se tu pamatuje na log do konzole i na log do logu. 
    # A i to ze jsi si pro to vytvorila svoji vlastni funkci... !
    # PS: TIP s ' ... Chyba při čekání na element '{by_locator}': '{e}' - co kdyz retezce budou prazdne neuvidis to v logovani...
    

# Nastavení logování
def get_log_filename():
    script_name = os.path.basename(__file__)  # logovací soubor s názvem scriptu a _log.log
    log_filename = f"{script_name.replace('.py', '')}_log.log"
    return log_filename
    #TODO: Lektor - nice, libi se mi ze se to prizpusobuje nazvu skriptu :-). Handy! - tady se premyslelo to se ceni!

def setup_logging():
    log_filename = get_log_filename()
    logging.basicConfig(filename=log_filename,
                        level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    #TODO: Lektor - nice, nastaveni time stamp to se hodi!
    
URL = "https://www.saucedemo.com/"
CREDENTIALS = {
    'standard_user': 'secret_sauce',
    'problem_user': 'secret_sauce'
    }

#TODO: Lektor - nice, uzivatel a heslo krasna dvojicka a automatizacni tricek!
#TODO: PS: TIP/k zamysleni... a co kdyby tam i bylo zakomponovano zda se to prihlasit ma/nema, pripadne jaka ma vyskocit error hlaska?

def start_browser():
    return webdriver.Edge()
    #TODO: Lektor - nice, tricek one liner... :-) s returnem!

def login(driver, username):
    setup_logging() #TODO: Lektor - to se asi koncepcne melo volat nekde jinde. ne v predpisu test casu. Treba pred forem pro test vsech useru.
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(CREDENTIALS[username])
    driver.find_element(By.ID, "login-button").click() 

    #TODO: Lektor - adresace by mela byt nekde bokem spis ulozena aby se zvysila citelnost.
    # tedy toto a podobne bych dal do promene na vhodne misto (By.ID, "login-button") 
    # kdyz ty ID jsou krasne citelna a takto kratka jeste se to prezit da kdyz je to pouzite jednou. 
    # Ale realny svvet tak krasny neni...

    try:
        WebDriverWait(driver, 2).until(EC.url_contains("inventory.html"))
        #TODO: Lektor - radek vyse je dle me zbytecny diky defaultni load strategy selenium dirveru - proste to pocka az se stranka nacte samo... . 
        logging.info(f"✅ Prihlasen uzivatel: {username}")
        print(f"✅ Přihlášen uživatel: {username}")
        #TODO: Lektor - TIP na toto logovani a print do konzole jsi si mohla udelat funkci/funkce... aby jsi nemusela mackat furt "Ctrl+C"
        #TODO: Wisdom, kdyz zmacknes "Ctrl+C" => Premyslej!

    except Exception as e:
        logging.error(f"⛔ Nepodarilo se prihlasit uzivatele: {username} - {e}")
        print(f"⛔ Nepodařilo se přihlásit uživatele: {username} - {e}")
        driver.quit()

    #TODO: Lektor - Obecne k teto funkci - TIP: toto je v podsdtate predpis test casu. Snazil bych se o vetsi citelnost a min aby to vypadalo jako kod...
    

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
         # TODO: Lektor - ty waity - pokud se tam neco nedeje vyslovene s javascriptem na strance. Tohle by uz melo byt nactene... .
         # a neni potreba sem explicitni wait psat.

        detail_img = detail_img_elem.get_attribute("src")
    except Exception as e:
        logging.error(f"⛔ Chyba pri ziskavani obrazku pro {product_name}: {e}")
        print(f"⛔ Chyba při získáváni obrázku pro {product_name}: {e}")
        return
    
    #TODO: Lektor - jako ze Nice... idea. Ale co kdyz cesta k obrazku je ale obrazek neexistuje a nebo ma 0 hodnotu? 
    # Tady se kontroluje jen exitence cesty ne samotneho souboru a jeho zobrazeni!
    # bud bych si ho zkusil jeste stahnout image_data = requests.get(detail_img).content
    # nebo neco jako...
    # assert detail_img, "Obrázek nemá src"
    # assert detail_img.startswith("http"), f"Neplatná URL: {detail_img}"
    # assert detail_img_elem.is_displayed(), "Obrázek není zobrazen"
    # assert detail_img_elem.size["height"] > 0 and detail_img_elem.size["width"] > 0, "Obrázek má nulové rozměry"
    
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

    #TODO: Lektor - super... nice idea! A chvalim. Jen je potreba si uvedomit ze porovnavas link na zdroje a ne samotny obsah!

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

    #TODO: Lektor - celkove myslenka porovnani objektu co je na productu s detailem je super!
    # presne takhle se vyuziva auto test a pak se to klidne pusti pres vsechny produkty! Nadherna idea!
    # TIP: vyuzil bych OOP a predaval bych si dva objekty... Jeden z Product page a druhy z deatilu a preovnaval bych jen ty objekty.
    # assert original.name == deatil.name
    # assert original.image_src == deatil.image_src
    # assert original.image_content == original.image_content
    # ...
    # TIP levl 2: muzes si napsat funkci/metodu co obecne porovna dva objekty, a jen mu hodis dve instance a uz se nestaras co je vevnitr... .

def test_all_products(username):#
    driver = start_browser()
    login(driver, username)
      
    try:
        products = get_inventory_items(driver)

        for i in range(len(products)):
            products = get_inventory_items(driver)  # znovu načti po návratu
            #TODO Lektor - Okej, to -radek vise- tu byt nemusi. Ale predpokladam ze to tam chces kdyby se to nahodou zmenilo?

            product = products[i]
            logging.info(f"Testuji produkt: {product['name']}")
            #TODO Lektor - vidis a protoze na to nemas funkci tady command line trpi a tam to videt nejde :-)

            product['element'].click()
            verify_product_detail(driver, product['name'], product['img'], product['price'])
            driver.back()
            wait_for_element(driver, (By.CLASS_NAME, "inventory_item"))
            #TODO Lektor - no, nejsem si uplne jist ze to cekani je zde potreba... . Tipl bych ze ne.

    #TODO Lektor - celkove opet, toto uz je v podtsate zapis test case, stale je to dost necitelne. 
    # dokonce jsi neodelila uplne predpis test casu od IDcek... (By.CLASS_NAME, "inventory_item") ... 
    # a take myslenka z toho neni uplne citelna na prvni dobrou... coz je skoda!
    # 
    # Pomohlo by i prejmenovani treba Products ==> Products_on_product_page 
    # compare(Product_detail[i], Products_on_product_page[i])
    # nebo neco takoveho... 

    except Exception as e:
        logging.error(f"❌ Vyjimka pri testovani produktu uzivatele {username}: {e}")
        #TODO Lektor - moc se me libi ten tvuj krizek... ale zase trpi command line :-)

    finally:
        driver.quit()

    #TODO Lektor - dobre vyuziti try / except / finally...!

if __name__ == "__main__":
    for user in CREDENTIALS:
        test_all_products(user)

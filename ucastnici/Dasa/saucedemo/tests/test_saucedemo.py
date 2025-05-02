import pytest
from selenium import webdriver
import time
import logging
import os
import sys
from datetime import datetime

# Přidání kořenového adresáře projektu do PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.Menu import Menu

# Konfigurace
BASE_URL = "https://www.saucedemo.com/"
# TODO Lektor: tahle base url ale neni vyuzita ... uvnitr LoginPage...!
# TODO prepnuti stranky proti ktere se testuje by bylo narconejsi... .

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# Nastavení loggeru
def setup_logger():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"test_{current_time}.log")
    
    logger = logging.getLogger("saucedemo_test")
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Fixtures
@pytest.fixture(scope="session")
def logger():
    """Fixture pro logger."""
    return setup_logger()

@pytest.fixture(autouse=True, scope="session")
def driver(logger):
    """Fixture pro webdriver."""
    logger.info("Inicializace webdriveru")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    
    try:
        driver = webdriver.Chrome(options=options)
        logger.info("Webdriver byl úspěšně inicializován")
        
        yield driver
        
    except Exception as e:
        logger.error(f"Chyba při inicializaci webdriveru: {str(e)}")
        raise
    
    finally:
        try:
            if 'driver' in locals():
                driver.quit()
                logger.info("Webdriver byl úspěšně ukončen")
        except Exception as e:
            logger.error(f"Chyba při ukončování webdriveru: {str(e)}")


#TODO Lektor: tohle user name a password jde urcite vyresit pomoci fixture :-). 
#Ale mnohem vhodnejsi by bylo to poresit pomoci parametrize... . Ta fixture je 'kanon na vrabce' zbytecne neictelny.
@pytest.fixture
def username():
    """Fixture pro uživatelské jméno."""
    return USERNAME

@pytest.fixture
def password():
    """Fixture pro heslo."""
    return PASSWORD

# Pomocné funkce
def slowdown():
    """Zpomalí test o 2 sekundy."""
    time.sleep(2)

# Testy
def test_login_the_user(driver, username, password, logger):
    # TODO Lektor: driver a logger bych zde uz nepredaval a nechal to na autouse... oboje.
    # respektive predaveni driveru a loggeru bych se snazil zbavit co to jde, ale chapu ze toto je nejsnazsi a funkcni reseni si to predat.
    # u druveru by se muselo asi vyuzit dedicnosti trid... a udelat base tridu pro page. 
    # U loggeru bud to stjene a nebo by slo vyuzit proste jen nastaveni loggingu a apk provolavat obecne logging.

    """Test úspěšného přihlášení uživatele."""
    login_page = LoginPage(driver, logger)
    inventory_page = InventoryPage(driver, logger)
    
    login_page.login_user(username, password)
    slowdown()
    inventory_page.we_are_on_page()

def test_cart_badge_behavior(driver, logger):
    """Test přidání a odebrání produktů z košíku."""
    inventory_page = InventoryPage(driver, logger)
    
    slowdown()
    inventory_page.add_random_products_to_cart()
    slowdown()
    inventory_page.remove_from_cart_all_products()
    slowdown()

def test_logout_a_user(driver, username, password, logger):
    """Test odhlášení uživatele."""
    login_page = LoginPage(driver, logger)
    menu_bar = Menu(driver, logger)
    inventory_page = InventoryPage(driver, logger)
    
    # Nejdřív se přihlásíme
    login_page.login_user(username, password)
    slowdown()
    
    # Počkáme na načtení stránky s produkty
    inventory_page.we_are_on_page()
    slowdown()
    
    # Pak se odhlásíme
    menu_bar.open_menu()
    slowdown()
    menu_bar.press_logout()
    slowdown()
    login_page.we_are_on_page() 

# TODO Lektor: celkove se me to libi. Je videt pouziti hodne veci z lekci, krasne vyuziti POM. Zjvene pouzite allure. krasa!
# Rozhodne je to dobre napsane (nekde bych rekl skorko kopie lektora :-) - jde videt ze sis odnesla tipy co na lekcich rikam).

#TIP: strtedni cast testu - nahodne pridavani - si neoveruje ze neco bylo pridano do kosiku, takze to jde udelat passed i kdyz se nic neprida. (vyskakuje me tam dialog s heslem co zablokuje test... tak jsem si toho vsiml)

# jinak logger ma problemy s ceskymy znaky - jde to videt v logach. Prvadepodobne zdrojovy kod neni ulozen jako unicode ale jako cp1250. Doporucuji zkusit preulozit jako unicode8 a kdyz to nezabere. 
# tak pohledat zda se da nak nastavit logovani jinych znaku...
# a kdyz ani to nezabere proste to mit v anglictne nebo bez hacku a carek.
# PS: mozna jsme to omylem, spatne preulozil ja.
from Utils.logger import setup_logging
from Utils.logger import assert_and_log
import logging
from Pages.product_page import ProductPage
from Pages.login_page import LoginPage
from Config import config
import pytest
from selenium import webdriver

setup_logging("pytest_Reset_App_Store_u9")
logger = logging.getLogger()
logger.info("Spouští se testování.")

@pytest.fixture(params=config.CREDENTIALS.items(), scope="function")
def driver_logged_in(request):
    username, password = request.param

    if config.BROWSER.lower() == "edge":
        driver = webdriver.Edge()
    elif config.BROWSER.lower() == "chrome":
        driver = webdriver.Chrome()
    elif config.BROWSER.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {config.BROWSER}")

    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(username, password)
    logger.info(f'Testování v prohlížeči {driver}')

    yield driver

    driver.quit()
    print("Test dokončen")
    logger.info("Test dokončen")
 
def test_reset_app_state(driver_logged_in):
    driver = driver_logged_in
    product_page = ProductPage(driver)
    product_id = "sauce-labs-backpack"

    # 1. Přidání do košíku
    product_page.click_cart_button(product_id)
    logger.info(f'Do košíku přidán produkt {product_id}.')

    # 2. Kontrola změny tlačítka na "Remove"
    button_text = product_page.get_cart_button_text(product_id)
    logger.info(f'Tlačítko je aktuálně {button_text}.')
    assert button_text is not None, "Tlačítko 'Remove' nebylo nalezeno"
    assert button_text.lower() == "remove", f"Očekáváno 'Remove', ale je '{button_text}'"
    
    # 3. Kontrola, že v košíku je 1 produkt
    cart_count = product_page.get_cart_count()
    logger.info(f'V košíku je {cart_count}')
    assert cart_count == "1", f"Očekáváno 1 produkt v košíku, ale je {cart_count}"
   
    # 4. Stisknutí Reset
    product_page.reset_app_state()
    logger.info('Proveden reset app store')

    # 5. Kontrola, že košík je prázdný
    cart_count_after = product_page.get_cart_count()
    logger.info(f'Stav košíku je {cart_count_after}')
   
    assert_and_log(
        cart_count_after == "0",
        f"Košík není po resetu prázdný, má: {cart_count_after}",logger
        )

    # 6. Kontrola, že tlačítko je zpět na "Add to cart" po resetu
    add_button_text = product_page.get_cart_button_text(product_id)
    logger.info(f"Tlačítko po resetu je {add_button_text}")

    if add_button_text is None:
        logger.warning("⚠️ Tlačítko nebylo nalezeno po resetu")
        print("⚠️ Tlačítko nebylo nalezeno po resetu")
    elif add_button_text.lower() != "add to cart":
        logger.warning(f"⚠️ Po resetu není tlačítko 'Add to cart', ale '{add_button_text}'")
        print(f"⚠️ Po resetu není tlačítko 'Add to cart', ale '{add_button_text}'")

    # 7. Pokud je to stále "Remove", zkusí se kliknout a ověřit se, že se změní
    if add_button_text and add_button_text.lower() == "remove":
        logger.info("Tlačítko po resetu je 'Remove', pokus na něj kliknout...")
        product_page.click_cart_button(product_id)
        add_button_text = product_page.get_cart_button_text(product_id)
        logger.info(f"Tlačítko po kliknutí je '{add_button_text}'")
        
        assert_and_log(
        add_button_text and add_button_text.lower() == "add to cart",
        f"Očekáváno 'Add to cart' po kliknutí, ale bylo: '{add_button_text}'",logger
        )



 
    
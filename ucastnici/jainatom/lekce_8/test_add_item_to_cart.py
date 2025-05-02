from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import wait_for_element
#TODO Lektor - chvalim za pouziti principu si napsat neco do externiho souboru!
# Je to spravny styl premyselni odklidit odsud co neni potreba aby zde bylo a jen to importovat.
# a zaroven to importem vyuzit jinde. Sice vetsinu toho co tam mas asi neni nutne... protoze cekani na stranlku by nemelo byt nutne... .
# tento princip se dal treba pouzit pro nektre fixtures, browser samotny... nebo parametrizaci... atp. a bylo by to the best!

import os
from saucedemo.LoginPage import LoginPage
from saucedemo.InventoryPage import InventoryPage
import pytest
import logging

logging.basicConfig(
    filename='log_jt_test_add_item_to_cart.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Logging setup successfully!")
test_page = "https://www.saucedemo.com/"
#TODO Lektor - tato parametrizace stranky se ale vevnitr nepouziva :-(
valid_user = 'standard_user'
user_password = "secret_sauce"

@pytest.fixture(autouse=True, scope="session")
def edgeBrowser():
    global browser
    browser = webdriver.Edge()
    browser.get(test_page)
    yield browser
    browser.quit()

@pytest.fixture
def username():
    return valid_user

@pytest.fixture
def password():
    return user_password
#TODO Lektor - pro password a pro username se da pouzit fixture. Ale mnohem vhodnejsi by bylo pouzit parametrize... .

#TEST CASE
def test_cart_badge_behavior(username, password):
    """Put random amount of items into cart and check its volume."""
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)

    login_page.login_user(username, password)
    wait_for_element(browser, 2, (By.CLASS_NAME, 'title'))
    #TODO Lektor - tento wait by tu nemel byt potreba. Ono by to samo melo pockat az se stranka nacte... .
    inventory_page.we_are_on_page()
    inventory_page.verify_login()
    wait_for_element(browser, 2, (By.CLASS_NAME, 'title'))
    #TODO Lektor - tento wait by tu nemel byt potreba. Ono by to samo melo pockat az se stranka nacte... .
    inventory_page.add_random_products_to_cart()

#TODO Lektor - moc hezky test case. Login uzivatele a ze jsme na inventory page je ale precondition toho testu, tak bych to tak i napsal... .
# zachoval bych se tak vuci tomu a vytovril si treba fixture loged_on_inventory_page
# do teto fixture bych dal kontrolu zda v tom stavu jsme a pokud by jsme nebyli dovedl bych to v te fixture do daneho stavu... (zalogoval a zkontroloval zalogovani).
# tim se pak v samotnem test casu uz muzes zamerit jen na to co skutrecne testuje... a to je test_cart_badge_behavior ...

#V celem POM - Page Object Modelu mas uplne minimum logovani... Vlastne cely tets dost minimalne vytvari logy a chtelo by je pridat, aby byly zobrazene v pytest-html reportech.
#(udelani par screenshotu by bylo taky fajn)

#stejny komentare plati ramcove i pro ten druhy test. Kam jsem komentare uz nedaval... .

# Celkove moc pekne vyuzite POM, jde videt ze se kopirovalo :-). Ale to je ok. Dulezity je umet to sama napsat a rozumet tomu...
# mohla jsi zkusit to rozsirit o nakou dalsi stranku tereba nebo funkci. A nenechat tam jen to co je v prikladech... .
# libi se mi ze nemas predavani browseru pro test...

#jinak trochu tu postradam naky naovd nebo install_dependencies.ps1 separe pro tento ukol... . Nebo tak neco.
#od ceho by nezanli dane veci zacal... treba readme.md ... .
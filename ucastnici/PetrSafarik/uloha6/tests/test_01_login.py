from selenium import webdriver
import sys
import logging
import pytest

#TODO: Lektor - Chvalim pouziti pytest.ini a nastudovani si PyTestu vcetne HTML reportu dopredu! 
#TODO: Lektor - Hodne Chvalim pouziti fixtures a yieldu a nastudovani si dopredu!

sys.path.append('../')
from uloha6.pages.login_page import LoginPage
#TODO: Lektor - Hodne Chvalim pouziti Page Object Modelu!


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#TODO: Lektor - Asi bych ten debug nenstavoval obecne dopredu. Mel bych strach ze prepisu nake default rozumne nastaveni. (to si ale clovek casem vychyta pohledem do logu)
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

class TestLoginPage:
    class_name = "TestLoginPage"
    file_handler = logging.FileHandler(f"{class_name}_debug_logs.log")
    #TODO: Lektor - tato konstrukce kde logujes/nastavujes neco co je samo o sobe v tom jazyce je super. Kdyz bych byl linej to hledat/psat udelal bych to stejne :-).
    #TODO: Da se zde ale typicky vyuzit naka vlastnost samotneho jazyka nemusis si to uvadet zvlast v promenne... proste to odnekud vytahnes... reflexe napriklad nebo pristup k parametrum tridy/instance cls., self. a nebo nastavit si to v _init_.
    #TODO: Po konzultaci s AI bych asi volil cestu nastavit si to a udelat tuto praci v _init_ jako "class_name = self.__class__.__name__" otazka zni zda PyTest s tim pracuje v instancich a nebo v tridach.
    #TODO: pokud v tridach museli by jsme heldat dal naky hack. Spis lektorsky je pro me dulezity ti rict, ze to jde udelat jinak / obecneji.


    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    #TODO: Lektor - celkove k tomu logovani. Ja bych to vubec po soborech nedelil. Nevidim k tomu duvod. Vse bych nechal logovat to defalutnich mist od PyTestu. 
    #TODO: Lektor - je to zbytecny kod na vic, pokud pro to neni naky specificky cil. (napriklad ze pro dany test, objekt, atd. chceme mit testy nekde)

    @pytest.fixture()
    def fixture(self):
        #TODO: Lektor - pojmenoval bych to jinak (browser, page, tab, ... ?) pro budovani Domain Language a proto ze fixture je skoro "klicove slovo".
        #TODO: Lektor - nevyuzita prilezitost budovat langauge
        driver = webdriver.Chrome()
        expected_title = "Swag Labs"
        #TODO: Lektor - Moc pekny trik predat si oboji i s verifikacni casti, jen je to moc "zadratovane" uvnitr. Zparametrizoval bych si tu fixture.
        yield driver, expected_title
        driver.close()
        driver.quit()

    def test_login(self, fixture):
        driver, expected_title = fixture
        login_page = LoginPage(driver)

        #TODO: Lektor - zde (nize) dvakrat otviras stranku. Vidis to? (staci prvni radek vynechat a nebo jeste lip zapamatovat si output)
        login_page.open_page()
        assert login_page.open_page() == expected_title, "Title mismatch"

        login_page.enter_user_name()
        login_page.enter_password()
        login_page.click_login_button()
        #TODO: Lektor - libi se mi jak krasne mas citelny test. Ale nak me tam chybi viditelnost do tech dat co tam tecou a jako uzivatel zadavam ... .
        #TODO: Lektor - protoze samotna data mas schovana v POM. Ale to je prece neco co by jsme meli videt na urovni testu. Zde by to mel byt parametr!
        #TODO: Lektor - login_page.enter_user_name('standard_user')
        #TODO: Lektor - login_page.enter_password('secret_sauce')
        assert login_page.login_error_message() == "", "Login failed."

    def test_login_invalid_password(self, fixture):
        driver, expected_title = fixture
        login_page = LoginPage(driver)
        assert login_page.open_page() == expected_title, "Title mismatch"
        login_page.enter_user_name()
        login_page.enter_invalid_password()
        login_page.click_login_button()
        assert login_page.login_error_message() == ("Epic sadface: Username and password do not match any user "
                                                    "in this service"), "incorrect error message"
        #TODO: Lektor - NICE hezky tricek s error message. Jen bych asi nedelal presne porovnani, ale spis jen zda dana vec/regular tam je.
        #TODO: Lektor - Celkove, celou vec s dvema test case bych napsal do jednoho a vyuzil parametrize z PyTestu! (vidis kolik je tam duplikace kodu? 
        #TODO: Lektor - Wisdom: Mackas "Ctrl+C" => Premysleji!)
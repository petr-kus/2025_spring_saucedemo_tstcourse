from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#TODO Lektor - tady nahore jsou veci co zde byt nemusi... protoze nejsou pouzivane
import logging

class LoginPage:
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    submit_button = (By.ID, "login-button")
    page_url = "https://www.saucedemo.com/"
    #TODO Lektor - Ta url by mela byt parametrizovana z venku... .
    # vim ze jsem to takhle asi mel v prikaldove uloze... ale co kdyz v testu budeme chtit zmenit vuci jake strance testujeme?

    def __init__(self, driver):
        self.driver = driver

    def we_are_on_page(self):
        assert self.page_url == self.driver.current_url, f"We are not on the right page '{self.page_url}'"

    def login_user(self, username, password):
        field_username = self.driver.find_element(*self.username_field)
        field_username.send_keys(username)
        #TODO Lektor - toto klidne mohl byt one liner... sem uz se moc nikdo nediva.
        # muzeme psat i usporneji a min sorozumitelne...
        #self.driver.find_element(*self.username_field).send_keys(username)
        #stejne tak nize...
        field_password = self.driver.find_element(*self.password_field)
        field_password.send_keys(password)
        button_submit = self.driver.find_element(*self.submit_button)
        button_submit.click()

    def verify_logout(self):
        '''Checks that user is on login page.'''
        login_button = self.driver.find_element(By.ID, 'login-button').is_displayed()
        assert login_button, 'Logout failed, login button not displayed.'
        logging.info('Correct page displayed after logout.')
        #TODO Lektor - Toto je silne tvrzeni na to ze jsme zkontrolobvali jen jeden button... mozna by jsme meli rict neco jako
        # was shown a login button, you are problay on login page
        # WISDOM tady je to jeste ok, ale kdyz si v autotestech zvyknes rikat veci co nejsou pravda pak to pridelava problemy, kdyz se dohledava problem... .
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "user-name")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//div[@id='login_button_container']//h3[@data-test='error']")

        #TODO: Lektor - nize - toto tady nejspise nema byt.
        self.url = "https://www.saucedemo.com/"

        #TODO: Lektor - toto tady urcite nema byt.
        self.user_name = "standard_user"
        self.password = "secret_sauce"
        self.invalid_password = "blabla"

    def open_page(self):
        self.driver.get(self.url)
        actual_title = self.driver.title
        #TODO: Lektor - tak pokud to mame uz tady, tak uz tady jsme schopni verifikovat zda jsme na spravne strance.
        #klidne to sem muzeme napsat!
        #PS: Obecne, ja osobne bych si to spis napsal do objektu browseru nebo do fixtures... ale proc ne muze to byt i zde.
        return actual_title

    def enter_user_name(self):
        self.driver.find_element(*self.username_textbox).send_keys(self.user_name)

    def enter_password(self):
        self.driver.find_element(*self.password_textbox).send_keys(self.password)
        #TODO: self.user_name a self.password by melo byt urcite parametrizovane z venku ne z tridy ci instance obejktu. (zmineno uz jinde)

    def enter_invalid_password(self):
        self.driver.find_element(*self.password_textbox).send_keys(self.invalid_password)
        #TODO: kdyz by jsme to vkladaly z venku tuto tridu nejspise ani nepotrebujeme... .
        #TODO: Lektor - Wisdom: Mackas "Ctrl+C" => Premysleji!)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login_error_message(self):
        try:
            error_message = self.driver.find_element(*self.error_message)
        except WebDriverException as e:
            return ""
        return error_message.text
        #TODO: Lektor - Pekny tricek jak jsi preposlal overeni konkretni error message ven do testu.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver: WebDriver, timeout=1):
        self.driver = driver
        self.timeout = timeout  # defaultní timeout pro čekání

    def wait_for_element(self, by_locator, timeout=None):
        """
        Čeká na viditelnost elementu a vrací ho.
        """
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        try:
            element = wait.until(EC.visibility_of_element_located(by_locator))
            return element
        except Exception as e:
            logger.error(f"❌ Chyba pri cekani na element {by_locator}: {e}")
            print(f"❌ Chyba při čekání na element {by_locator}: {e}")
            return None

    def click(self, by_locator):
        element = self.wait_for_element(by_locator)
        if  element:
            element.click()

    def send_keys(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        if  element:
            element.clear()
            element.send_keys(text)

    def get_text(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.text if element else None
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def wait_for_element(driver, timeout, locator):
    """Waits for an element to be present on the page."""
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

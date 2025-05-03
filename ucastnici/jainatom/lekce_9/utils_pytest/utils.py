from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def wait_for_element(driver, timeout, locator):
    """
    Wait for an element to be present and visible within the timeout period.
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator), 
        message=f"Element with locator {locator} not found within {timeout} seconds."
    )

def wait_for_element_with_text(driver, timeout, locator, expected_text):
    """
    Wait for an element to be present and have a specific text value within the timeout period.
    """
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, expected_text),
        message=f"Element with locator {locator} did not have text '{expected_text}' within {timeout} seconds."
    )
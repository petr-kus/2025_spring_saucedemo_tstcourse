# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1195, 1040)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  

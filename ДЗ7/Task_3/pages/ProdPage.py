from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProdPage:

    def __init__(self, browser):
        self._driver = browser

    def add_to_cart(self):
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
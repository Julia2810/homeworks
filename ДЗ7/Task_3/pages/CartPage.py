from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CartPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/cart.html")


    def click_on_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()
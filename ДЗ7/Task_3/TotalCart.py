from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TotalCart:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")


    def input_login(self, name):
        self._driver.find_element(By.ID,"user-name").send_keys(name)

    def input_password(self, pas):
        self._driver.find_element(By.ID,"password").send_keys(pas)

    def click_for_authorization(self):
        self._driver.find_element(By.ID, "login-button").click()

    def add_cart(self):
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()

    def click_on_cart(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def click_on_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()

    def input_first_name(self, name):
        self._driver.find_element(By.ID, "first-name").send_keys(name)

    def input_last_name(self, surname):
        self._driver.find_element(By.ID, "last-name").send_keys(surname)

    def input_index(self, index):
        self._driver.find_element(By.ID, "postal-code").send_keys(index)

    def click_on_continue(self):
        self._driver.find_element(By.ID, "continue").click()

    def write_of_total(self):
        total = self._driver.find_element(By.XPATH, "//div[contains(text(),'Total: $')]").text
        print(total)

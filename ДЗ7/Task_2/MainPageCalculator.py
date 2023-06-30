from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    def __init__(self, driver):
        self._driver = driver
        self._WebDriverWait = WebDriverWait
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.find_element(By.ID, "delay").clear()

    def input_secund(self, number):
        self._driver.find_element(By.ID, "delay").send_keys(number)

    def click_button_7(self):
        self._driver.find_element(By.XPATH,"//span[contains(text(),'7')]").click()

    def click_button_plus(self):
        self._driver.find_element(By.XPATH,"//span[contains(text(),'+')]").click()

    def click_button_8(self):
        self._driver.find_element(By.XPATH,"//span[contains(text(),'8')]").click()

    def click_button_equally(self):
        self._driver.find_element(By.XPATH,"//span[contains(text(),'=')]").click()

    def wait_result(self, secunds, result_of_action):
        self._WebDriverWait(self._driver, secunds).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), result_of_action))

    def test_result_of_sum(self):
        res = self._driver.find_element(By.CLASS_NAME, "screen").text
        return res
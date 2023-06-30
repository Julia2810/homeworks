from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OverviewPage:

    def __init__(self, browser):
        self._driver = browser


    def write_of_total(self):
        total = self._driver.find_element(By.XPATH, "//div[contains(text(),'Total: $')]").text
        print(total)
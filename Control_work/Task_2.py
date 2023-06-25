from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")



Entry_field = driver.find_element(By.ID, "delay")
Entry_field.clear()
Entry_field.send_keys(45)



Seven = driver.find_element(By.XPATH,"//span[contains(text(),'7')]").click()

Plus = driver.find_element(By.XPATH,"//span[contains(text(),'+')]").click()

Eight = driver.find_element(By.XPATH,"//span[contains(text(),'8')]").click()

Equals = driver.find_element(By.XPATH,"//span[contains(text(),'=')]").click()


WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))

def test_result_of_sum():
    result = driver.find_element(By.CLASS_NAME, "screen")
    assert result.text == '15'
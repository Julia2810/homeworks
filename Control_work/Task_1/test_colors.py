from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys('Иван')

driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys('Петров')

driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys('Ленина, 55-3')

driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys('test@skypro.com')

driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys('+7985899998787')

driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys('Москва')

driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys('Россия')

driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys('QA')

driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


red_color = 'rgba(248, 215, 218, 1)'
green_color = 'rgba(209, 231, 221, 1)'
new_list = [driver.find_element(By.ID, "first-name").value_of_css_property('background-color'),
            driver.find_element(By.ID, "last-name").value_of_css_property('background-color'),
            driver.find_element(By.ID, "address").value_of_css_property('background-color'),
            driver.find_element(By.ID, "e-mail").value_of_css_property('background-color'),
            driver.find_element(By.ID, "phone").value_of_css_property('background-color'),
            driver.find_element(By.ID, "city").value_of_css_property('background-color'),
            driver.find_element(By.ID, "country").value_of_css_property('background-color'),
            driver.find_element(By.ID, "job-position").value_of_css_property('background-color'),
            driver.find_element(By.ID, "company").value_of_css_property('background-color')]


def test_red_color():
    Zip_code = driver.find_element(By.ID, "zip-code")
    assert Zip_code.value_of_css_property('background-color') == red_color

def test_green_color():
    for element in new_list:
        assert element == green_color
    






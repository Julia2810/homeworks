from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
sleep(1)

First_name = driver.find_element(By.NAME, "first-name")
First_name.send_keys('Иван')
sleep(1)

Last_name = driver.find_element(By.NAME, 'last-name')
Last_name.send_keys('Петров')
sleep(1)

Address = driver.find_element(By.NAME, 'address')
Address.send_keys('Ленина, 55-3')
sleep(1)

Email = driver.find_element(By.NAME, 'e-mail')
Email.send_keys('test@skypro.com')
sleep(1)

Phone_number = driver.find_element(By.NAME, 'phone')
Phone_number.send_keys('+7985899998787')
sleep(1)

City = driver.find_element(By.NAME, 'city')
City.send_keys('Москва')
sleep(1)

Country = driver.find_element(By.NAME, 'country')
Country.send_keys('Россия')
sleep(1)

Job_position = driver.find_element(By.NAME, 'job-position')
Job_position.send_keys('QA')
sleep(1)

Company = driver.find_element(By.NAME, 'company')
Company.send_keys('SkyPro')
sleep(1)

Submit = driver.find_element(By.TAG_NAME, 'button').click()
sleep(5)


def test_color_zip_code():
    Zip_code = driver.find_element(By.ID, 'zip-code')
    assert Zip_code.value_of_css_property('background-color') == 'rgba(248, 215, 218, 1)'

def test_color_first_name():
    First_name = driver.find_element(By.ID, "first-name")
    assert First_name.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'

def test_color_last_name():
    Last_name = driver.find_element(By.ID, 'last-name')
    assert Last_name.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'

def test_color_address():
    Address = driver.find_element(By.ID, 'address')
    assert Address.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'

def test_color_email():
    Email = driver.find_element(By.ID, 'e-mail')
    assert Email.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'

def test_color_phone_number():
    Phone_number = driver.find_element(By.ID, 'phone')
    assert Phone_number.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'

def test_color_city():
    City = driver.find_element(By.ID, 'city')
    assert City.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'

def test_color_country():
    Country = driver.find_element(By.ID, 'country')
    assert Country.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'

def test_color_job_position():
    Job_position = driver.find_element(By.ID, 'job-position')
    assert Job_position.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'

def test_color_company():
    Company = driver.find_element(By.ID, 'company')
    assert Company.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'
    






from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
sleep(5)

search_locator = 'username'


element1 = driver.find_element(By.NAME, search_locator)
element1.send_keys('tomsmith')
sleep(5)
element2 = driver.find_element(By.NAME, 'password')
element2.send_keys('SuperSecretPassword!')
sleep(5)
element3 = driver.find_element(By.CLASS_NAME, 'fa')
element3.click()
sleep(5)
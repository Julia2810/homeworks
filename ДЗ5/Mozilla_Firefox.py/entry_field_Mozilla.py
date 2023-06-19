from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(5)

search_locator = 'input'


element = driver.find_element(By.TAG_NAME, search_locator)
element.send_keys(1000)
sleep(5)
element.clear()
sleep(5)
element.send_keys(999)

sleep(5)
driver.close()
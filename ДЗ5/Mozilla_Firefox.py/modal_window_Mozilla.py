from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

search_locator = 'modal-footer'


element = driver.find_element(By.CLASS_NAME, search_locator)
element.click()

sleep(5)
driver.close()
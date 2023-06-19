from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

search_locator = 'button'



for element in range(5):
    element = driver.find_element(By.CSS_SELECTOR, search_locator)
    element.click()
    
    
delete_elements = []    
for elements in range(5):
    elements = driver.find_element(By.CLASS_NAME, 'added-manually')
    delete_elements.append(elements)
    
print(len(delete_elements))


sleep(2)
driver.close()

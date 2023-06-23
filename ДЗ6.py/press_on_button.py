from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")


blue_button = driver.find_element(By.ID, 'ajaxButton').click()


green_button = driver.find_element(By.CLASS_NAME, "bg-success").text



print(green_button)
    
    

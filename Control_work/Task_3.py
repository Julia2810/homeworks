from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")


driver.find_element(By.ID,"user-name").send_keys('standard_user')

driver.find_element(By.ID,"password").send_keys('secret_sauce')

driver.find_element(By.ID,"login-button").click()




driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()

driver.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt").click()

driver.find_element(By.NAME,"add-to-cart-sauce-labs-onesie").click()




driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()



driver.find_element(By.ID,"checkout").click()



driver.find_element(By.ID,"first-name").send_keys('Иван')

driver.find_element(By.ID,"last-name").send_keys('Петров')

driver.find_element(By.ID,"postal-code").send_keys(430000)

driver.find_element(By.ID,"continue").click()


print(driver.find_element(By.XPATH,"//div[contains(text(),'Total: $')]").text)


driver.quit()


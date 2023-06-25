from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")


Username = driver.find_element(By.ID,"user-name").send_keys('standard_user')

Password = driver.find_element(By.ID,"password").send_keys('secret_sauce')

Login = driver.find_element(By.ID,"login-button").click()

sleep(2)


Sauce_Labs_Backpack = driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()

Sauce_Labs_Bolt_T_Shirt= driver.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt").click()

Sauce_Labs_Onesie = driver.find_element(By.NAME,"add-to-cart-sauce-labs-onesie").click()

sleep(2)


Cart = driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
sleep(2)


Checkout = driver.find_element(By.ID,"checkout").click()
sleep(2)


First_name = driver.find_element(By.ID,"first-name").send_keys('Иван')

Last_name = driver.find_element(By.ID,"last-name").send_keys('Петров')

Index = driver.find_element(By.ID,"postal-code").send_keys(430000)

Continue = driver.find_element(By.ID,"continue").click()
sleep(2)


Total = driver.find_element(By.XPATH,"//div[contains(text(),'Total: $')]").text

driver.quit()

print(Total)
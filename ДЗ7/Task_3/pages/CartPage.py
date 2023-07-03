from selenium.webdriver.common.by import By



class CartPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/cart.html")


    def click_on_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()
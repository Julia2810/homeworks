from selenium.webdriver.common.by import By
import allure



class ProdPage:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self):
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
from selenium.webdriver.common.by import By
import allure



class ProdPage:

    def __init__(self, browser):
        """
        Функция иницилизирует класс ProdPage,
        в driver передается browser Chrome
        
        """
        self._driver = browser

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self):
        """
        С помощью данной функции осуществляется на сайте добавление товаров в
        корзину путем нажатия на кнопки "Add to cart".
        
        Задаем driver найти элементы по локатору "name".
        
        """
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
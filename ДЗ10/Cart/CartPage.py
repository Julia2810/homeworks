from selenium.webdriver.common.by import By
import allure



class CartPage:
    def __init__(self, browser):
        """
        Функция иницилизирует класс CartPage.
        
        В driver передается browser Chrome.
        
        Открывается страница сайта с помощью метода get.
        
        """
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Подтверждение в корзине добавленных товаров")
    def click_on_checkout(self):
        """
        С помощью данной функции driver находит на странице кнопку "Checkout" по ID и осуществляет по ней клик.
        
        """
        self._driver.find_element(By.ID, "checkout").click()
from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Функция иницилизирует класс LoginPage.
        
        Открывается страница сайта с помощью метода get.
        
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Заполнение поля username: {name}")
    def input_login(self, name: str):
        """
        С помощью данной функции driver находит на странице поле username по ID и осуществляет его заполнение.
        
        """
        self._driver.find_element(By.ID, "user-name").send_keys(name)

    @allure.step("Заполнение поля password: {pas}")
    def input_password(self, pas: str):
        """
        С помощью данной функции driver находит на странице поле password по ID и осуществляет его заполнение.
        
        """
        self._driver.find_element(By.ID, "password").send_keys(pas)

    @allure.step("Нажатие на кнопку Login")
    def click_for_authorization(self):
        """
        Driver находит по ID кнопку "Login" и осуществляет по ней клик.
        
        """
        self._driver.find_element(By.ID, "login-button").click()
from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Заполнение поля username: {name}")
    def input_login(self, name: str):
        self._driver.find_element(By.ID, "user-name").send_keys(name)

    @allure.step("Заполнение поля password: {pas}")
    def input_password(self, pas: str):
        self._driver.find_element(By.ID, "password").send_keys(pas)

    @allure.step("Нажатие на кнопку Login")
    def click_for_authorization(self):
        self._driver.find_element(By.ID, "login-button").click()
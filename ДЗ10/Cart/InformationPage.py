from selenium.webdriver.common.by import By
import allure



class InformationPage:

    def __init__(self, browser):
        """
        Функция иницилизирует класс InformationPage,
        в driver передается browser Chrome
        
        """
        self._driver = browser

    @allure.step("Заполнение поля First name: {name}")
    def input_first_name(self, name: str):
        """
        Функция принимает параметр name(тип данных: строка), driver находит по ID поле First name и осуществляет его заполнение.
        
        """
        self._driver.find_element(By.ID, "first-name").send_keys(name)
        
    @allure.step("Заполнение поля Last name: {surname}")
    def input_last_name(self, surname: str):
        """
        Функция принимает параметр surname(тип данных: строка), driver находит по ID поле Last name и осуществляет его заполнение.
        
        """
        self._driver.find_element(By.ID, "last-name").send_keys(surname)
        
    @allure.step("Заполнение поля Zip/Postal Code: {index}")
    def input_index(self, index: int):
        """
        Функция принимает параметр index(тип данных: число), driver находит по ID поле Zip/Postal Code и осуществляет его заполнение.
        
        """
        self._driver.find_element(By.ID, "postal-code").send_keys(index)
        
    @allure.step("Нажатие на кнопку Continue")
    def click_on_continue(self):
        """
        Driver находит по ID кнопку "Continue" и осуществляет по ней клик.
        
        """
        self._driver.find_element(By.ID, "continue").click()
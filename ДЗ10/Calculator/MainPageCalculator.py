import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Calculator:
    def __init__(self, driver):
        """
        Иницилизируем класс Calculator

        Args:
            driver: название браузера
        """
        self._driver = driver
        self._WebDriverWait = WebDriverWait
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        with allure.step("Очищаем поле ввода количества секунд"):
            self._driver.find_element(By.ID, "delay").clear()

    @allure.step("Введение количества секунд")
    def input_secund(self, number: str):
        """
        Ввод количества секунд для ожидания

        Args:
            number (str): количество секунд
        """
        self._driver.find_element(By.ID, "delay").send_keys(number)

    @allure.step("Нажатие на кнопку с цифрой 7")
    def click_button_7(self):
        """
        Нажатие кнопки с цифрой 7
        """
        self._driver.find_element(By.XPATH,"//span[contains(text(),'7')]").click()

    @allure.step("Нажатие на кнопку +")
    def click_button_plus(self):
        """
        Нажатие кнопки со значением +
        """
        self._driver.find_element(By.XPATH,"//span[contains(text(),'+')]").click()

    @allure.step("Нажатие на кнопку с цифрой 8")
    def click_button_8(self):
        """
        Нажатие кнопки с цифрой 8
        """
        self._driver.find_element(By.XPATH,"//span[contains(text(),'8')]").click()

    @allure.step("Нажатие на кнопку =")
    def click_button_equally(self):
        """
        Нажатие кнопки со значением =
        """
        self._driver.find_element(By.XPATH,"//span[contains(text(),'=')]").click()

    @allure.step("Ожидание драйвера в течение {secunds} секунд до появления результата {result_of_action}")
    def wait_result(self, secunds: int, result_of_action: str):
        """
        Ожидание результата после выполненного действия

        Args:
            secunds (int): количество секунд
            result_of_action (str): ожидаемый результат на экране
        """
        self._WebDriverWait(self._driver, secunds).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), result_of_action))

    @allure.step("Получение результата")
    def test_result_of_sum(self)-> str:
        """
        Получение результата, появившегося на экране

        Returns:
            str: результат
        """
        res = self._driver.find_element(By.CLASS_NAME, "screen").text
        return res
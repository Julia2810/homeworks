from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageCalculator import Calculator
import allure



@allure.title("Проверка калькулятора")
@allure.description("Сравнение результата, полученного после ожидания выполненного действия")
@allure.feature("READ")
@allure.severity("HIGH")
def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator = Calculator(browser)

    with allure.step("Вводим количество секунд, когда должен появиться результат"):
        calculator.input_secund('45')

    with allure.step("Нажимаем на цифру 7"):
        calculator.click_button_7()

    with allure.step("Нажимаем на кнопку +"):
        calculator.click_button_plus()

    with allure.step("Нажимаем на цифру 8"):
        calculator.click_button_8()

    with allure.step("Нажимаем на кнопку ="):
        calculator.click_button_equally()

    with allure.step("Ждем 46 секунд до появления нужного результата 15"):
        calculator.wait_result(46, '15')

    with allure.step("Проверяем результат с суммой на экране"):
        assert calculator.test_result_of_sum() == '15'
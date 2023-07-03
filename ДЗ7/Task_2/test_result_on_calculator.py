from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageCalculator import Calculator




def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator = Calculator(browser)
    calculator.input_secund('45')
    calculator.click_button_7()
    calculator.click_button_plus()
    calculator.click_button_8()
    calculator.click_button_equally()
    calculator.wait_result(46, '15')

    assert calculator.test_result_of_sum() == '15'
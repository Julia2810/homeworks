from selenium.webdriver.common.by import By
import allure



class InformationPage:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Заполнение поля First name: {name}")
    def input_first_name(self, name):
        self._driver.find_element(By.ID, "first-name").send_keys(name)
        
    @allure.step("Заполнение поля Last name: {surname}")
    def input_last_name(self, surname):
        self._driver.find_element(By.ID, "last-name").send_keys(surname)
        
    @allure.step("Заполнение поля Zip/Postal Code: {index}")
    def input_index(self, index):
        self._driver.find_element(By.ID, "postal-code").send_keys(index)
        
    @allure.step("Нажатие на кнопку Continue")
    def click_on_continue(self):
        self._driver.find_element(By.ID, "continue").click()
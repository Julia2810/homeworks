from selenium.webdriver.common.by import By
import allure



class OverviewPage:

    def __init__(self, browser):
        """
        Функция иницилизирует класс OverviewPage,
        в driver передается browser Chrome.
        
        """
        self._driver = browser

    @allure.step("Получение всей суммы заказа")
    def write_of_total(self) -> str:
        """
        Функция с помощью  XPATH находит на странице полную стоимость заказа и возвращает текст в форме строки (str).
        
        """
        total = self._driver.find_element(By.XPATH, "//div[contains(text(),'Total: $')]").text
        return total
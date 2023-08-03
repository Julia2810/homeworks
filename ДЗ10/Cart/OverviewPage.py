from selenium.webdriver.common.by import By
import allure



class OverviewPage:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Получение всей суммы заказа")
    def write_of_total(self) -> str:
        total = self._driver.find_element(By.XPATH, "//div[contains(text(),'Total: $')]").text
        return total
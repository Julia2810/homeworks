from selenium.webdriver.common.by import By



class OverviewPage:

    def __init__(self, browser):
        self._driver = browser


    def write_of_total(self):
        total = self._driver.find_element(By.XPATH, "//div[contains(text(),'Total: $')]").text
        return total
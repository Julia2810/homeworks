from selenium.webdriver.common.by import By



class InformationPage:

    def __init__(self, browser):
        self._driver = browser


    def input_first_name(self, name):
        self._driver.find_element(By.ID, "first-name").send_keys(name)

    def input_last_name(self, surname):
        self._driver.find_element(By.ID, "last-name").send_keys(surname)

    def input_index(self, index):
        self._driver.find_element(By.ID, "postal-code").send_keys(index)

    def click_on_continue(self):
        self._driver.find_element(By.ID, "continue").click()
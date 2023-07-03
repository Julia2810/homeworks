from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    def input_login(self, name):
        self._driver.find_element(By.ID, "user-name").send_keys(name)

    def input_password(self, pas):
        self._driver.find_element(By.ID, "password").send_keys(pas)

    def click_for_authorization(self):
        self._driver.find_element(By.ID, "login-button").click()

  

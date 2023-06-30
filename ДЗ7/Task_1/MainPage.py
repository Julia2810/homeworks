from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage:
    def __init__(self, driver):
        self._new_list = []
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def input_first_name(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(word)

    def input_last_name(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(word)

    def input_address(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(word)

    def input_e_mail(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(word)

    def input_phone(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(word)

    def input_city(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(word)

    def input_country(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(word)

    def input_job_position(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(word)

    def input_company(self, word):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(word)

    def click_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def test_red_color(self):
        color = self._driver.find_element(By.ID, "zip-code").value_of_css_property('background-color')
        return color

    def test_green_color(self):
        new_list = [self._driver.find_element(By.ID, "first-name").value_of_css_property('background-color'),
                    self._driver.find_element(By.ID, "last-name").value_of_css_property('background-color'),
                    self._driver.find_element(By.ID, "address").value_of_css_property('background-color'),
                    self._driver.find_element(By.ID, "e-mail").value_of_css_property('background-color'),
                    self._driver.find_element(By.ID, "phone").value_of_css_property('background-color'),
                    self._driver.find_element(By.ID, "city").value_of_css_property('background-color'),
                    self._driver.find_element(By.ID, "country").value_of_css_property('background-color'),
                    self._driver.find_element(By.ID, "job-position").value_of_css_property('background-color'),
                    self._driver.find_element(By.ID, "company").value_of_css_property('background-color')]

        for element in new_list:
            return element

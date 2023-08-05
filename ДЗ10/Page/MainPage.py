from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


class MainPage:
    def __init__(self, driver):
        """
        Иницилизируем класс MainPage

        Args:
            driver: название браузера
        """
        self._new_list = []
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнение поля First name: {word}")
    def input_first_name(self, word: str):
        """
        Ввод имени

        Args:
            word (str): имя
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(word)

    @allure.step("Заполнение поля Last name: {word}")
    def input_last_name(self, word: str):
        """
        Ввод фамилии

        Args:
            word (str): фамилия
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(word)

    @allure.step("Заполнение поля Address: {word}")
    def input_address(self, word: str):
        """
        Ввод адреса

        Args:
            word (str): адрес
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(word)

    @allure.step("Заполнение поля E-mail: {word}")
    def input_e_mail(self, word: str):
        """
        Ввод адреса эл. почты

        Args:
            word (str): адрес эл. почты
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(word)

    @allure.step("Заполнение поля Phone number: {word}")
    def input_phone(self, word: str):
        """
        Ввод номера телефона

        Args:
            word (str): номер телефона
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(word)

    @allure.step("Заполнение поля City: {word}")
    def input_city(self, word: str):
        """
        Ввод названия города

        Args:
            word (str): город
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(word)

    @allure.step("Заполнение поля Country: {word}")
    def input_country(self, word: str):
        """
        ввод названия страны

        Args:
            word (str): страна
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(word)

    @allure.step("Заполнение поля Job position: {word}")
    def input_job_position(self, word: str):
        """
        Ввод названия должности

        Args:
            word (str): должность
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(word)

    @allure.step("Заполнение поля Company: {word}")
    def input_company(self, word: str):
        """
        Ввод названия компании 

        Args:
            word (str): компания
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(word)

    @allure.step("Нажатие на кнопку Submit")
    def click_submit(self):
        """
        Осуществление клика по кнопке
        """
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    @allure.step("Получение цвета поля Zip-code")
    def test_red_color(self) -> str:
        """
        Получение цвета поля 

        Returns:
            str: название цвета, в формате rgba
        """
        color = self._driver.find_element(By.ID, "zip-code").value_of_css_property('background-color')
        return color

    @allure.step("Получение цвета полей First name, Last name, Address, E-mail, Phone number, City, Country, Job position, Company")
    def test_green_color(self) -> str:
        """
        Получение цвета полей из списка 

        Returns:
            str: название цвета, в формате rgba
        """
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
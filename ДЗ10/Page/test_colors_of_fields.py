from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage
import allure

@allure.title("Заполнение полей формы")
@allure.description("Проверка, что поля подсвечиваются нужными нам цветами")
@allure.feature("CREATE")
@allure.severity("HIGH")
def test_input():
    """
    Тест на проверку цветов полей
    """
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)

    with allure.step("Вводим имя в поле First name"):
        main_page.input_first_name('Иван')

    with allure.step("Вводим фамилию в поле Last name"):
        main_page.input_last_name('Петров')

    with allure.step("Вводим адрес в поле Adress"):
        main_page.input_address('Ленина, 55-3')

    with allure.step("Вводим адрес эл. почты в поле E-mail"):
        main_page.input_e_mail('test@skypro.com')

    with allure.step("Вводим номер телефона в поле Phone number"):
        main_page.input_phone('+7985899998787')

    with allure.step("Вводим название города в поле City"):
        main_page.input_city('Москва')

    with allure.step("Вводим название страны в поле Country"):
        main_page.input_country('Россия')

    with allure.step("Вводим название должности в поле Job position"):
        main_page.input_job_position('QA')

    with allure.step("Вводим название компании в поле Company"):
        main_page.input_company('SkyPro')

    with allure.step("Нажимаем на кнопку Submit"):
        main_page.click_submit()

    with allure.step("Проверка, что поле Zip-code подсвечивается красным цветом"):
        assert main_page.test_red_color() == 'rgba(248, 215, 218, 1)'

    with allure.step("Проверка, что поля First name, Last name, Address, E-mail, Phone number, City, Country, Job position, Company подсвечиваются зеленым цветом"):
        assert main_page.test_green_color() == 'rgba(209, 231, 221, 1)'
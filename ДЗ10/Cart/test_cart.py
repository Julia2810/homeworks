from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage
from ProdPage import ProdPage
from CartPage import CartPage
from InformationPage import InformationPage
from OverviewPage import OverviewPage
import allure


@allure.title("Проверка общей суммы товаров")
@allure.description("Авторизация, заполнение данных, наполнение корзины товарами, проверка общей суммы в корзине")
@allure.feature("CREATE")
@allure.severity("HIGH")
def test_total_of_cart():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Проходим авторизацию, заполняем поля username и password, нажимаем кнопку Login"):
        login_page = LoginPage(browser)
        login_page.input_login('standard_user')
        login_page.input_password('secret_sauce')
        login_page.click_for_authorization()

    with allure.step("Добавляем товары в корзину"):
        prod_page = ProdPage(browser)
        prod_page.add_to_cart()

    with allure.step("Подтверждаем в корзине выбранные нами товары и переходим к заполнению данных о Пользователе"):
        cart_page = CartPage(browser)
        cart_page.click_on_checkout()

    with allure.step("Вводим данные о Пользователе в поля First Name, Last Name, Zip/Postal Code, нажимаем кнопку Continue"):
        information_page = InformationPage(browser)
        information_page.input_first_name('Иван')
        information_page.input_last_name('Петров')
        information_page.input_index(430000)
        information_page.click_on_continue()

    with allure.step("Проверяем, что итоговая сумма совпадает с суммой на экране"):
        overview_page = OverviewPage(browser)
        assert overview_page.write_of_total() == 'Total: $58.29'

    with allure.step("Закрываем браузер"):
        browser.quit()
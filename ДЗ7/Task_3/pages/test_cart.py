from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage
from ProdPage import ProdPage
from CartPage import CartPage
from InformationPage import InformationPage
from OverviewPage import OverviewPage

def test_total_of_cart():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login_page = LoginPage(browser)
    login_page.input_login('standard_user')
    login_page.input_password('secret_sauce')
    login_page.click_for_authorization()

    prod_page = ProdPage(browser)
    prod_page.add_to_cart()

    cart_page = CartPage(browser)
    cart_page.click_on_checkout()

    information_page = InformationPage(browser)
    information_page.input_first_name('Иван')
    information_page.input_last_name('Петров')
    information_page.input_index(430000)
    information_page.click_on_continue()

    overview_page = OverviewPage(browser)
    assert overview_page.write_of_total() == 'Total: $58.29'
    
    browser.quit()
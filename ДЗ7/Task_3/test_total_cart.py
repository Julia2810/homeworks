from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

from TotalCart import TotalCart


def test_total_of_cart():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    total_cart = TotalCart(browser)
    total_cart.input_login('standard_user')
    total_cart.input_password('secret_sauce')
    total_cart.click_for_authorization()
    total_cart.add_cart()
    total_cart.click_on_cart()
    total_cart.click_on_checkout()
    total_cart.input_first_name('Иван')
    total_cart.input_last_name('Петров')
    total_cart.input_index(430000)
    total_cart.click_on_continue()
    total_cart.write_of_total()
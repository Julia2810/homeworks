from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

from MainPage import MainPage

red_color = 'rgba(248, 215, 218, 1)'
green_color = 'rgba(209, 231, 221, 1)'

def test_input():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.input_first_name('Иван')
    main_page.input_last_name('Петров')
    main_page.input_address('Ленина, 55-3')
    main_page.input_e_mail('test@skypro.com')
    main_page.input_phone('+7985899998787')
    main_page.input_city('Москва')
    main_page.input_country('Россия')
    main_page.input_job_position('QA')
    main_page.input_company('SkyPro')
    main_page.click_submit()

    assert red_color == main_page.test_red_color()
    assert green_color == main_page.test_green_color()
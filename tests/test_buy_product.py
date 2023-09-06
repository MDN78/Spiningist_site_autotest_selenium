from selenium import webdriver
import time

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.spinning_page import SpinningPage


def test_buy_product():
    driver = webdriver.Chrome()
    time.sleep(1)
    print("Start Test 1")

    login = LoginPage(driver)
    login.authorization()
    # mp - short name for main page
    mp = MainPage(driver)
    mp.select_spinning_page()
    # sp - short name spinning page
    sp = SpinningPage(driver)
    sp.select_spinning_character()
    sp.select_spinning()
    # bp - short name for basket page
    bp = BasketPage(driver)
    bp.data_entry()

    time.sleep(4)
    driver.close()

import pytest
from selenium import webdriver
import time
# from pages.cart_page import CartPage
# from pages.client_information_page import ClientPage
# from pages.finish_page import FinishPage
from pages.login_page import LoginPage

# from pages.main_page import MainPage
# from pages.payment_page import PaymentPage


def test_buy_product():
    driver = webdriver.Chrome()
    time.sleep(1)
    print("Start Test 1")

    login = LoginPage(driver)
    login.authorization()

    # login = LoginPage(driver)
    # login.authorization()
    # # mp - short name for main page
    # mp = MainPage(driver)
    # mp.select_products_1()
    # # cp - short name for cart_page
    # cp = CartPage(driver)
    # cp.click_checkout_button()
    # #cip - short name for client_information_page
    # cip = ClientPage(driver)
    # cip.input_information()
    # # p - short name for payment_page
    # p = PaymentPage(driver)
    # p.click_finish_button()
    # # fp - short name for finish_page
    # fp = FinishPage(driver)
    # fp.finish()
    # print("Finish test 1")
    time.sleep(1)
    driver.close()
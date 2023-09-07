import time
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.user_info import UserInfo


class BasketPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.SpinningPage = None
        self.driver = driver

    # Locators
    name = "//input[@name='firstname']"
    email = "//input[@name='email']"
    phone = "//input[@name='contact']"

    payment_method = 'naturalPaymentMethods'
    payment_bank_card = "//option[@data-ami-payment-method='stub2']"
    delivery = "//input[@id='shipping_method_11_12']"
    delivery_date_menu = "//select[@name='delivery_date_custom']"
    delivery_date = "//option[@value='13.09.23']"
    metro_menu = "//select[@name='station_custom']"
    metro_station = "//option[@value='Автозаводская']"

    street = "cityAdress"
    house = "citydom"

    comments = "//textarea[@name='comments']"

    word_basket = "//div[@class='b-cmall-page-name__order']"

    # Getters

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_payment_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.payment_method)))

    def get_payment_bank_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_bank_card)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_word_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_basket)))

    def get_delivery_date_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_date_menu)))

    def get_delivery_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_date)))

    def get_metro_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.metro_menu)))

    def get_metro_station(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.metro_station)))

    def get_comments(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comments)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.street)))

    def get_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.house)))

    # Actions

    def input_name(self):
        self.get_name().clear()
        self.get_name().send_keys(UserInfo.name)
        print("Input first name")

    def input_email(self):
        self.get_email().clear()
        self.get_email().send_keys(UserInfo.email)
        print("Input E-MAIL")

    def input_phone(self):
        self.get_phone().send_keys(UserInfo.phone)
        print("Input phone number")

    def select_payment_method(self):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", self.get_payment_method())
        self.get_payment_method().click()
        self.get_payment_bank_card().click()
        print("Select payment method")

    def select_delivery(self):
        self.get_delivery().click()
        print("Select delivery type")

    def input_street(self):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", self.get_street())
        self.get_street().send_keys(UserInfo.street_user)
        print("Input street")

    def input_house(self):
        self.get_house().send_keys(UserInfo.house_user)
        print("Input house")

    def select_delivery_date(self):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", self.get_delivery_date_menu())
        self.get_delivery_date_menu().click()
        self.get_delivery_date().click()
        print("Select delivery date")

    def select_metro_station(self):
        self.driver.execute_script("window.scrollBy(0, 400);")
        self.get_metro_menu().click()
        self.get_metro_station().click()
        print("Select metro station")

    def input_comments(self):
        self.get_comments().send_keys(UserInfo.additional_information)
        print("Input comments")


    # Methods

    def data_entry(self):
        self.get_current_url()
        self.assert_word(self.get_word_basket(), 'Оформление заказа')
        self.input_name()
        self.input_email()
        self.input_phone()
        self.select_payment_method()
        self.select_delivery()
        self.input_street()
        self.input_house()
        self.select_delivery_date()
        self.select_metro_station()
        self.input_comments()
        self.create_screenshot("Final_order")
        time.sleep(3)
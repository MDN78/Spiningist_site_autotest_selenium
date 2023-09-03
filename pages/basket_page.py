import time
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BasketPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name = "//input[@name='firstname']"
    email = "//input[@name='email']"
    phone = "//input[@name='contact']"
    payment_method = "//select[@id='naturalPaymentMethods']"
    payment_bank_card = "//options[@data-ami-payment-method='stub2']"
    delivery = "//input[@id='shipping_method_11_12']"
    word_basket = "//div[@class='b-cmall-page-name__order']"

    # Getters

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_payment_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method)))

    def get_payment_bank_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_bank_card)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_word_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_basket)))

    # Actions

    def input_name(self):
        self.get_name().clear()
        self.get_name().send_keys('Evlampy')
        print("Input first name")

    def input_email(self):
        self.get_email().clear()
        self.get_email().send_keys('test@yandex.ru')
        print("Input E-MAIL")

    def input_phone(self):
        self.get_phone().send_keys('9214445566')
        print("Input phone number")

    # Methods

    def data_entry(self):
        self.get_current_url()
        self.assert_word(self.get_word_basket(), 'Оформление заказа')
        self.input_name()
        self.input_email()
        self.input_phone()
        time.sleep(3)
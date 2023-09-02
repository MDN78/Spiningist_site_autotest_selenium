from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class SpinningPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    spinning_brand = "checkbox_spec_eshop_filter_001003112ext_custom_13[]_11"
    spinning_class = "checkbox_spec_eshop_filter_001003112ext_custom_75[]_5"
    spinning_type = "checkbox_spec_eshop_filter_001003112ext_custom_96[]_1"
    max_price = "//input[@class='cmallFilter__rangeSlider_price_to form-control b-cmall-eshop-filter-spec-cf__item-text b-cmall-eshop-filter-spec-cf__item-text-to']"
    count_section = "checkbox_spec_eshop_filter_001003112ext_custom_77[]_3"

    # Getters
    def get_spinning_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.spinning_brand)))

    def get_spinning_class(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.spinning_class)))

    def get_spinning_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.spinning_type)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_count_section(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.count_section)))

    # Actions

    def click_spinning_brand(self):
        self.get_spinning_brand().click()
        print("Chose spinning brand")

    def click_spinning_class(self):
        self.get_spinning_class().click()
        print("Chose spinning class")

    def click_spinning_type(self):
        self.get_spinning_type().click()
        print("Chose spinning type")

    def click_max_price(self):
        self.get_max_price().send_keys(Keys.BACKSPACE * 6)
        self.get_max_price().send_keys(12000)
        print("Select max price")

    def click_count_section(self):
        self.get_count_section().click()
        print("Chose count section")

    # Methods

    def select_spinning_character(self):
        self.get_current_url()
        self.click_spinning_brand()
        self.click_spinning_class()
        self.click_spinning_type()
        self.click_max_price()
        self.click_count_section()



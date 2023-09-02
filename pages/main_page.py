from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_spinning = "//a[@class='b-menu__link b-menu__link-arr']"

    # Getters
    def get_button_spinning(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_spinning)))

    # Actions

    def click_button_spinning(self):
        self.get_button_spinning().click()
        print("Open spinnings page")

    # Methods

    def select_spinning_page(self):
        self.get_current_url()
        self.click_button_spinning()


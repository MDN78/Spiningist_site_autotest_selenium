from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class LoginPage(Base):

    url = 'https://spinningist.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    enter_account = "//span[@class='hidden-sm hidden-xs b-cmall-members-small_menu_login__item-link-name']"
    user_name = "//input[@id='username']"
    password = "//input[@id='password']"
    button_login = "//button[@class='btn btn-black b-cmall-members-body_small_block__body-button']"
    exit_account = "//span[@class='hidden-sm hidden-xs']"
    word_authorization = "//span[@class='hidden-sm hidden-xs']"


    # Getters
    def get_enter_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_account)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_exit_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exit_account)))

    def get_word_authorization(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_authorization)))

    # Actions
    def click_enter_account(self):
        self.get_enter_account().click()
        print("Open login window")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_user_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_button_login().click()
        print("Click login button")

    def click_exit_account(self):
        self.get_exit_account().click()
        print("Exit account")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_account()
        self.input_user_name("test_login")
        self.input_password("111111test")
        self.click_login_button()
        self.assert_word(self.get_word_authorization(), 'История заказов')


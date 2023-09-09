import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, "Wrong assert word"
        print("Good value word")

    """Method checking by XPATH"""

    def check_exists_by_xpath(self, xpath, search_word):
        try:
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
                (By.XPATH, xpath), search_word))
            print("Desired text was present")
        except TimeoutException:
            print("Desired text was not present")

    """Method for screenshot"""

    def create_screenshot(self, name):
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f"{name}_{current_date}.png"
        self.driver.save_screenshot('C:\\Users\\Dmitry\\Desktop\\git\\Spiningist_site_autotest_selenium\\screen\\'
                                    + name_screenshot)


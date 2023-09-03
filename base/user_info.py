from base.base_class import Base

class UserInfo(Base):
    """General information about user"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Login user info"""
    user = 'test_login'
    passw = '111111test'

    """User general info"""

    name = 'Evlampy'
    email = 'test@yandex.ru'
    phone = '9214445566'

    """Delivery info"""

    street = "Lermontova"
    house = 12
    flat = 234
    metro_station = "Orehovo"
    additional_information = "Delivery after 12 o'clock'"

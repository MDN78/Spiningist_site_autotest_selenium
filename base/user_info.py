from base.base_class import Base

class UserInfo(Base):

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

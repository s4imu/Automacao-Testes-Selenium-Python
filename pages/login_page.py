import conftest
from selenium.webdriver.common.by import By

# Required to be a class
class LoginPage:
    # Class constructor
    def __init__(self):
        self.driver = conftest.driver
        # Working with locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, user, password):
        self.driver.find_element(*self.username_field).send_keys(user)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
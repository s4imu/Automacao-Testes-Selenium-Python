import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Required to be a class
class LoginPage(BasePage): # Heritage
    # Class constructor
    def __init__(self):
        self.driver = conftest.driver
        # Working with locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, user, password):
        # self.driver.find_element(*self.username_field).send_keys(user)
        # self.driver.find_element(*self.password_field).send_keys(password)
        # self.driver.find_element(*self.login_button).click()
        self.type(self.username_field, user)
        self.type(self.password_field, password)
        self.click(self.login_button)
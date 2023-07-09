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
        self.error_message = (By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']")

    def login(self, user, password):
        self.type(self.username_field, user)
        self.type(self.password_field, password)
        self.click(self.login_button)

    def unsuccessful_login_check(self):
       self.check_if_element_exists(self.error_message)
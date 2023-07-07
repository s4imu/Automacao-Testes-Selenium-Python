import conftest
from selenium.webdriver.common.by import By

# Required to be a class
class LoginPage:
    # Class constructor
    def __init__(self):
        self.driver = conftest.driver

    def login(self, user, password):
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
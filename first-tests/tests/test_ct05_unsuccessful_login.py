from selenium.webdriver.common.by import By
import pytest
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT05:

    def test_ct05_unsuccessful_login(self):
        driver = conftest.driver
        # Login
        login_page = LoginPage()
        login_page.login("standard_user","wrong_password")
        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # driver.find_element(By.ID, "password").send_keys("wrong_password")
        # driver.find_element(By.ID, "login-button").click()

        assert driver.find_element(By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']").is_displayed()
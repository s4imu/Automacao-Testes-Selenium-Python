from selenium.webdriver.common.by import By
import pytest
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT01:
    def test_ct01_login_successful(self):
        driver = conftest.driver
        # Trying to login
        login_page = LoginPage()
        login_page.login("standard_user","secret_sauce")
        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # driver.find_element(By.ID, "login-button").click()



        # Checking if redirects to products page
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
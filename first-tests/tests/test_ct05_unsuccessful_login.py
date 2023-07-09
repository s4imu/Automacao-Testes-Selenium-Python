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

        # Check error message
        login_page.unsuccessful_login_check()
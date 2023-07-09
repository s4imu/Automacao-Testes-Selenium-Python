import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT05:

    def test_ct05_unsuccessful_login(self):
        error_message = "Epic sadface: Username and password do not match any user in this service"
        # Login
        login_page = LoginPage()
        login_page.login("standard_user","wrong_password")

        # Check error message
        login_page.unsuccessful_login_check()
        login_page.login_error_message_text_check(error_message)
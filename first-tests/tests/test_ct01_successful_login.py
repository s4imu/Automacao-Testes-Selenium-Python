import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT01:
    def test_ct01_login_successful(self):
        # Trying to login
        login_page = LoginPage()
        home_page = HomePage()
        login_page.login("standard_user","secret_sauce")

        # Checking if redirects to products page
        home_page.successful_login_check()

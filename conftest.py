import pytest
from selenium import webdriver

driver = webdriver.Remote

@pytest.fixture()
def setup_teardown():
    # setup
    global driver # It required to work with the variable previous declarated
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test
    yield

    # teardown
    driver.quit()
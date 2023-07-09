from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")

    def successful_login_check(self):
        self.check_if_element_exists(self.page_title)
from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class InformationPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.expected_title = 'Checkout: Your Information'
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def information_page_redirect_check(self):
        self.page_redirect_check(self.expected_title)

    def fill_form(self,name,surname,zip_code):
        self.type(self.first_name_field, name)
        self.type(self.last_name_field, surname)
        self.type(self.postal_code_field, zip_code)
        self.click(self.continue_button)
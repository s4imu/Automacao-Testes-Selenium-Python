import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class OrderConfirmationPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.expected_title = 'Checkout: Complete!'
        self.message_field = (By.XPATH, "//h2[@class='complete-header']")

    def order_confirmation_redirect_check(self):
        self.page_redirect_check(self.expected_title)

    def order_confirmation_message_check(self, expected_text):
        gotten_text = self.check_element_text(self.message_field)
        assert gotten_text == expected_text, f"Expected text: '{expected_text}' Gotten text: '{gotten_text}'"
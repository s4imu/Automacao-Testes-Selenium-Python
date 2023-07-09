import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class OverviewPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.expected_title = 'Checkout: Overview'
        self.finish_button = (By.ID, "finish")
    def overview_page_redirect_check(self):
        self.page_redirect_check(self.expected_title)

    def finish_buy(self):
        self.click(self.finish_button)
from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.expected_title = "Your Cart"
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.inventory_item = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.checkout_button = (By.ID, "checkout")

    def cart_page_redirect_check(self):
        self.page_redirect_check(self.expected_title)
    def check_item_in_cart(self, item_name):
        item = (self.inventory_item[0], self.inventory_item[1].format(item_name))
        self.check_if_element_exists(item)
    def continue_shopping(self):
        self.click(self.continue_shopping_button)

    def proceed_to_checkout(self):
        self.click(self.checkout_button)
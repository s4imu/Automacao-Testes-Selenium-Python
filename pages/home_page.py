from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.inventory_item = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.add_to_cart_button = (By.XPATH, "//*[text()='Add to cart']")

    def successful_login_check(self):
        self.check_if_element_exists(self.page_title)

    def add_item_to_cart(self, item_name):
         item = (self.inventory_item[0], self.inventory_item[1].format(item_name))
         self.click(item)
         self.click(self.add_to_cart_button)

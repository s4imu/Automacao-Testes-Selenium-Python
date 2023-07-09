import conftest
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def type(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self,locator):
        self.find_element(locator).click()

    def check_if_element_exists(self, locator):
        assert self.find_element(locator).is_displayed(), f"Element '{locator}' not found!!!"

    def check_element_text(self, locator):
        return self.find_element(locator).text

    def page_redirect_check(self, expected_title):
        gotten_title = self.check_element_text(self.page_title)
        assert gotten_title == expected_title, f"Expected text: '{expected_title}' Gotten text: '{gotten_title}'"
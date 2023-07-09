from selenium.webdriver.common.by import By
import pytest
import conftest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.cart
class TestCT02:
    def test_ct02_add_products_to_cart(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        # Login
        login_page.login("standard_user","secret_sauce")

        # Add Products to shopping cart
        home_page.add_item_to_cart('Sauce Labs Backpack')

        # Checking if the product is in shopping cart
        home_page.go_to_cart()
        cart_page.check_item_in_cart('Sauce Labs Backpack')

        driver.find_element(By.ID, "continue-shopping").click()

        # Adding a new product to cart
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()

        driver.find_element(By.ID, "continue-shopping").click()

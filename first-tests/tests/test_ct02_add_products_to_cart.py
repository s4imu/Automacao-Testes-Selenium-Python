from selenium.webdriver.common.by import By
import pytest
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.cart
class TestCT02:
    def test_ct02_add_products_to_cart(self):
        driver = conftest.driver
        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        # Add Products to shopping cart

        # Selecting product
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Checking if the product is in shopping cart
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        driver.find_element(By.ID, "continue-shopping").click()

        # Adding a new product to cart
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()

        driver.find_element(By.ID, "continue-shopping").click()

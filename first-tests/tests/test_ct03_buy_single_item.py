from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buy
class TestCT03:

    def test_ct03_buy_single_item(self):
        driver = conftest.driver
        # Login
        login_page = LoginPage()
        login_page.login("standard_user","secret_sauce")
        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # driver.find_element(By.ID, "login-button").click()

        assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Products']").is_displayed()

        # Add product to cart
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()

        # Proceed to cart
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

        # Implicity wait
        assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Your Cart']").is_displayed()

        # Explicity wait
        # wait.until(ec.text_to_be_present_in_element((By.XPATH, "//span[@class='title']"), "Your Cart"))
        # title_text = driver.find_element(By.XPATH, "//span[@class='title']").text
        # assert title_text == "Your Cart"

        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # Proceed to checkout
        driver.find_element(By.ID, "checkout").click()

        assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Checkout: Your Information']").is_displayed()

        # Fill inputs
        driver.find_element(By.ID, "first-name").send_keys("Symon")
        driver.find_element(By.ID, "last-name").send_keys("Barreto")
        driver.find_element(By.ID, "postal-code").send_keys("69097-760")

        driver.find_element(By.ID, "continue").click()

        # Confirm Pay
        assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Checkout: Overview']")

        driver.find_element(By.ID, "finish").click()

        # Order confirmation
        assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Checkout: Complete!']")
        assert driver.find_element(By.XPATH, "//h2[@class='complete-header' and text()='Thank you for your order!']")

from selenium.webdriver.common.by import By
import conftest
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buy
class TestCT04:

    def test_ct04_buy_many_itens(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        # Login
        login_page.login("standard_user","secret_sauce")

        home_page.successful_login_check()

        # Add first product to cart
        home_page.add_item_to_cart('Sauce Labs Backpack')

        # Proceed to cart
        home_page.go_to_cart()

        cart_page.cart_page_redirect_check()
        cart_page.check_item_in_cart('Sauce Labs Backpack')

        # Add second product to cart
        cart_page.continue_shopping()

        home_page.successful_login_check()

        home_page.add_item_to_cart('Sauce Labs Bike Light')

        # Proceed to cart
        home_page.go_to_cart()

        cart_page.cart_page_redirect_check()
        cart_page.check_item_in_cart('Sauce Labs Backpack')
        cart_page.check_item_in_cart('Sauce Labs Bike Light')

        # Proceed to checkout
        cart_page.proceed_to_checkout()

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


from selenium.webdriver.common.by import By
import conftest
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.information_page import InformationPage
from pages.overview_page import OverviewPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buy
class TestCT04:

    def test_ct04_buy_many_itens(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        information_page = InformationPage()
        overview_page = OverviewPage()

        product_1 = 'Sauce Labs Backpack'
        product_2 = 'Sauce Labs Bike Light'

        first_name = "Symon"
        last_name = "Barreto"
        postal_code = "69097-760"
        # Login
        login_page.login("standard_user","secret_sauce")

        home_page.successful_login_check()

        # Add first product to cart
        home_page.add_item_to_cart(product_1)

        # Proceed to cart
        home_page.go_to_cart()

        cart_page.cart_page_redirect_check()
        cart_page.check_item_in_cart(product_1)

        # Add second product to cart
        cart_page.continue_shopping()

        home_page.successful_login_check()

        home_page.add_item_to_cart(product_2)

        # Proceed to cart
        home_page.go_to_cart()

        cart_page.cart_page_redirect_check()
        cart_page.check_item_in_cart(product_1)
        cart_page.check_item_in_cart(product_2)

        # Proceed to checkout
        cart_page.proceed_to_checkout()

        information_page.information_page_redirect_check()

        # Fill inputs
        information_page.fill_form(first_name, last_name, postal_code)

        # Confirm Pay
        overview_page.overview_page_redirect_check()
        overview_page.finish_buy()

        # Order confirmation
        assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Checkout: Complete!']")
        assert driver.find_element(By.XPATH, "//h2[@class='complete-header' and text()='Thank you for your order!']")


import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.cart
class TestCT02:
    def test_ct02_add_products_to_cart(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()

        product_1 = 'Sauce Labs Backpack'
        product_2 = 'Sauce Labs Bike Light'

        # Login
        login_page.login("standard_user", "secret_sauce")

        # Add Products to shopping cart
        home_page.add_item_to_cart(product_1)

        # Checking if the product is in shopping cart
        home_page.go_to_cart()
        cart_page.cart_page_redirect_check()
        cart_page.check_item_in_cart(product_1)

        cart_page.continue_shopping()

        # Adding a new product to cart
        home_page.add_item_to_cart(product_2)
        home_page.go_to_cart()
        cart_page.cart_page_redirect_check()
        cart_page.check_item_in_cart(product_1)
        cart_page.check_item_in_cart(product_2)

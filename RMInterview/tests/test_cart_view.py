"""
A module to selenium test the Cart view
"""

# Built-in
import unittest

# External
from selenium import webdriver

# Internal
from helpers import authentication_helper, generic_helper
from variables import config, locators


class CartTest(unittest.TestCase):
    """
    A class to initialise the selenium tests
    """
    def setUp(self):
        """
        Opens web browser before each test and sets config variables
        """
        # Setup
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.PATH = config.GenericConfig.frontend_path

        # Config variables
        self.auth_helper = authentication_helper.AuthHelper(self.driver)
        self.generic_helper = generic_helper.GenericHelper(self.driver)
        self.inventory_url = config.Urls.FrontendUrls.Inventory
        self.cart_url = config.Urls.FrontendUrls.Cart
        self.password = config.Inputs.FrontendView.user_password
        self.user_name = config.Inputs.FrontendView.user_name

        # Locators
        self.inventory_locator = locators.Locator().inventory_page
        self.cart_locator = locators.Locator().cart_page

    def test_add_item_view_cart(self):
        """
        Test
            - Login a user
            - Add an item to cart
            - View cart
        Assertions
            - Page is on the cart screen
            - Item added is in the cart
        """
        # Setup variables
        self.driver.get(self.PATH)
        self.auth_helper.login_user(self.user_name, self.password)
        self.generic_helper.click_by_id(self.inventory_locator.get("backpack_add_cart_button"))
        self.generic_helper.click_by_id(self.inventory_locator.get("cart_button"))

        # Method to test
        item_name = self.generic_helper.get_text_by_class(self.cart_locator.get("cart_item"))

        # Assertions
        self.assertEqual(item_name, "Sauce Labs Backpack")
        self.assertEqual(self.driver.current_url, self.cart_url)

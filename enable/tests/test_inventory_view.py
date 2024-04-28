"""
A module to selenium test the Inventory view
"""

# Built-in
import unittest

# External
from selenium import webdriver

# Internal
from helpers import authentication_helper, generic_helper
from variables import config, locators


class InventoryTest(unittest.TestCase):
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
        self.password = config.Inputs.FrontendView.user_password
        self.user_name = config.Inputs.FrontendView.user_name

        # Locators
        self.inventory_locator = locators.Locator().inventory_page

    def tearDown(self):
        """
        Closes browser when finished
        """

        self.driver.quit()
        super().tearDown()

    def test_add_item_to_cart(self):
        """
        Test
            - Login a user
            - Add an item to cart
        Assertions
            - Remove button now visible
        """
        # Setup variables
        self.driver.get(self.PATH)
        self.auth_helper.login_user(self.user_name, self.password)

        # Method to test
        remove_visible_before = self.generic_helper.is_element_visible_by_id(
            self.inventory_locator.get("remove_backpack_button"))
        self.generic_helper.click_by_id(self.inventory_locator.get("backpack_add_cart_button"))
        remove_visible_after = self.generic_helper.is_element_visible_by_id(
            self.inventory_locator.get("remove_backpack_button"))

        # Assertion
        self.assertFalse(remove_visible_before)
        self.assertTrue(remove_visible_after)

    def test_remove_item_from_cart(self):
        """
        Test
            - Login a user
            - Add an item to cart
            - Remove the item from the cart
        Assertions
            - Add to cart button now visible again
        """
        # Setup variables
        self.driver.get(self.PATH)
        self.auth_helper.login_user(self.user_name, self.password)
        self.generic_helper.click_by_id(self.inventory_locator.get("backpack_add_cart_button"))

        # Method to test
        add_cart_visible_before = self.generic_helper.is_element_visible_by_id(
            self.inventory_locator.get("backpack_add_cart_button"))
        self.generic_helper.click_by_id(self.inventory_locator.get("remove_backpack_button"))
        add_cart_visible_after = self.generic_helper.is_element_visible_by_id(
            self.inventory_locator.get("backpack_add_cart_button"))

        # Assertion
        self.assertFalse(add_cart_visible_before)
        self.assertTrue(add_cart_visible_after)

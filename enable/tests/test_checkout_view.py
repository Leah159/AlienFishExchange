"""
A module to selenium test the Checkout view
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
        self.checkout_complete_url = config.Urls.FrontendUrls.CheckoutComplete
        self.checkout_step_one_url = config.Urls.FrontendUrls.CheckoutStepOne
        self.generic_helper = generic_helper.GenericHelper(self.driver)
        self.password = config.Inputs.FrontendView.user_password
        self.responses = config.Responses.CheckoutView
        self.user_name = config.Inputs.FrontendView.user_name

        # Locators
        self.inventory_locator = locators.Locator().inventory_page
        self.cart_locator = locators.Locator().cart_page
        self.checkout_locator = locators.Locator().checkout_page

    def test_checkout_successfully(self):
        """
        Test
            - Login a user
            - Add an item to cart
            - Go to cart and checkout
            - Fill in customer details
            - Confirm purchase
        Assertions
            - Page is on the checkout complete screen
        """
        # Setup variables
        self.driver.get(self.PATH)
        self.auth_helper.login_user(self.user_name, self.password)
        self.generic_helper.click_by_id(self.inventory_locator.get("backpack_add_cart_button"))
        self.generic_helper.click_by_id(self.inventory_locator.get("cart_button"))
        self.generic_helper.click_by_id(self.cart_locator.get("checkout_button"))

        # Method under test
        self.generic_helper.enter_text_by_id("Test", self.checkout_locator.get("first_name_text"))
        self.generic_helper.enter_text_by_id("User", self.checkout_locator.get("last_name_text"))
        self.generic_helper.enter_text_by_id("TE11 1ST", self.checkout_locator.get("post_code_text"))
        self.generic_helper.click_by_id(self.checkout_locator.get("continue_button"))
        self.generic_helper.click_by_id(self.checkout_locator.get("finish_button"))

        # Assertions
        self.assertEqual(self.driver.current_url, self.checkout_complete_url)

    def test_checkout_no_user_details(self):
        """
        Test
            - Login a user
            - Add an item to cart
            - Go to cart and checkout
            - Confirm purchase
        Assertions
            - Page is on the checkout step one screen
        """
        # Setup variables
        self.driver.get(self.PATH)
        self.auth_helper.login_user(self.user_name, self.password)
        self.generic_helper.click_by_id(self.inventory_locator.get("backpack_add_cart_button"))
        self.generic_helper.click_by_id(self.inventory_locator.get("cart_button"))
        self.generic_helper.click_by_id(self.cart_locator.get("checkout_button"))

        # Method under test
        self.generic_helper.click_by_id(self.checkout_locator.get("continue_button"))
        error_text = self.generic_helper.get_text_by_css(self.checkout_locator.get("error_text"))

        # Assertions
        self.assertEqual(self.driver.current_url, self.checkout_step_one_url)
        self.assertEqual(self.responses.no_first_name, error_text)

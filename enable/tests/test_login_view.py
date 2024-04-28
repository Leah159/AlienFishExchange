"""
A module to selenium test the Login view
"""

# Built-in
import time
import unittest

# External
from selenium import webdriver

# Internal
from helpers import authentication_helper, generic_helper
from variables import config, locators


class LoginAccountTest(unittest.TestCase):
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
        self.password_error = config.Inputs.FrontendView.failed_password
        self.user_name = config.Inputs.FrontendView.user_name
        self.responses = config.Responses.LoginView

        # Locators
        self.login_locator = locators.Locator().login_page
        self.inventory_locator = locators.Locator().inventory_page

    def tearDown(self):
        """
        Closes browser when finished
        """

        self.driver.quit()
        super().tearDown()

    def test_login_account_success(self):
        """
        Test
            - Login a user successfully into their account
        Assertions
            - Page is moved to the Inventory view
        """
        # Method to test
        self.driver.get(self.PATH)
        self.generic_helper.enter_text_by_id(self.user_name, self.login_locator.get("username_field"))
        self.generic_helper.enter_text_by_id(self.password, self.login_locator.get("password_field"))
        self.generic_helper.click_by_id(self.login_locator.get("login_button"))

        # Assertions
        self.assertEqual(self.driver.current_url, self.inventory_url)

    def test_login_account_failed(self):
        """
        Test
            - Login a user in with invalid credentials
        Assertions
            - Page does not redirect
            - Login failed message is displayed on the screen
        """
        # Method to test
        self.driver.get(self.PATH)
        self.generic_helper.enter_text_by_id(self.user_name, self.login_locator.get("username_field"))
        self.generic_helper.enter_text_by_id(self.password_error, self.login_locator.get("password_field"))
        self.generic_helper.click_by_id(self.login_locator.get("login_button"))
        error_text = self.generic_helper.get_text_by_css(self.login_locator.get("error_text"))

        # Assertions
        self.assertEqual(self.driver.current_url, self.PATH)
        self.assertEqual(error_text, self.responses.login_failed)

    def test_login_empty_fields(self):
        """
        Test
            - Login without entering any data into the required fields
        Assertions
            - Login failed is displayed on the screen
            - Page does not redirect
        """
        # Method to test
        self.driver.get(self.PATH)
        self.generic_helper.click_by_id(self.login_locator.get("login_button"))
        error_text = self.generic_helper.get_text_by_css(self.login_locator.get("error_text"))

        # Assertion
        self.assertEqual(error_text, self.responses.username_required)
        self.assertEqual(self.driver.current_url, self.PATH)

    def test_logout_successful(self):
        """
        Test
            - Login successfully using their credentials
            - Logout the user
        Assertions
            - Page is back on the login screen
        """
        # Setup variables
        self.driver.get(self.PATH)
        self.auth_helper.login_user(self.user_name, self.password)
        time.sleep(1)

        # Method to test
        self.generic_helper.click_by_id(self.inventory_locator.get("burger_menu"))
        self.generic_helper.click_by_id(self.inventory_locator.get("logout_button"))

        # Assertion
        self.assertEqual(self.driver.current_url, self.PATH)

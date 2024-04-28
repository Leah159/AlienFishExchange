"""
Module containing AuthHelper class
"""

# Built-in

# Internal
from helpers import generic_helper
from variables import config, locators


class AuthHelper:
    """
    Class containing authentication helper functions for assisting testing
    """
    def __init__(self, driver):
        """
        Method to initialise the variables needed in the authentication helper
        """
        # Config Variables
        self.driver = driver
        self.generic_config = config.GenericConfig
        self.generic_helper = generic_helper.GenericHelper(self.driver)
        self.locator = locators.Locator().login_page

    def login_user(self, user_name, password):
        """
        Method to log in a user account
        :param user_name: Username used to log in to a user account
        :param password: Password used to log in to a user account
        """
        self.generic_helper.enter_text_by_id(user_name, self.locator.get("username_field"))
        self.generic_helper.enter_text_by_id(password, self.locator.get("password_field"))
        self.generic_helper.click_by_id(self.locator.get("login_button"))

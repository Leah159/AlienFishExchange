"""
A module to hold config variables for selenium tests
"""


class GenericConfig:
    """
    A class to hold generic config for application
    """
    frontend_path = 'https://www.saucedemo.com/'


class Inputs:
    """
    A class to store test inputs
    """

    class FrontendView:
        """
        A class to store test inputs for the Register and Login view
        """
        failed_password = "TestPassword"
        user_name = "standard_user"
        user_password = "secret_sauce"


class Responses:
    """
    A class to store response data from tests
    """

    class LoginView:
        """
        A class to store response data from Login view tests
        """
        login_failed = "Epic sadface: Username and password do not match any user in this service"
        username_required = "Epic sadface: Username is required"

    class CheckoutView:
        """
        A class to store response data from Checkout view tests
        """
        no_first_name = "Error: First Name is required"


class Urls:
    class FrontendUrls:
        """
        A class to store Frontend Urls
        """
        Cart = f"{GenericConfig.frontend_path}cart.html"
        CheckoutComplete = f"{GenericConfig.frontend_path}checkout-complete.html"
        CheckoutStepOne = f"{GenericConfig.frontend_path}checkout-step-one.html"
        Inventory = f"{GenericConfig.frontend_path}inventory.html"


class Config:
    """
    A class where all configs can be referenced
    """
    GenericConfig = GenericConfig
    Inputs = Inputs
    Urls = Urls
    Responses = Responses

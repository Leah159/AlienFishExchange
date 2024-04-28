"""
A module to hold the locators class for finding ui elements
"""


class Locator:
    """
    A class to locate UI elements
    """

    cart_page = {
        "cart_item": "inventory_item_name",
        "checkout_button": "checkout",
    }

    checkout_page = {
        "continue_button": "continue",
        "error_text": "h3[data-test=\"error\"]",
        "finish_button": "finish",
        "first_name_text": "first-name",
        "last_name_text": "last-name",
        "post_code_text": "postal-code",
    }

    inventory_page = {
        "backpack_add_cart_button": "add-to-cart-sauce-labs-backpack",
        "burger_menu": "react-burger-menu-btn",
        "cart_button": "shopping_cart_container",
        "logout_button": "logout_sidebar_link",
        "remove_backpack_button": "remove-sauce-labs-backpack",
    }

    login_page = {
        "error_text": "h3[data-test=\"error\"]",
        "login_button": "login-button",
        "password_field": "password",
        "username_field": "user-name",
    }

"""
A module to store global variables
"""

# Built-in
import os


class GenericConfig:
    """
    A class to hold generic config for application
    """
    api_url = "http://127.0.0.1:5000"
    database_path = os.path.dirname(__file__) + "\\db\\alifex_db.db"

    class _Urls:
        """
        A class to hold API endpoints
        """

        def __init__(self, api_url):
            """
            Initialises the class with API URLs for various resources.
            :param api_url: Base URL of the API.
            """

            self.fish = f"{api_url}/fish"
            self.user = f"{api_url}/user"

    urls = _Urls(api_url)

    class ResponseKeys:
        """
        A class to hold response keys for server requests
        """
        data = "data"
        error = "error"
        group_id = "group_id"
        message = "message"
        project_id = "project_id"
        success = "success"
        token = "token"

    class SuccessStatus:
        """
        A class to hold boolean value keys for whether a request was successful
        """
        failed = False
        passed = True

    class ValidationMessages:
        """
        A class to hold response messages for schema validation
        """
        invalid = "Request body doesn't match the specified Schema."
        invalid_route = "Invalid route operation."


class UsersConfig:
    """
    A class to hold config specific to the users table and endpoint
    """

    class ResponseMessages:
        """
        A class to hold response messages for requests
        """

        kudos_amount_updated = "Kudos amount updated"
        user_created_failed = "Email or username is already being used by another user."
        user_created_success = "User created successfully."
        user_found = "User found"
        user_not_found = "User not found"
        invalid_credentials = "The user did not provide valid credentials"

    class RequestKeys:
        """
        A class to hold request keys for requests
        """
        email = "email"
        kudos = "kudos"
        password = "password"
        user_id = "user_id"
        username = "username"


class FishConfig:
    """
    A class to hold config specific to the fish table and endpoint
    """

    class ResponseMessages:
        """
        A class to hold response messages for requests
        """

        fish_created_success = "Fish created successfully."
        fish_frozen_success = "Fish frozen successfully."
        fish_not_found = "No fish found under this user id"
        fish_sold_success = "Fish sold successfully"
        fish_unfrozen_success = "Fish unfrozen successfully."

    class RequestKeys:
        """
        A class to hold request keys for requests
        """
        fish_type: "fish_type"
        birth_weight: "birth_weight"
        daily_weight_increase: "daily_weight_increase"
        mutation_day: "mutation_day"
        fertile_day: "fertile_day"
        buy_cost: "buy_cost"
        sell_cost: "sell_cost"


class GameConfig:
    """
    A class to hold config specific to the game endpoint
    """

    class ResponseMessages:
        """
        A class to hold response messages for requests
        """

        game_advanced_success = "Game advanced successfully"


class Config:
    """
    A class where all configs can be referenced
    """
    FishConfig = FishConfig
    GameConfig = GameConfig
    GenericConfig = GenericConfig
    UsersConfig = UsersConfig

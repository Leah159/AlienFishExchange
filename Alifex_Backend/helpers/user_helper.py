"""
A module containing helper functions for the users table and endpoint
"""

# Internal
from config import Config, UsersConfig

ResponseKeys = UsersConfig.RequestKeys
user_url = Config.GenericConfig.urls.user


def format_user_details(user):
    """
    A function to format the user details into an object format for authentication
    :param user: The user to format into an object
    :return: User formatted as an object
    """
    return {
        ResponseKeys.user_id: user[0],
        ResponseKeys.email: user[1],
        ResponseKeys.username: user[2],
        ResponseKeys.password: user[3]
    }

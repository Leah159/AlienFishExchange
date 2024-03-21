"""
A module for managing the login endpoint methods
"""

# Built-in
from operator import itemgetter

# External
import bcrypt
import requests.exceptions

# Internal
from config import Config
from db_manager import DatabaseManager
from helpers.response_formatter import (
    format_bad_request_response,
    format_error_response,
    format_ok_response,
)

RequestKeys = Config.UsersConfig.RequestKeys
ResponseKeys = Config.GenericConfig.ResponseKeys
ResponseMessages = Config.UsersConfig.ResponseMessages


def login_user(request):
    """
    A function to handle the post method for the login endpoint
    :param request: Incoming post request for login endpoint
    :return: Request response
    """
    body = request.json
    email, password = itemgetter('email', 'password')(body)

    try:
        with DatabaseManager(Config.GenericConfig.database_path) as database:
            database.get_database_version()
            user_exists = database.users.get_user_by_email(email)
            if user_exists:
                if bcrypt.checkpw(bytes(password, 'utf-8'), user_exists.get(RequestKeys.password)):
                    user_id = user_exists.get(RequestKeys.user_id)
                    data = {"user_id": user_id}
                    response = format_ok_response({ResponseKeys.data: data})
                else:
                    response = format_bad_request_response({ResponseKeys.message: ResponseMessages.invalid_credentials})
            else:
                return format_bad_request_response({ResponseKeys.message: ResponseMessages.invalid_credentials})

    except requests.exceptions.RequestException as error:
        response = format_error_response({ResponseKeys.error: error})

    return response

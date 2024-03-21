"""
A module for managing the users endpoint methods
"""

# Built-in
from operator import itemgetter
import requests.exceptions

# Internal
from config import Config
from db_manager import DatabaseManager
from helpers.response_formatter import (
    format_bad_request_response,
    format_error_response,
    format_not_found_response,
    format_ok_response
)

RequestKeys = Config.UsersConfig.RequestKeys
ResponseKeys = Config.GenericConfig.ResponseKeys
ResponseMessages = Config.UsersConfig.ResponseMessages


def post_user(request):
    """
    A function to handle the post method for the user's endpoint
    :param request: Incoming post request for user endpoint
    :return: Request response
    """
    body = request.json
    email, password, username = itemgetter('email', 'password', 'username')(body)

    try:
        with DatabaseManager(Config.GenericConfig.database_path) as database:
            database.get_database_version()
            email_exists = database.users.get_user_by_email(email)
            username_exists = database.users.get_user_by_username(username)
            if not username_exists and not email_exists:
                user_id = database.users.create_user(email, username, password, 10000, 0, 0)
                database.fish.create_fish(
                    user_id, "White Sprat", "Sprat", 100, 0, False, 1, 1, 0)
                database.users.update_users_fish(user_id)
                response = format_ok_response({ResponseKeys.message: ResponseMessages.user_created_success})
            else:
                response = format_bad_request_response({ResponseKeys.error: ResponseMessages.user_created_failed})
    except requests.exceptions.RequestException as error:
        response = format_error_response({ResponseKeys.error: error})
    return response


def patch_user(request):
    """
    A function to handle the PATCH method for the user endpoint
    :param request: Incoming PATCH request
    :return: Request response
    """
    body = request.json
    try:
        with DatabaseManager(Config.GenericConfig.database_path) as database:
            database.get_database_version()
            # If kudos key is in the request body
            if RequestKeys.kudos in body.keys():
                user_id, kudos = itemgetter('user_id', 'kudos')(body)
                database.users.update_user_kudos_amount(user_id, kudos)
                response = format_ok_response({ResponseKeys.message: ResponseMessages.kudos_amount_updated})
    except requests.exceptions.RequestException as error:
        response = format_error_response({ResponseKeys.error: error})
    return response


def get_user_by_id(user_id):
    """
    A function to handle the get method for the user endpoint to return a specific user by their user_id
    :param user_id: Incoming GET request user_id parameter
    :return: User GET request response
    """
    try:
        with DatabaseManager(Config.GenericConfig.database_path) as database:
            database.get_database_version()
            fetched_user = database.users.get_user_by_id(user_id)
        if fetched_user:
            response = format_ok_response({
                ResponseKeys.message: ResponseMessages.user_found,
                ResponseKeys.data: {
                    "email": fetched_user[1],
                    "user_id": user_id,
                    "username": fetched_user[2],
                    "kudos": fetched_user[4],
                    "fish_count": fetched_user[5],
                    "user_age": fetched_user[6]
                }
            })
        else:
            response = format_not_found_response({ResponseKeys.error: ResponseMessages.user_not_found})
    except requests.exceptions.RequestException as error:
        response = format_error_response({ResponseKeys.error: error})
    return response

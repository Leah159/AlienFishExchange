"""
A module for managing the fish endpoint methods
"""

# Built-in
from operator import itemgetter
import requests.exceptions

# Internal
from config import Config
from db_manager import DatabaseManager
from helpers.fish_helper import get_fish_data_by_name
from helpers.response_formatter import (
    format_error_response,
    format_not_found_response,
    format_ok_response
)

ResponseKeys = Config.GenericConfig.ResponseKeys
ResponseMessages = Config.FishConfig.ResponseMessages


def post_fish(request):
    """
    A function to handle the post method for the fish endpoint
    :param request: Incoming post request for fish endpoint
    :return: Request response
    """
    body = request.json
    user_id, name, quantity = itemgetter('user_id', 'name', 'quantity')(body)
    fish_info = get_fish_data_by_name(name)
    try:
        with DatabaseManager(Config.GenericConfig.database_path) as database:
            database.get_database_version()
            if database.fish.check_existing_fish_entry(user_id, name, 0, False):
                database.fish.update_quantity_fish(user_id, name, 0, quantity, False)
            else:
                current_value = fish_info['birth_weight'] * fish_info['sell_cost']
                database.fish.create_fish(
                    user_id, name, fish_info['fish_type'], quantity, 0, False, fish_info['birth_weight'], current_value, 0)
            database.users.update_users_fish(user_id)
            response = format_ok_response({ResponseKeys.message: ResponseMessages.fish_created_success})
    except requests.exceptions.RequestException as error:
        response = format_error_response({ResponseKeys.error: error})
    return response


def patch_fish(request):
    """
    A function to handle the patch method for the fish endpoint
    :param request: Incoming patch request for fish endpoint
    :return: Request response
    """

    body = request.json
    user_id, fish_id, quantity, sell, freeze = itemgetter('user_id', 'fish_id', 'quantity', 'sell', 'freeze')(body)

    try:
        with DatabaseManager(Config.GenericConfig.database_path) as database:
            database.get_database_version()

            if sell:
                name, age = database.fish.get_fish_name_and_age(fish_id)
                database.fish.update_quantity_fish(user_id, name, age, -quantity, False)
                response = format_ok_response({ResponseKeys.message: ResponseMessages.fish_sold_success})
            else:
                if freeze:
                    database.fish.freeze_fish(fish_id, quantity)
                    response = format_ok_response({ResponseKeys.message: ResponseMessages.fish_frozen_success})
                else:
                    database.fish.unfreeze_fish(fish_id, quantity)
                    response = format_ok_response({ResponseKeys.message: ResponseMessages.fish_unfrozen_success})

            database.users.update_users_fish(user_id)

    except requests.exceptions.RequestException as error:
        response = format_error_response({ResponseKeys.error: error})
    return response


def get_fish_by_user_id(user_id):
    """
    A function to handle the get method for the user endpoint to return a specific user by their user_id
    :param user_id: Incoming GET request user_id parameter
    :param frozen: Boolean of whether to fetch only unfrozen fish or frozen fish
    :return: User GET request response
    """
    try:
        with DatabaseManager(Config.GenericConfig.database_path) as database:
            database.get_database_version()
            fetched_fish = database.fish.get_fish_list_by_user_id(user_id, False)
        if fetched_fish:
            data = {ResponseKeys.data: fetched_fish}
            response = format_ok_response(data)
        else:
            response = format_not_found_response({ResponseKeys.error: ResponseMessages.fish_not_found})
    except requests.exceptions.RequestException as error:
        response = format_error_response({ResponseKeys.error: error})
    return response

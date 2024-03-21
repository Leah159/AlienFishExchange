"""
This module is the main which uses the database manager module
"""

# External
from flask import Flask, request
from flask_cors import CORS, cross_origin

# Internal
from config import Config
from controllers.authentication_controller import login_user
from controllers.fish_controller import (
    post_fish, patch_fish, get_fish_by_user_id
)
from controllers.game_controller import (
    advance_day
)
from controllers.user_controller import (
    patch_user,
    post_user, get_user_by_id
)
from db_manager import DatabaseManager
from helpers.response_formatter import (
    format_bad_request_response,
)
from validation.fish_schema import fish_post_schema, fish_patch_schema
from validation.login_schema import login_post_schema
from validation.user_schema import user_patch_schema, user_post_schema
from validation.validate_schema import validate_json

ResponseKeys = Config.GenericConfig.ResponseKeys
ValidationMessages = Config.GenericConfig.ValidationMessages

app = Flask(__name__)
CORS(app)
database_path = Config.GenericConfig.database_path


def main():
    """
    A function which runs when the script is executed
    """
    with DatabaseManager(database_path) as database:
        database.create_tables()
    app.run(host='0.0.0.0')


@app.route('/user', methods=['POST', 'PATCH'])
@cross_origin(expose_headers="*")
def user():
    """
    A function for handling the user endpoint
    :return: Request response
    """
    if request.method == 'POST':
        if validate_json(request.json, user_post_schema):
            return post_user(request)
        return format_bad_request_response({ResponseKeys.error: ValidationMessages.invalid})
    if request.method == 'PATCH':
        if validate_json(request.json, user_patch_schema):
            return patch_user(request)
        return format_bad_request_response({ResponseKeys.error: ValidationMessages.invalid})
    return format_bad_request_response({ResponseKeys.error: ValidationMessages.invalid_route})


@app.route('/user/id/<int:user_id>', methods=['GET'])
@cross_origin(expose_headers="*")
def get_user_record_by_id(user_id):
    """
    A function for handling the user's GET endpoint
    :param: User's username
    :return: Request response
    """
    return get_user_by_id(user_id)


@app.route('/fish/id/<int:user_id>', methods=['GET'])
@cross_origin(expose_headers="*")
def get_fish_list_by_user_id(user_id):
    """
    A function for handling the user's GET endpoint
    :param: User's username
    :return: Request response
    """
    return get_fish_by_user_id(user_id)


@app.route('/fish', methods=['POST', 'PATCH'])
@cross_origin(expose_headers="*")
def fish():
    """
    A function for handling the user endpoint
    :return: Request response
    """
    if request.method == 'POST':
        if validate_json(request.json, fish_post_schema):
            return post_fish(request)
        return format_bad_request_response({ResponseKeys.error: ValidationMessages.invalid})
    if request.method == 'PATCH':
        if validate_json(request.json, fish_patch_schema):
            return patch_fish(request)
        return format_bad_request_response({ResponseKeys.error: ValidationMessages.invalid})
    return format_bad_request_response({ResponseKeys.error: ValidationMessages.invalid_route})


@app.route('/game/<int:user_id>', methods=['GET'])
@cross_origin(expose_headers="*")
def advance_day_user(user_id):
    """
    A function for handling advancing the day endpoint
    :param: User's user id
    """
    return advance_day(user_id)


@app.route('/login', methods=['POST'])
@cross_origin(expose_headers="*")
def login():
    """
    A function for handling the login endpoint
    :return: Request response
    """
    if request.method == 'POST':
        if validate_json(request.json, login_post_schema):
            return login_user(request)
        return format_bad_request_response({ResponseKeys.error: ValidationMessages.invalid})
    return format_bad_request_response({ResponseKeys.error: ValidationMessages.invalid_route})


if __name__ == '__main__':
    main()

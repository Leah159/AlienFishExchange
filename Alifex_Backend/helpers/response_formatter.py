"""
A module for formatting request responses
"""

# Built-in
from http import HTTPStatus

# External
from flask import jsonify

# Internal
from config import Config

SuccessStatus = Config.GenericConfig.SuccessStatus


def format_bad_request_response(data):
    """
    A function to format bad request error responses
    :param data: Data of the response
    :return: Formatted response
    """
    data["success"] = SuccessStatus.failed
    response = jsonify(data)
    response.status_code = HTTPStatus.BAD_REQUEST
    return response


def format_error_response(data):
    """
    A function to format request server error responses
    :param data: Data of the response
    :return: Formatted response
    """
    data["success"] = SuccessStatus.failed
    response = jsonify(data)
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return response


def format_ok_response(data):
    """
    A function to format ok request responses
    :param data: Data of the response
    :return: Formatted response
    """
    data["success"] = SuccessStatus.passed
    response = jsonify(data)
    response.status_code = HTTPStatus.OK
    return response


def format_not_found_response(data):
    """
    A function to format not found request responses
    :param data: Data of the response
    :return: Formatted response
    """
    data["success"] = SuccessStatus.failed
    response = jsonify(data)
    response.status_code = HTTPStatus.NOT_FOUND
    return response

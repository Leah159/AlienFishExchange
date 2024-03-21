"""
A module to validate a json schema
"""

# External
import jsonschema
from jsonschema import validate


def validate_json(json_data, schema):
    """
    A function to validate json data against a schema
    :param json_data:Json data to validate
    :param schema: Schema for data to be validated against
    :return: Json validity against schema
    """
    try:
        validate(instance=json_data, schema=schema)
        valid_json = True
    except jsonschema.exceptions.ValidationError:
        valid_json = False
    return valid_json

"""
A module to handle the schemas for the users endpoint
"""

user_post_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "username": {"type": "string", "minLength": 5, "maxLength": 15},
        "password": {
            "type": "string",
            "maxLength": 24,
            "pattern": "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
        },
    },
    "required": ["email", "username", "password"]
}

user_patch_schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "kudos": {"type": "integer"},
    },
    "oneOf": [
        {"required": ["user_id", "kudos"]},
    ],
}
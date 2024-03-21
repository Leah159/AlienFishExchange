"""
A module to handle the schemas for the fish endpoint
"""

fish_post_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "quantity": {"type": "integer"},
    },
    "required": ["name", "quantity"]
}

fish_patch_schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "fish_id": {"type": "integer"},
        "quantity": {"type": "integer"},
        "sell": {"type": "boolean"},
        "freeze": {"type": "boolean"}
    },
    "required": ["user_id", "fish_id", "quantity","sell", "freeze"]
}

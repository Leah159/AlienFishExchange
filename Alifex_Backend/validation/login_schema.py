"""
A module to handle the schemas for the login endpoint
"""

login_post_schema = {
    "type": "object",
    "properties": {"email": {"type": "string"}, "password": {"type": "string"}},
    "required": ["email", "password"]
}

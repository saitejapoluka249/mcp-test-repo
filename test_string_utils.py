# test_string_utils.py
from string_utils import greet_user

def test_greet_user():
    # This will fail because the function returns "HelloJohn" instead of "Hello John"
    assert greet_user("John") == "Hello John"
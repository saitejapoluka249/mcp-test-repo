# test_string_utils.py
from string_utils import greet_user

def test_greet_user():
    # Corrected: The function returns "Hello John" with a space
    assert greet_user("John") == "Hello John"
    # Additional test cases
    assert greet_user("") == "Hello "
    assert greet_user("@!#") == "Hello @!#"

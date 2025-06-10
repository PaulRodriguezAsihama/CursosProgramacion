import re
import string


def valid_password(user_password, nums=1, special_chars=1, uppercase=1, lowercase=1):
    if len(user_password) < 8:
        return print("invalid password: must be at least 8 characters")
    constraints = [
        (nums, r'\d'),
        (special_chars, fr'[{string.punctuation}]'),
        (uppercase, r'[A-Z]'),
        (lowercase, r'[a-z]')
    ]
    if all(constraint <= len(re.findall(pattern, user_password)) for constraint, pattern in constraints):
        return print("valid password")
    else:
        return print("invalid password")


password = "User123@_{"

valid_password(password)

import string
import re


def password_validation(password, num=1, special_character=1, uppercase=1, lowercase=1):
    if len(password) < 8:
        return print("password must be at least 8 characters")
    constraints = [(num, r'\d'), (special_character,
                                  fr'[{string.punctuation}]'), (uppercase, r'[A-Z]'), (lowercase, r'[a-z]')]
    if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):
        return print("valid password")
    else:
        return print("invalid password")


# test
password = "Out123#_sss{"
password_validation(password)

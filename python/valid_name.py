import re


def name_validation(name):
    pattern = f'^[A-Z][a-z]+ [A-Z][a-z]+$'
    test = bool(re.match(pattern, name))
    if test:
        return print("name valid")
    else:
        return print("name invalid")


# test
user_name = "JhonDoe"
name_validation(user_name)

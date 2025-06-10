import re


def email_validation(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    test = bool(re.match(pattern, email))
    if test:
        return print("valid email")
    else:
        return print("invalid email")


# test
email = "Jhon.Doe@gmail.com"
email_validation(email)

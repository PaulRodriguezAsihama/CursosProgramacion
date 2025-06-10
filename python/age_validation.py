from datetime import datetime


def age_validation(birth_date, min_age=18):
    date_of_birth = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - date_of_birth.year - \
        ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    if age >= 18:
        return print("is older than 18")
    else:
        return print("is younger than 18")


# test
birth_date = "2015-12-15"
age_validation(birth_date)

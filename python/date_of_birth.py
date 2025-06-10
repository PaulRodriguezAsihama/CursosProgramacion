from datetime import datetime


def is_adult(birthday):
    date_of_birth = datetime.strptime(birthday, '%Y-%m-%d')
    today = datetime.today()
    age = today.year-date_of_birth.year - \
        ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age >= 18


date_user = "2015-06-06"
if is_adult(date_user):
    print("is older than 18")
else:
    print("is younger than 18")

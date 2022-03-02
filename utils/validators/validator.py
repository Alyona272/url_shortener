import re


def validate_email(email: str) -> bool:
    if re.search(r"[a-z, 1-9]*@[a-z]*.[a-z]*", email):
        return True
    return False


def validate_login(login: str) -> bool:
    if re.search(r"\s|[^a-z, _]", login) or len(login) == 0:
        return False
    return True


def validate_phone_number(phone_number: str) -> bool:
    if re.search(r"(\+79[0-9]{7}\b)|(89[0-9]{7}\b)", phone_number):
        return True
    return False


def validate_url(url: str) -> bool:
    if re.search(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", url):
        return True
    return False

import re


def validate_required(value):
    value = value.strip()
    if not value:
        raise ValueError("This field is required.")
    return value


def validate_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()))


def validate_positive_number(value):
    number = float(value)
    if number < 0:
        raise ValueError("Value cannot be negative.")
    return number

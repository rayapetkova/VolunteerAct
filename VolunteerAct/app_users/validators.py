from django.core.exceptions import ValidationError


def first_name_validator(value):
    if not value.is_alpha():
        raise ValidationError('First name needs to contain only alphabetic symbols.')

    return value


def last_name_validator(value):
    if not value.is_alpha():
        raise ValidationError('Last name needs to contain only alphabetic symbols.')

    return value


def phone_number_validator(value):
    if not value.is_digit():
        raise ValidationError('Phone number needs to consist of only digits.')

    return value
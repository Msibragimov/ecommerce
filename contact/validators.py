from django.forms import ValidationError


def validate_number(number):
    if number[0] == '+':
        if number[1:].isnumeric() == False:
            raise ValidationError("Iltimos telefon raqamizni to'g'ri kiriting")
    else:
        if number.isnumeric() == False:
            raise ValidationError("Iltimos telefon raqamizni to'g'ri kiriting")


def validate_name_or_surname(value):
    if value[0].isupper() == False or len(value) < 4:
        raise ValidationError("Iltimos to'g'ri ma'lumot kiriting")
def validate_number(number):
    if number[0] == '+':
        if number[1:].isnumeric():
            return number
        raise Exception("Iltimos telefon raqamizni to'g'ri kiriting")
    else:
        if number.isnumeric():
            return number
        raise Exception("Iltimos telefon raqamizni to'g'ri kiriting")


def validate_name_or_surname(value):
    if value[0].isupper() and len(value) >= 4:
        return value
    raise Exception("Iltimos to'g'ri ma'lumot kiriting")
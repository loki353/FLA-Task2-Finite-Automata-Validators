def validate_mobile(number):
    if len(number) != 10:
        return False
    if number[0] not in "6789":
        return False
    state = "START"
    for char in number:
        if char not in "0123456789":
            return False
        if state == "START":
            state = "FIRST_DIGIT"
        else:
            state = "DIGITS"
    return state == "DIGITS"


def validate_username(username):
    if not username or not username[0].isalpha():
        return False
    previous_underscore = False
    for index, char in enumerate(username):
        if index == 0:
            continue
        if char.isalpha() or char.isdigit():
            previous_underscore = False
        elif char == "_" and not previous_underscore and index != len(username) - 1:
            previous_underscore = True
        else:
            return False
    return True


def validate_time(time):
    if len(time) != 5 or time[2] != ":":
        return False
    hour_text = time[:2]
    minute_text = time[3:]
    if not (hour_text.isascii() and hour_text.isdigit() and minute_text.isascii() and minute_text.isdigit()):
        return False
    hour = int(hour_text)
    minute = int(minute_text)
    return 0 <= hour <= 23 and 0 <= minute <= 59


def validate(kind, value):
    validators = {
        "mobile": validate_mobile,
        "username": validate_username,
        "time": validate_time
    }
    if kind not in validators:
        raise ValueError("kind must be mobile, username, or time")
    return validators[kind](value)

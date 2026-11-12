from finite_automata.validators import validate


def test_mobile_numbers():
    assert validate("mobile", "9123456780")
    assert not validate("mobile", "5123456789")
    assert not validate("mobile", "78901234567")


def test_usernames():
    assert validate("username", "lokesh25")
    assert validate("username", "arjun_24")
    assert not validate("username", "25lokesh")
    assert not validate("username", "tech__user")


def test_24_hour_time():
    assert validate("time", "14:35")
    assert validate("time", "00:00")
    assert not validate("time", "25:10")
    assert not validate("time", "16:75")


def test_unknown_validator():
    try:
        validate("email", "student@example.com")
    except ValueError:
        return
    assert False, "Unknown validator should raise ValueError"

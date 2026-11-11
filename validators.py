"""Finite-automata-inspired validators for FLA Task 2."""
import re

def validate_pin(pin: str) -> bool:
    """Accept exactly four ASCII decimal digits."""
    if len(pin) != 4:
        return False
    state = 0
    for ch in pin:
        if ch not in "0123456789":
            return False
        state += 1
    return state == 4

def validate_password(password: str) -> bool:
    """Require >=8 chars, uppercase, lowercase, digit and special character."""
    return (
        len(password) >= 8
        and re.search(r"[A-Z]", password) is not None
        and re.search(r"[a-z]", password) is not None
        and re.search(r"[0-9]", password) is not None
        and re.search(r"[^A-Za-z0-9]", password) is not None
    )

def validate_email(email: str) -> bool:
    """Practical email-format check; not a complete RFC mailbox parser."""
    if len(email) > 254:
        return False
    pattern = r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"
    if not re.fullmatch(pattern, email):
        return False
    local, domain = email.rsplit("@", 1)
    return (
        len(local) <= 64
        and not local.startswith(".")
        and not local.endswith(".")
        and ".." not in local
        and all(label and not label.startswith("-") and not label.endswith("-")
                for label in domain.split("."))
    )

if __name__ == "__main__":
    print("PIN 1234:", "ACCEPTED" if validate_pin("1234") else "REJECTED")
    print("Password Abcd@123:", "ACCEPTED" if validate_password("Abcd@123") else "REJECTED")
    print("Email student@example.com:", "ACCEPTED" if validate_email("student@example.com") else "REJECTED")

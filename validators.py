from finite_automata.validators import validate_mobile, validate_username, validate_time, validate


if __name__ == "__main__":
    mobile_numbers = ["9123456780", "6789012345", "5123456789"]
    usernames = ["lokesh25", "arjun_24", "25lokesh"]
    times = ["06:25", "14:35", "25:10"]

    for value in mobile_numbers:
        print(f"Mobile {value}: {'ACCEPTED' if validate_mobile(value) else 'REJECTED'}")

    for value in usernames:
        print(f"Username {value}: {'ACCEPTED' if validate_username(value) else 'REJECTED'}")

    for value in times:
        print(f"Time {value}: {'ACCEPTED' if validate_time(value) else 'REJECTED'}")

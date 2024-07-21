def eight_or_more_char(pw: str) -> bool:
    return True if (len(pw) >= 8) else False


def two_or_more_numbers(pw: str) -> bool:
    num_count = 0

    for i in pw:
        if i.isnumeric():
            num_count += 1

    return True if num_count >= 2 else False


def at_least_one_capital_letter(pw: str) -> bool:
    cap_count = 0

    for i in pw:
        if i.isupper():
            cap_count += 1

    return True if cap_count else False


def at_least_one_special_char(pw: str) -> bool:
    special_char = 0

    for i in pw:
        if not i.isalnum():
            special_char += 1

    return True if special_char else False


def password_validator(pw: str) -> bool | str:
    val_errors = []

    if not eight_or_more_char(pw):
        val_errors.append("Password must be at least 8 characters")

    if not two_or_more_numbers(pw):
        val_errors.append("The password must contain at least 2 numbers")

    if not at_least_one_capital_letter(pw):
        val_errors.append("Password must contain at least one capital letter")

    if not at_least_one_special_char(pw):
        val_errors.append("Password must contain at least one special character")

    if val_errors:
        return val_errors[0] if len(val_errors) == 1 else "\n".join(val_errors)

    return True

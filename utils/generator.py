import array
import random
import string


def generate_password(params: dict[str, str]):
    use_digits = True if params["digits"].lower() == "yes" else False
    use_symbols = True if params["symbols"].lower() == "yes" else False

    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digit_chars = string.digits if use_digits else ""
    symbol_chars = "!@#$%^&*()_-+=[]{}|;:,.<>?" if use_symbols else ""

    all_chars = lower_chars + upper_chars + digit_chars + symbol_chars

    password = []

    password.append(random.choice(lower_chars))
    password.append(random.choice(upper_chars))

    if digit_chars != "":
        password.append(random.choice(digit_chars))
    if symbol_chars != "":
        password.append(random.choice(symbol_chars))

    remainging_length = int(params["length"]) - len(password)

    for _ in range(remainging_length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password)

import random
import string

def key_generation(pwd_length=4):
    UPPERCASE_CHARACTERS = string.ascii_uppercase
    DIGITS = string.digits

    combined_list = UPPERCASE_CHARACTERS + DIGITS

    rand_upper = random.choice(UPPERCASE_CHARACTERS)
    rand_digit = random.choice(DIGITS)

    temp_pwd = random.sample(combined_list, pwd_length - 2) + [rand_upper, rand_digit]
    random.shuffle(temp_pwd)
    password = "".join(temp_pwd)

    return password

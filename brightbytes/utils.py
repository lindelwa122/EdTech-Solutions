def check_upper(str):
    for char in str:
        if char.isupper(): return True
    return False

def check_lower(str):
    for char in str:
        if char.islower(): return True
    return False

def check_digit(str):
    for char in str:
        if char.isdigit(): return True
    return False
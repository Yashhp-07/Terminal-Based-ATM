from Bank.validations import validate_amount


def validate_bank_name(existing_banks):
    while True:
        name = input("Enter bank name: ")
        if not name:
            print("Bank name cannot be empty.")
            continue
        if len(name) < 2 or len(name) > 30:
            print("Bank name must be between 2 and 30 characters.")
            continue
        if name in existing_banks:
            print("A bank with this name already exists.")
            continue
        return name


def validate_bank_username():
    while True:
        username = input("Enter bank username: ")
        if not username:
            print("Username cannot be empty.")
            continue
        if len(username) < 3 or len(username) > 20:
            print("Username must be between 3 and 20 characters.")
            continue
        return username


def validate_bank_password():
    while True:
        password = input("Enter bank password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            continue
        return password


def validate_bank_initial_balance():
    return validate_amount(
        "Enter initial bank balance (minimum Rs. 10,00,000): ",
        1000000,
        "Initial bank balance must be at least Rs. 10,00,000."
    )

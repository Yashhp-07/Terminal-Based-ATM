def get_deposit_amount():
    """
    Prompts the user for a deposit amount and validates it.

    Rules:
        - Must be a valid number.
        - Minimum: Rs. 100.
        - Must be in multiples of Rs. 100.

    Returns:
        float: The validated deposit amount.
    """
    while True:
        value = input("Enter deposit amount (minimum Rs. 100, multiples of 100): ")
        try:
            amount = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if amount < 100:
            print("Minimum deposit amount is Rs. 100.")
            continue
        if int(amount) % 100 != 0:
            print("Deposit amount must be in multiples of 100.")
            continue
        return amount


def get_card_number(users):
    """
    Prompts the user for their card number and validates it.

    Rules:
        - Must contain only digits.
        - Must be exactly 16 characters long.
        - Must exist in the provided users dictionary.

    Args:
        users (dict): Dictionary of users keyed by card number.

    Returns:
        str: The validated card number.
    """
    while True:
        card_number = input("Enter your card number: ")
        if not card_number.isdigit():
            print("Card number must contain only digits.")
            continue
        if len(card_number) != 16:
            print("Card number must be exactly 16 digits.")
            continue
        if card_number not in users:
            print("Invalid card number. No account found.")
            continue
        return card_number


def get_pin():
    """
    Prompts the user for their 4-digit ATM PIN and validates it.

    Rules:
        - Must contain only digits.
        - Must be exactly 4 characters long.

    Returns:
        str: The validated PIN.
    """
    while True:
        pin = input("Enter your PIN: ")
        if not pin.isdigit():
            print("PIN must contain only digits.")
            continue
        if len(pin) != 4:
            print("PIN must be exactly 4 digits.")
            continue
        return pin


def get_withdraw_amount():
    """
    Prompts the user for a withdrawal amount and validates it.

    Rules:
        - Must be a valid number.
        - Minimum: Rs. 100.
        - Maximum: Rs. 10,000 per transaction.
        - Must be in multiples of Rs. 100.

    Returns:
        float: The validated withdrawal amount.
    """
    while True:
        value = input("Enter withdrawal amount (Rs. 100 - Rs. 10,000, multiples of 100): ")
        try:
            amount = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if amount < 100:
            print("Minimum withdrawal amount is Rs. 100.")
            continue
        if amount > 10000:
            print("Maximum withdrawal amount per transaction is Rs. 10,000.")
            continue
        if int(amount) % 100 != 0:
            print("Withdrawal amount must be in multiples of 100.")
            continue
        return amount

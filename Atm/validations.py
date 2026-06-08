from .constants import (
    ENTER_DEPOSIT_AMOUNT, ERR_DEPOSIT_MIN, ERR_DEPOSIT_AMOUNT,
    ENTER_CARD_NUMBER, ERR_DIGITS, ERR_CARD_LENGTH, ERR_INVALID_CARD,
    ENTER_PIN_NUMBER, ERR_PIN_LENGTH,
    ENTER_WITHDRAW_AMOUNT, ERR_WITHDRAW_MIN, ERR_WITHDRAW_MAX, ERR_WITHDRAW_AMOUNT,
    ERR_NOT_A_NUMBER
)

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
        value = input(ENTER_DEPOSIT_AMOUNT)
        try:
            amount = float(value)
        except ValueError:
            print(ERR_NOT_A_NUMBER)
            continue
        if amount < 100:
            print(ERR_DEPOSIT_MIN)
            continue
        if int(amount) % 100 != 0:
            print(ERR_DEPOSIT_AMOUNT)
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
        card_number = input(ENTER_CARD_NUMBER)
        if not card_number.isdigit():
            print(f"Card number {ERR_DIGITS}")
            continue
        if len(card_number) != 16:
            print(ERR_CARD_LENGTH)
            continue
        if card_number not in users:
            print(ERR_INVALID_CARD)
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
        pin = input(ENTER_PIN_NUMBER)
        if not pin.isdigit():
            print(f"PIN {ERR_DIGITS}")
            continue
        if len(pin) != 4:
            print(ERR_PIN_LENGTH)
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
        value = input(ENTER_WITHDRAW_AMOUNT)
        try:
            amount = float(value)
        except ValueError:
            print(ERR_NOT_A_NUMBER)
            continue
        if amount < 100:
            print(ERR_WITHDRAW_MIN)
            continue
        if amount > 10000:
            print(ERR_WITHDRAW_MAX)
            continue
        if int(amount) % 100 != 0:
            print(ERR_WITHDRAW_AMOUNT)
            continue
        return amount

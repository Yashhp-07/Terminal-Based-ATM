"""Validation functions for the Admin module.

Provides interactive input validators for bank registration operations.
Each function loops until valid input is provided.
"""

from Bank.validations import validate_amount
from .constants import (
    ENTER_BANK_NAME, ERR_BANK_NAME_EMPTY, ERR_BANK_NAME_LENGTH, ERR_BANK_NAME_EXISTS,
    ENTER_BANK_USERNAME, ERR_BANK_USERNAME_EMPTY, ERR_BANK_USERNAME_LENGTH,
    ENTER_BANK_PASSWORD, ERR_BANK_PASSWORD_SHORT,
    ENTER_BANK_BALANCE, ERR_BALANCE_MIN
)


def validate_bank_name(existing_banks):
    """Prompt and validate the name for a new bank.

    Rules:
        - Must not be empty.
        - Must be between 2 and 30 characters.
        - Must not already exist in the system.

    Args:
        existing_banks (dict): Dictionary of currently registered banks keyed by name.

    Returns:
        str: The validated bank name.
    """
    while True:
        name = input(ENTER_BANK_NAME)
        if not name:
            print(ERR_BANK_NAME_EMPTY)
            continue
        if len(name) < 2 or len(name) > 30:
            print(ERR_BANK_NAME_LENGTH)
            continue
        if name in existing_banks:
            print(ERR_BANK_NAME_EXISTS)
            continue
        return name


def validate_bank_username():
    """Prompt and validate the username for a new bank account.

    Rules:
        - Must not be empty.
        - Must be between 3 and 20 characters.

    Returns:
        str: The validated username.
    """
    while True:
        username = input(ENTER_BANK_USERNAME)
        if not username:
            print(ERR_BANK_USERNAME_EMPTY)
            continue
        if len(username) < 3 or len(username) > 20:
            print(ERR_BANK_USERNAME_LENGTH)
            continue
        return username


def validate_bank_password():
    """Prompt and validate the password for a new bank account.

    Rules:
        - Must be at least 6 characters long.

    Returns:
        str: The validated password.
    """
    while True:
        password = input(ENTER_BANK_PASSWORD)
        if len(password) < 6:
            print(ERR_BANK_PASSWORD_SHORT)
            continue
        return password


def validate_bank_initial_balance():
    """Prompt and validate the initial operational balance for a new bank.

    Rules:
        - Must be a valid number.
        - Minimum: Rs. 10,00,000.

    Returns:
        float: The validated initial balance.
    """
    return validate_amount(ENTER_BANK_BALANCE, 1000000, ERR_BALANCE_MIN)

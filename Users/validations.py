from .constants import (
    ENTER_CURRENT_PIN, ENTER_NEW_PIN, ERR_PIN_FORMAT, ERR_WRONG_PIN, ERR_PIN_SAME, ERR_PIN_MISMATCH,
    CONFIRM_NEW_PIN
    )

def get_old_pin(user):
    """
    Prompts the user for their current PIN and verifies it.

    Loops until the correct current PIN is entered — no attempt limit since the user is already authenticated at
    this point.

    Args:
        user (User): The authenticated User object to verify against.

    Returns:
        str: The verified current PIN.
    """

    while True:
        value = input(ENTER_CURRENT_PIN)
        if value == user.atm_pin:
            return value
        print(ERR_WRONG_PIN)

def get_new_pin(user):
    """
    Prompts the user for a new PIN, validates it, and confirms it with a second entry to prevent typos.

    Rules:
        - Must be exactly 4 digits.
        - Must differ from the current PIN.
        - Must match the confirmation entry.

    Args:
        user (User): The authenticated User object, used to check the new PIN differs from the current one.

    Returns:
        str: A valid, confirmed new 4-digit PIN.
    """
     
    while True:
        new_pin = input(ENTER_NEW_PIN)
        if not new_pin.isdigit() or len(new_pin) != 4:
            print(ERR_PIN_FORMAT)
            continue

        # new PIN must be different from current pin
        if new_pin == user.atm_pin:
            print(ERR_PIN_SAME)
            continue

        # confirm again
        confirm = input(CONFIRM_NEW_PIN)
        if new_pin != confirm:
            print(ERR_PIN_MISMATCH)
            continue
        return new_pin
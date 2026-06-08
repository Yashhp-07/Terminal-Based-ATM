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
        value = input("Enter your current PIN: ")
        if value == user.atm_pin:
            return value
        print("Wrong PIN. Please try again.")


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
        new_pin = input("Enter your new PIN (4 digits): ")
        if not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be exactly 4 digits.")
            continue

        # new PIN must be different from current pin
        if new_pin == user.atm_pin:
            print("New PIN must be different from current PIN.")
            continue

        # confirm again
        confirm = input("Confirm your new PIN: ")
        if new_pin != confirm:
            print("PINs do not match. Please try again.")
            continue
        return new_pin
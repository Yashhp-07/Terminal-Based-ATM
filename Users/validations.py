def get_old_pin(user):
    while True:
        value = input("Enter your current PIN: ")
        if value == user.atm_pin:
            return value
        print("Wrong PIN. Please try again.")


def get_new_pin(user):
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
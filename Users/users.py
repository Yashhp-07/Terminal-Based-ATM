class User:
    def __init__(self, user_id, name, dob, phone_number, email, aadhar_number, pan_number, initial_balance, bank_name, card_number, atm_pin):
        self.user_id = user_id
        self.name = name
        self.dob = dob
        self.phone_number = phone_number
        self.email = email
        self.aadhar_number = aadhar_number
        self.pan_number = pan_number
        self.balance = initial_balance
        self.bank_name = bank_name
        self.card_number = card_number
        self.atm_pin = atm_pin
        self.daily_withdrawal_amount = 0.0
        self.daily_withdrawal_count = 0

    def change_pin(self):
        old_pin = get_old_pin(self)
        new_pin = get_new_pin(self)
        self.atm_pin = new_pin
        print("PIN changed successfully!")


def get_old_pin(user):
    while True:
        entered = input("Enter your current PIN: ")
        if entered == user.atm_pin:
            return entered
        print("Wrong PIN. Please try again.")


def get_new_pin(user):
    while True:
        new_pin = input("Enter your new PIN (4 digits): ")
        if not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be exactly 4 digits.")
            continue
        if new_pin == user.atm_pin:
            print("New PIN must be different from current PIN.")
            continue
        confirm = input("Confirm your new PIN: ")
        if new_pin != confirm:
            print("PINs do not match. Please try again.")
            continue
        return new_pin

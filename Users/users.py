from .validations import get_old_pin, get_new_pin

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



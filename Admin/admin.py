import hashlib
from utils.generators import generate_bank_id
from Bank.bank import Bank
from .validations import (
    validate_bank_name, validate_bank_username, validate_bank_password,
    validate_bank_initial_balance
)


class Admin:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        self.banks = {}

    def verify_credentials(self, username, password):
        return username == self.username and hashlib.sha256(password.encode()).hexdigest() == self.password_hash

    def create_bank(self):
        print("\n--- Create Bank ---")
        name = validate_bank_name(self.banks)
        username = validate_bank_username()
        password = validate_bank_password()
        balance = validate_bank_initial_balance()

        bank_id = generate_bank_id()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        bank = Bank(bank_id, name, username, password_hash, balance)
        self.banks[name] = bank

        print("\nBank created successfully!")
        print(f"Bank ID: {bank.bank_id}")
        print(f"Bank Name: {bank.name}")
        print(f"Balance: Rs.{bank.balance:.2f}")

    def view_all_banks(self):
        print("\n--- All Banks ---")
        if not self.banks:
            print("No banks registered yet.")
            return
        for name, bank in self.banks.items():
            print(f"\nBank ID: {bank.bank_id}")
            print(f"Name: {bank.name}")
            print(f"Balance: Rs.{bank.balance:.2f}")
            print(f"Users: {len(bank.users)}")
            print(f"ATMs: {len(bank.atms)}")
            print("-" * 25)

    def view_all_users(self):
        print("\n--- All Users ---")
        if not self.banks:
            print("No banks registered yet.")
            return
        for bank_name, bank in self.banks.items():
            if not bank.users:
                continue
            print(f"\nBank: {bank_name}")
            for card, user in bank.users.items():
                print(f"  Name: {user.name}, Card: {card}, Balance: Rs.{user.balance:.2f}")

    def view_all_atms(self):
        print("\n--- All ATMs ---")
        if not self.banks:
            print("No banks registered yet.")
            return
        for bank_name, bank in self.banks.items():
            if not bank.atms:
                continue
            print(f"\nBank: {bank_name}")
            for atm_id, atm in bank.atms.items():
                print(f"  ATM: {atm_id}, Location: {atm.location}, Cash: Rs.{atm.balance:.2f}")




import hashlib
from utils.generators import generate_bank_id
from Bank.bank import Bank


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
    from Bank.validations import validate_amount
    return validate_amount(
        "Enter initial bank balance (minimum Rs. 10,00,000): ",
        1000000,
        "Initial bank balance must be at least Rs. 10,00,000."
    )

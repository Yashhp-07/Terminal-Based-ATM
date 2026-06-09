from utils.generators import generate_user_id, generate_card_number, generate_pin, generate_atm_id
from Users.users import User
from Atm.atm import ATM
from .constants import (
    HEADER_CREATE_USER, HEADER_CREATE_ATM, HEADER_ACCOUNT_SUCCESS, MSG_ATM_SUCCESS,
    ERR_INSUFFICIENT_FUNDS, HEADER_ADD_BALANCE, ERR_ATM_NOT_FOUND,
    ERR_INSUFFICIENT_BANK_FUNDS, MSG_BALANCE_ADDED,
    HEADER_VIEW_USERS, MSG_NO_USERS, HEADER_VIEW_ATMS, MSG_NO_ATMS
)
from .validations import (
    validate_name, validate_dob, validate_phone_number, validate_email,
    validate_aadhar_number, validate_pan_number, validate_initial_balance,
    validate_location, validate_atm_initial_balance, validate_atm_topup_balance
)


class Bank:
    def __init__(self, bank_id, name, username, password, initial_balance):
        self.bank_id = bank_id
        self.name = name
        self.username = username
        self.password = password
        self.balance = initial_balance
        self.users = {}
        self.atms = {}

    def create_user_account(self):
        print(HEADER_CREATE_USER)
        name = validate_name()
        dob = validate_dob()
        phone = validate_phone_number()
        email = validate_email()
        aadhar = validate_aadhar_number()
        pan = validate_pan_number()
        initial_balance = validate_initial_balance()

        user_id = generate_user_id()
        card_number = generate_card_number()
        pin = generate_pin()

        user = User(user_id, name, dob, phone, email, aadhar, pan, initial_balance, self.name, card_number, pin)
        self.users[card_number] = user

        print(HEADER_ACCOUNT_SUCCESS)
        print(f"Name: {user.name}")
        print(f"User ID: {user.user_id}")
        print(f"Card Number: {user.card_number}")
        print(f"ATM PIN: {user.atm_pin}")
        print(f"Initial Balance: Rs.{user.balance:.2f}")
        print(f"Bank: {user.bank_name}")

    def create_atm(self):
        print(HEADER_CREATE_ATM)
        atm_id = generate_atm_id(self.name)
        location = validate_location()

        while True:
            amount = validate_atm_initial_balance()
            if self.balance >= amount:
                break
            print(ERR_INSUFFICIENT_FUNDS)

        atm = ATM(atm_id, self.name, amount, self, location)
        self.atms[atm_id] = atm
        self.balance -= amount

        print(MSG_ATM_SUCCESS)
        print(f"ATM ID: {atm.atm_id}")
        print(f"Location: {atm.location}")
        print(f"Initial Cash: Rs.{atm.balance:.2f}")

    def add_balance_to_atm(self):
        if not self.atms:
            print(ERR_ATM_NOT_FOUND)
            return

        print(HEADER_ADD_BALANCE)
        atm_list = list(self.atms.values())
        for i, atm in enumerate(atm_list, 1):
            print(f"{i}. {atm.atm_id} - {atm.location} (Current balance: Rs.{atm.balance:.2f})")

        try:
            choice = int(input("Select an ATM: "))
            if choice < 1 or choice > len(atm_list):
                print("Invalid selection.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        selected_atm = atm_list[choice - 1]
        amount = validate_atm_topup_balance()

        if self.balance < amount:
            print(ERR_INSUFFICIENT_BANK_FUNDS)
            return

        selected_atm.balance += amount
        self.balance -= amount
        print(MSG_BALANCE_ADDED.format(amount, selected_atm.atm_id, selected_atm.balance))

    def view_users(self):
        print(HEADER_VIEW_USERS)
        if not self.users:
            print(MSG_NO_USERS)
            return
        for card, user in self.users.items():
            print(f"\nName: {user.name}")
            print(f"User ID: {user.user_id}")
            print(f"Card: {card}")
            print(f"Balance: Rs.{user.balance:.2f}")
            print("-" * 25)

    def view_atms(self, show_balance=False):
        print(HEADER_VIEW_ATMS)
        if not self.atms:
            print(MSG_NO_ATMS)
            return
        for atm_id, atm in self.atms.items():
            print(f"\nATM ID: {atm_id}")
            print(f"Location: {atm.location}")
            if show_balance:
                print(f"Cash Balance: Rs.{atm.balance:.2f}")
            print("-" * 25)

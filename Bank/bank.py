from utils.generators import generate_user_id, generate_card_number, generate_pin, generate_atm_id
from Users.users import User
from Atm.atm import ATM
from .constants import (
    HEADER_CREATE_USER, HEADER_CREATE_ATM, HEADER_ACCOUNT_SUCCESS, MSG_ATM_SUCCESS,
    ERR_INSUFFICIENT_FUNDS
)
from .validations import (
    validate_name, validate_dob, validate_phone_number, validate_email,
    validate_aadhar_number, validate_pan_number, validate_initial_balance,
    validate_location, validate_atm_initial_balance
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

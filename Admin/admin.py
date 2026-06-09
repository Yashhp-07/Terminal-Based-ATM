"""Admin module for the ATM system.

Defines the Admin class which manages bank registration and provides
system-wide visibility into all banks, users, and ATMs.
"""

import hashlib
from utils.generators import generate_bank_id
from Bank.bank import Bank
from .constants import (
    HEADER_CREATE_BANK, HEADER_ALL_BANKS, HEADER_ALL_USERS, HEADER_ALL_ATMS,
    SUCCESS_BANK_CREATED, MSG_NO_BANKS
)
from .validations import (
    validate_bank_name, validate_bank_username, validate_bank_password,
    validate_bank_initial_balance
)


class Admin:
    """Represents the system administrator who manages bank registration.

    The Admin sits at the top of the object hierarchy and owns all Bank
    instances. It handles credential verification, bank creation, and
    provides read-only views across the entire system.

    Attributes:
        username (str): Admin login username.
        password_hash (str): SHA-256 hashed admin password.
        banks (dict): Dictionary of Bank objects keyed by bank name.
    """

    def __init__(self, username, password_hash):
        """Initialize the Admin with login credentials.

        Args:
            username (str): Admin username.
            password_hash (str): SHA-256 hash of the admin password.
        """
        self.username = username
        self.password_hash = password_hash
        self.banks = {}

    def verify_credentials(self, username, password):
        """Verify admin login credentials against stored values.

        Args:
            username (str): The provided username.
            password (str): The provided password (plain text).

        Returns:
            bool: True if both username and password hash match.
        """
        return username == self.username and hashlib.sha256(password.encode()).hexdigest() == self.password_hash

    def create_bank(self):
        """Register a new bank in the system.

        Flow:
            1. Prompts for and validates bank name, username, password.
            2. Prompts for initial operational balance (minimum Rs. 10,00,000).
            3. Generates a unique bank ID and hashes the password.
            4. Creates a Bank object and stores it keyed by name.
            5. Displays the created bank's details.
        """
        print(HEADER_CREATE_BANK)
        name = validate_bank_name(self.banks)
        username = validate_bank_username()
        password = validate_bank_password()
        balance = validate_bank_initial_balance()

        bank_id = generate_bank_id()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        bank = Bank(bank_id, name, username, password_hash, balance)
        self.banks[name] = bank

        print(SUCCESS_BANK_CREATED)
        print(f"Bank ID: {bank.bank_id}")
        print(f"Bank Name: {bank.name}")
        print(f"Balance: Rs.{bank.balance:.2f}")

    def view_all_banks(self):
        """Display all registered banks with their statistics.

        Prints each bank's ID, name, balance, user count, and ATM count.
        If no banks are registered, displays an appropriate message.
        """
        print(HEADER_ALL_BANKS)
        if not self.banks:
            print(MSG_NO_BANKS)
            return
        for name, bank in self.banks.items():
            print(f"\nBank ID: {bank.bank_id}")
            print(f"Name: {bank.name}")
            print(f"Balance: Rs.{bank.balance:.2f}")
            print(f"Users: {len(bank.users)}")
            print(f"ATMs: {len(bank.atms)}")
            print("-" * 25)

    def view_all_users(self):
        """Display all users across all banks, grouped by bank.

        If no banks or no users exist, displays an appropriate message.
        """
        print(HEADER_ALL_USERS)
        if not self.banks:
            print(MSG_NO_BANKS)
            return
        for bank_name, bank in self.banks.items():
            if not bank.users:
                continue
            print(f"\nBank: {bank_name}")
            for card, user in bank.users.items():
                print(f"  Name: {user.name}, Card: {card}, Balance: Rs.{user.balance:.2f}")

    def view_all_atms(self):
        """Display all ATMs across all banks, grouped by bank.

        If no banks or no ATMs exist, displays an appropriate message.
        """
        print(HEADER_ALL_ATMS)
        if not self.banks:
            print(MSG_NO_BANKS)
            return
        for bank_name, bank in self.banks.items():
            if not bank.atms:
                continue
            print(f"\nBank: {bank_name}")
            for atm_id, atm in bank.atms.items():
                print(f"  ATM: {atm_id}, Location: {atm.location}, Cash: Rs.{atm.balance:.2f}")

"""Interactive menu system for the ATM application.

Orchestrates the entire user experience by delegating to domain classes
(Admin, Bank, ATM, User) based on role selection and authentication.
"""

import hashlib

from Admin.validations import validate_admin_credentials
from Atm.validations import get_card_number, get_pin
from .constants import (
    HEADER_ADMIN_LOGIN, HEADER_ADMIN_PANEL, HEADER_SELECT_BANK, HEADER_BANK_LOGIN,
    HEADER_SELECT_ATM, HEADER_ATM_MENU,
    MENU_ADMIN_CREATE_BANK, MENU_ADMIN_VIEW_BANKS, MENU_ADMIN_VIEW_USERS,
    MENU_ADMIN_VIEW_ATMS, MENU_ADMIN_BACK,
    MENU_BANK_CREATE_USER, MENU_BANK_DEPLOY_ATM, MENU_BANK_ADD_BALANCE,
    MENU_BANK_VIEW_USERS, MENU_BANK_VIEW_ATMS, MENU_BANK_BACK,
    MENU_ATM_BALANCE, MENU_ATM_DEPOSIT, MENU_ATM_WITHDRAW, MENU_ATM_CHANGE_PIN,
    MENU_ATM_BACK,
    DISPLAY_BANK_ITEM, DISPLAY_ATM_ITEM, DISPLAY_BANK_PANEL_HEADER,
    DISPLAY_BANK_FUNDS, DISPLAY_ATM_INFO, DISPLAY_ATM_LOCATION,
    SUCCESS_ADMIN_LOGIN, SUCCESS_BANK_LOGIN,
    ERR_INVALID_CREDENTIALS, REMAINING_ATTEMPTS, ERR_CREDENTIALS_EXHAUSTED,
    ERR_WRONG_BANK_CREDENTIALS, ERR_WRONG_BANK_CREDENTIALS_REMAINING,
    ERR_WRONG_BANK_CREDENTIALS_EXHAUSTED,
    ERR_INVALID_CHOICE, ERR_INVALID_CHOICE_RANGE, ERR_INVALID_SELECTION,
    ERR_NOT_A_NUMBER,
    MSG_NO_BANKS_REGISTERED, MSG_NO_ATMS_AVAILABLE,
    ENTER_CHOICE, ENTER_SELECT_BANK, ENTER_SELECT_ATM,
    ENTER_BANK_USERNAME, ENTER_BANK_PASSWORD
)


class Menu:
    """Orchestrates the interactive menu-based navigation for all user roles.

    Handles authentication flows for admin, bank, and user roles, and
    delegates to the appropriate domain methods for each operation.

    Attributes:
        admin (Admin): The Admin instance that owns all banks in the system.
    """

    def __init__(self, admin):
        """Initialize the menu system with a reference to the Admin.

        Args:
            admin (Admin): The seeded Admin instance with populated banks.
        """
        self.admin = admin

    def authenticate_admin(self, max_attempts=3):
        """Authenticate an admin user with up to 3 attempts.

        Delegates to validate_admin_credentials for the credential prompt
        and verification loop.

        Args:
            max_attempts (int): Maximum number of login attempts. Defaults to 3.

        Returns:
            bool: True if authentication succeeds, False otherwise.
        """
        return validate_admin_credentials(self.admin)

    def authenticate_user(self, users, max_attempts=3):
        """Authenticate a user via card number and PIN with up to 3 attempts.

        Uses get_card_number and get_pin from the Atm validations module.
        Displays attempt countdown and locks out after max attempts.

        Args:
            users (dict): Dictionary of User objects keyed by card number.
            max_attempts (int): Maximum number of login attempts. Defaults to 3.

        Returns:
            User: The authenticated User object, or None on failure.
        """
        attempts = 0
        while attempts < max_attempts:
            card_number = get_card_number(users)
            pin = get_pin()
            if users[card_number].atm_pin == pin:
                return users[card_number]
            attempts += 1
            print(ERR_INVALID_CREDENTIALS)
            if attempts < max_attempts:
                print(REMAINING_ATTEMPTS.format(max_attempts - attempts))
        print(ERR_CREDENTIALS_EXHAUSTED)
        return None

    def handle_admin(self):
        """Handle the admin role flow: authenticate then show admin menu."""
        print(HEADER_ADMIN_LOGIN)
        if self.authenticate_admin():
            self.admin_menu()

    def admin_menu(self):
        """Display and process the admin operations menu.

        Options:
            1. Create a new bank
            2. View all banks
            3. View all users across all banks
            4. View all ATMs across all banks
            5. Return to main menu
        """
        while True:
            print(HEADER_ADMIN_PANEL)
            print(MENU_ADMIN_CREATE_BANK)
            print(MENU_ADMIN_VIEW_BANKS)
            print(MENU_ADMIN_VIEW_USERS)
            print(MENU_ADMIN_VIEW_ATMS)
            print(MENU_ADMIN_BACK)

            choice = input(ENTER_CHOICE)
            if choice == "1":
                self.admin.create_bank()
            elif choice == "2":
                self.admin.view_all_banks()
            elif choice == "3":
                self.admin.view_all_users()
            elif choice == "4":
                self.admin.view_all_atms()
            elif choice == "5":
                break
            else:
                print(ERR_INVALID_CHOICE_RANGE.format(5))

    def handle_bank(self):
        """Handle the bank role flow: select bank, authenticate, show bank menu.

        Lists all registered banks, prompts the operator to select one,
        authenticates with bank credentials (3 attempts), then opens the
        bank operations menu.
        """
        if not self.admin.banks:
            print(MSG_NO_BANKS_REGISTERED)
            return

        print(HEADER_SELECT_BANK)
        bank_list = list(self.admin.banks.values())
        for i, bank in enumerate(bank_list, 1):
            print(DISPLAY_BANK_ITEM.format(i, bank.name))

        try:
            choice = int(input(ENTER_SELECT_BANK))
            if choice < 1 or choice > len(bank_list):
                print(ERR_INVALID_SELECTION)
                return
        except ValueError:
            print(ERR_NOT_A_NUMBER)
            return

        selected_bank = bank_list[choice - 1]
        print(HEADER_BANK_LOGIN)
        for attempt in range(3, 0, -1):
            username = input(ENTER_BANK_USERNAME)
            password = input(ENTER_BANK_PASSWORD)
            if username == selected_bank.username and hashlib.sha256(password.encode()).hexdigest() == selected_bank.password:
                print(SUCCESS_BANK_LOGIN)
                self.bank_menu(selected_bank)
                return
            print(ERR_WRONG_BANK_CREDENTIALS)
            if attempt > 1:
                print(ERR_WRONG_BANK_CREDENTIALS_REMAINING.format(attempt - 1))
        print(ERR_WRONG_BANK_CREDENTIALS_EXHAUSTED)

    def bank_menu(self, bank):
        """Display and process the bank operations menu.

        Shows the bank name and available funds in the header.

        Args:
            bank (Bank): The authenticated Bank instance to operate on.

        Options:
            1. Create a new user account
            2. Deploy a new ATM
            3. Add cash balance to an existing ATM
            4. View all registered users
            5. View all deployed ATMs (with cash balances)
            6. Return to main menu
        """
        while True:
            print(DISPLAY_BANK_PANEL_HEADER.format(bank.name))
            print(DISPLAY_BANK_FUNDS.format(bank.balance))
            print(MENU_BANK_CREATE_USER)
            print(MENU_BANK_DEPLOY_ATM)
            print(MENU_BANK_ADD_BALANCE)
            print(MENU_BANK_VIEW_USERS)
            print(MENU_BANK_VIEW_ATMS)
            print(MENU_BANK_BACK)

            choice = input(ENTER_CHOICE)
            if choice == "1":
                bank.create_user_account()
            elif choice == "2":
                bank.create_atm()
            elif choice == "3":
                bank.add_balance_to_atm()
            elif choice == "4":
                bank.view_users()
            elif choice == "5":
                bank.view_atms(show_balance=True)
            elif choice == "6":
                break
            else:
                print(ERR_INVALID_CHOICE_RANGE.format(6))

    def handle_user(self):
        """Handle the user role flow: select ATM, then show ATM menu.

        Flattens all ATMs across all banks into a single list, prompts the
        user to select one, then opens the ATM operations menu where each
        transaction requires individual user authentication.
        """
        all_atms = []
        for bank in self.admin.banks.values():
            for atm in bank.atms.values():
                all_atms.append((atm, bank))

        if not all_atms:
            print(MSG_NO_ATMS_AVAILABLE)
            return

        print(HEADER_SELECT_ATM)
        for i, (atm, bank) in enumerate(all_atms, 1):
            print(DISPLAY_ATM_ITEM.format(i, atm.atm_id, bank.name, atm.location))

        try:
            choice = int(input(ENTER_SELECT_ATM))
            if choice < 1 or choice > len(all_atms):
                print(ERR_INVALID_SELECTION)
                return
        except ValueError:
            print(ERR_NOT_A_NUMBER)
            return

        selected_atm, selected_bank = all_atms[choice - 1]
        self.atm_menu(selected_atm, selected_bank)

    def atm_menu(self, atm, bank):
        """Display and process the ATM operations menu.

        Each transaction (balance check, deposit, withdraw, change PIN)
        requires the user to authenticate with their card number and PIN.

        Args:
            atm (ATM): The selected ATM instance.
            bank (Bank): The bank that owns the selected ATM.

        Options:
            1. Check account balance
            2. Make a deposit
            3. Make a withdrawal
            4. Change ATM PIN
            5. Return to main menu
        """
        users = bank.users
        while True:
            print(HEADER_ATM_MENU)
            print(DISPLAY_ATM_INFO.format(atm.atm_id))
            print(DISPLAY_ATM_LOCATION.format(atm.location))
            print(MENU_ATM_BALANCE)
            print(MENU_ATM_DEPOSIT)
            print(MENU_ATM_WITHDRAW)
            print(MENU_ATM_CHANGE_PIN)
            print(MENU_ATM_BACK)

            choice = input(ENTER_CHOICE)
            if choice == "5":
                break
            if choice not in ("1", "2", "3", "4"):
                print(ERR_INVALID_CHOICE_RANGE.format(5))
                continue

            user = self.authenticate_user(users)
            if user is None:
                continue

            if choice == "1":
                atm.check_balance(user)
            elif choice == "2":
                atm.deposit(user)
            elif choice == "3":
                atm.withdraw(user)
            elif choice == "4":
                user.change_pin()

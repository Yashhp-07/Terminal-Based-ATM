from .validations import get_old_pin, get_new_pin
from .constants import SUCCESS_PIN_CHANGED

class User:
    """
    Represents a bank customer with their personal and account details.

    Attributes:
        user_id (str): Auto-generated unique ID for this user.
        name (str): Full name of the user.
        dob (str): Date of birth in DD/MM/YYYY format.
        phone_number (str): 10-digit phone number.
        email (str): Email address.
        aadhar_number (str): 12-digit Aadhar card number.
        pan_number (str): PAN card number in ABCDE1234F format.
        balance (float): Current account balance.
        bank_name (str): Name of the bank where the account is held.
        card_number (str): Auto-generated 16-digit debit card number.
        atm_pin (str): Auto-generated 4-digit ATM PIN.
        daily_withdrawal_amount (float): Total amount withdrawn today.
        daily_withdrawal_count (int): Number of withdrawals made today.
    """

    def __init__(self, user_id, name, dob, phone_number, email, aadhar_number, pan_number, initial_balance, bank_name, card_number, atm_pin):
        """
        Initializes a User object with personal and bank account details.

        Args:
            user_id (str): Auto-generated unique user ID.
            name (str): Full name of the user.
            dob (str): Date of birth in DD/MM/YYYY format.
            phone_number (str): 10-digit phone number.
            email (str): Email address.
            aadhar_number (str): 12-digit Aadhar card number.
            pan_number (str): PAN card number in ABCDE1234F format.
            initial_balance (float): Opening deposit amount.
            bank_name (str): Name of the bank where the account is held.
            card_number (str): Auto-generated 16-digit debit card number.
            atm_pin (str): Auto-generated 4-digit ATM PIN.
        """

        # Auto-generated unique identifier
        self.user_id = user_id

        # Details of the user required to open a bank account
        self.name = name
        self.dob = dob
        self.phone_number = phone_number
        self.email = email
        self.aadhar_number = aadhar_number
        self.pan_number = pan_number
        self.balance = initial_balance          # stored as self.balance so it denotes user account balance

        # Credentials provided by the bank to the user
        self.bank_name = bank_name
        self.card_number = card_number
        self.atm_pin = atm_pin

        # Tracker for daily transaction limit
        self.daily_withdrawal_amount = 0.0
        self.daily_withdrawal_count = 0

    def change_pin(self):
        """
        Allows the authenticated user to change their ATM PIN.

        Flow:
            1. Verify current PIN matches the stored PIN.
            2. Prompt for a new PIN — must be 4 digits and differ from current.
            3. Confirm new PIN with a second entry.
            4. Update atm_pin on success.

        Returns:
            None
        """
        old_pin = get_old_pin(self)
        new_pin = get_new_pin(self)
        self.atm_pin = new_pin
        print(SUCCESS_PIN_CHANGED)



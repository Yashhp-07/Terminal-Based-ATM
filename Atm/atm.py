class ATM:
    """
    Represents an ATM machine that handles deposits, withdrawals, and balance inquiries.

    Attributes:
        atm_id (str): Unique identifier for this ATM (format: BankName_XXX).
        bank_name (str): Name of the bank that owns this ATM.
        balance (float): Current cash available in the ATM.
        bank (Bank): Reference to the parent Bank object (used for cross-bank fee revenue).
        location (str): Physical location of the ATM.
    """

    def __init__(self, atm_id, bank_name, initial_balance, bank, location):
        """
        Initializes an ATM with identification, cash, and location details.

        Args:
            atm_id (str): Auto-generated ATM ID (e.g., HDFC_001).
            bank_name (str): Name of the bank that owns this ATM.
            initial_balance (float): Starting cash loaded into the ATM.
            bank (Bank): Reference to the parent Bank object.
            location (str): Physical location of the ATM.
        """
        self.atm_id = atm_id
        self.bank_name = bank_name
        self.balance = initial_balance
        self.bank = bank
        self.location = location

    def deposit(self, current_user):
        """
        Handles a cash deposit from a user into the ATM.

        Deposit rules:
            - Cross-bank deposits are not allowed (card must belong to the same bank).
            - Minimum deposit: Rs. 100.
            - Deposit must be in multiples of Rs. 100.

        Args:
            current_user (User): The user making the deposit.
        """
        if self.bank_name != current_user.bank_name:
            print("Cross-bank deposits are not allowed.")
            return

        amount = get_deposit_amount()
        current_user.balance += amount
        self.balance += amount
        print(f"Successfully deposited Rs.{amount:.2f}. New balance: Rs.{current_user.balance:.2f}")

    def check_balance(self, current_user):
        """
        Displays the account balance and related details for the authenticated user.

        Args:
            current_user (User): The authenticated user whose balance is being checked.
        """
        print("\n--- Account Balance ---")
        print(f"Account Holder: {current_user.name}")
        print(f"Card Number: {current_user.card_number}")
        print(f"Bank: {current_user.bank_name}")
        print(f"Current Balance: Rs.{current_user.balance:.2f}")
        print("-" * 25)

    def withdraw(self, user):
        """
        Handles a cash withdrawal from the ATM by an authenticated user.

        Withdrawal rules:
            - Minimum withdrawal: Rs. 100.
            - Withdrawal must be in multiples of Rs. 100.
            - Maximum withdrawal per transaction: Rs. 10,000.
            - ATM must have sufficient cash.
            - User must have sufficient balance.
            - Limited to 10 withdrawals per day.
            - Cross-bank withdrawals incur a 5% fee (credited to the ATM's bank).

        Args:
            user (User): The authenticated user making the withdrawal.
        """
        amount = get_withdraw_amount()

        if self.balance < amount:
            print("Insufficient funds in the ATM. Please try a smaller amount.")
            return

        if user.balance < amount:
            print("Insufficient balance in your account.")
            return

        if user.daily_withdrawal_count >= 10:
            print("Daily withdrawal limit reached. Maximum 10 withdrawals per day.")
            return

        fee = 0
        if self.bank_name != user.bank_name:
            fee = amount * 0.05
            total_deduction = amount + fee
            if user.balance < total_deduction:
                print("Insufficient balance to cover withdrawal amount plus cross-bank fee.")
                return
            user.balance -= total_deduction
            self.bank.balance += fee
        else:
            user.balance -= amount

        self.balance -= amount
        user.daily_withdrawal_amount += amount
        user.daily_withdrawal_count += 1

        print(f"Successfully withdrew Rs.{amount:.2f}.")
        if fee > 0:
            print(f"Cross-bank fee: Rs.{fee:.2f}")
        print(f"Remaining balance: Rs.{user.balance:.2f}")


def get_deposit_amount():
    """
    Prompts the user for a deposit amount and validates it.

    Rules:
        - Must be a valid number.
        - Minimum: Rs. 100.
        - Must be in multiples of Rs. 100.

    Returns:
        float: The validated deposit amount.
    """
    while True:
        value = input("Enter deposit amount (minimum Rs. 100, multiples of 100): ")
        try:
            amount = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if amount < 100:
            print("Minimum deposit amount is Rs. 100.")
            continue
        if int(amount) % 100 != 0:
            print("Deposit amount must be in multiples of 100.")
            continue
        return amount


def get_card_number(users):
    """
    Prompts the user for their card number and validates it.

    Rules:
        - Must contain only digits.
        - Must be exactly 16 characters long.
        - Must exist in the provided users dictionary.

    Args:
        users (dict): Dictionary of users keyed by card number.

    Returns:
        str: The validated card number.
    """
    while True:
        card_number = input("Enter your card number: ")
        if not card_number.isdigit():
            print("Card number must contain only digits.")
            continue
        if len(card_number) != 16:
            print("Card number must be exactly 16 digits.")
            continue
        if card_number not in users:
            print("Invalid card number. No account found.")
            continue
        return card_number


def get_pin():
    """
    Prompts the user for their 4-digit ATM PIN and validates it.

    Rules:
        - Must contain only digits.
        - Must be exactly 4 characters long.

    Returns:
        str: The validated PIN.
    """
    while True:
        pin = input("Enter your PIN: ")
        if not pin.isdigit():
            print("PIN must contain only digits.")
            continue
        if len(pin) != 4:
            print("PIN must be exactly 4 digits.")
            continue
        return pin


def get_withdraw_amount():
    """
    Prompts the user for a withdrawal amount and validates it.

    Rules:
        - Must be a valid number.
        - Minimum: Rs. 100.
        - Maximum: Rs. 10,000 per transaction.
        - Must be in multiples of Rs. 100.

    Returns:
        float: The validated withdrawal amount.
    """
    while True:
        value = input("Enter withdrawal amount (Rs. 100 - Rs. 10,000, multiples of 100): ")
        try:
            amount = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if amount < 100:
            print("Minimum withdrawal amount is Rs. 100.")
            continue
        if amount > 10000:
            print("Maximum withdrawal amount per transaction is Rs. 10,000.")
            continue
        if int(amount) % 100 != 0:
            print("Withdrawal amount must be in multiples of 100.")
            continue
        return amount
